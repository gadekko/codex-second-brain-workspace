#!/usr/bin/env python3
"""Read-only structural audit of a project second brain. Standard library only."""

import argparse
import hashlib
import json
from pathlib import Path, PureWindowsPath
import re
import sys
from urllib.parse import unquote, urlsplit


ROLES = ("entrypoint", "scope", "status", "decisions", "tasks", "sources", "maintenance")
LIMITATIONS = [
    "Checks manifest structure, selected local file targets and recorded source hashes only.",
    "Does not verify heading anchors, web destinations, factual accuracy, instruction quality or app behavior.",
    "Link coverage is inline Markdown links/images in mapped and supporting documents; reference-style links, HTML and unmapped documents are not checked.",
    "Preserved-source hashes prove equality to the manifest, not authenticity, full-corpus coverage or substantive review.",
    "Does not execute project content, use the network or write files.",
]


def inline_links(text):
    """Yield (destination, line) for inline links outside code; handle nested ()."""
    # Keep line numbers while ignoring fenced and inline code examples.
    lines = text.splitlines(keepends=True)
    fence = None
    for index, line in enumerate(lines):
        match = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if fence:
            lines[index] = "\n" if line.endswith("\n") else ""
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence):
                fence = None
        elif match:
            fence = match[1]
            lines[index] = "\n" if line.endswith("\n") else ""
    text = "".join(lines)
    text = re.sub(r"(`+)([^`]*?)\1", lambda m: "\n" * m[0].count("\n"), text)
    for match in re.finditer(r"!?\[(?:\\.|[^\]\\\n])*\]\(", text):
        start = match.end()
        while start < len(text) and text[start].isspace():
            start += 1
        cursor = start
        depth = 0
        angle = cursor < len(text) and text[cursor] == "<"
        if angle:
            start += 1
            cursor += 1
        while cursor < len(text):
            char = text[cursor]
            if char == "\\" and cursor + 1 < len(text):
                cursor += 2
                continue
            if angle and char == ">":
                break
            if not angle:
                if char == "(":
                    depth += 1
                elif char == ")":
                    if depth == 0:
                        break
                    depth -= 1
                elif char.isspace() and depth == 0:
                    break
            cursor += 1
        if cursor < len(text):
            target = re.sub(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\]\\^_`{|}~])", r"\1", text[start:cursor])
            yield target, text[:match.start()].count("\n") + 1


def audit(root, manifest="brain.json"):
    errors = []
    counts = {"documents": 0, "documents_read": 0, "local_links": 0,
              "external_links_skipped": 0, "preserved_sources": 0, "hashes_checked": 0}

    def error(code, path, message, line=None):
        item = {"code": code, "path": str(path), "message": message}
        if line is not None:
            item["line"] = line
        errors.append(item)

    def result():
        return {"ok": not errors, "errors": errors, "counts": counts, "limitations": LIMITATIONS}

    try:
        root = Path(root).resolve()
        if not root.is_dir():
            error("root", root, "Project root must be an existing directory.")
            return result()
    except (OSError, RuntimeError, ValueError, TypeError) as exc:
        error("root", str(root), str(exc))
        return result()

    def local_path(value, label, base=None):
        if not isinstance(value, str) or not value.strip() or "\x00" in value:
            error("path", label, "Expected a nonempty relative path without null bytes.")
            return None
        if Path(value).is_absolute() or PureWindowsPath(value).is_absolute():
            error("path", label, "Absolute paths are not portable; use a path inside the project root.")
            return None
        try:
            candidate = ((base or root) / value).resolve()
            if not candidate.is_relative_to(root):
                error("escape", label, "Path or symlink resolves outside the project root.")
                return None
            return candidate
        except (OSError, RuntimeError, ValueError) as exc:
            error("path", label, str(exc))
            return None

    manifest_path = local_path(manifest, "manifest")
    if manifest_path is None:
        return result()
    try:
        if not manifest_path.is_file():
            raise OSError("Manifest must be an existing regular file.")
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError) as exc:
        error("manifest", manifest, f"Cannot read a UTF-8 JSON manifest: {exc}")
        return result()
    if not isinstance(data, dict):
        error("manifest", manifest, "Manifest must be a JSON object.")
        return result()
    if type(data.get("schema_version")) is not int or data["schema_version"] != 1:
        error("schema_version", manifest, "Expected schema_version: 1.")

    documents = data.get("documents")
    if not isinstance(documents, dict):
        error("documents", manifest, "documents must map role names to relative Markdown file paths.")
        documents = {}
    for role in ROLES:
        if role not in documents:
            error("missing_role", manifest, f"Required document role is missing: {role}.")
    supporting = data.get("supporting_documents", [])
    if not isinstance(supporting, list):
        error("supporting_documents", manifest, "supporting_documents must be an array of relative Markdown file paths.")
        supporting = []
    unique_documents = {}
    entries = [(f"documents.{role}", value) for role, value in documents.items()]
    entries += [(f"supporting_documents[{index}]", value) for index, value in enumerate(supporting)]
    for label, value in entries:
        path = local_path(value, label)
        if path is None:
            continue
        if path.suffix.lower() != ".md":
            error("document_type", label, "Mapped documents must be Markdown (.md) files.")
            continue
        unique_documents.setdefault(path, value)
    counts["documents"] = len(unique_documents)
    for path, relative in unique_documents.items():
        try:
            if not path.is_file():
                raise OSError("Document must be an existing regular file.")
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            error("document", relative, f"Cannot read document: {exc}")
            continue
        counts["documents_read"] += 1
        for target, line in inline_links(content):
            if not target or target.startswith("#"):
                continue
            try:
                url = urlsplit(target)
            except ValueError as exc:
                error("link", relative, f"Invalid link target {target!r}: {exc}", line)
                continue
            if url.scheme or url.netloc:
                counts["external_links_skipped"] += 1
                continue
            if not url.path:
                continue
            counts["local_links"] += 1
            destination = local_path(unquote(url.path), f"{relative}:{line}: {target}", path.parent)
            if destination is not None:
                try:
                    if not destination.exists():
                        error("missing_link", relative, f"Local target does not exist: {target}", line)
                except (OSError, ValueError) as exc:
                    error("link", relative, str(exc), line)

    sources = data.get("preserved_sources", [])
    if not isinstance(sources, list):
        error("preserved_sources", manifest, "preserved_sources must be an array of objects with id, path and sha256.")
        sources = []
    seen_ids = set()
    for index, source in enumerate(sources):
        label = f"preserved_sources[{index}]"
        counts["preserved_sources"] += 1
        if not isinstance(source, dict):
            error("source", label, "Expected an object with id, path and sha256.")
            continue
        identifier = source.get("id")
        if not isinstance(identifier, str) or not identifier.strip():
            error("source_id", label, "Source id must be a nonempty string.")
        elif identifier in seen_ids:
            error("duplicate_id", label, f"Duplicate source id: {identifier}.")
        else:
            seen_ids.add(identifier)
        path = local_path(source.get("path"), label + ".path")
        digest = source.get("sha256")
        if not isinstance(digest, str) or re.fullmatch(r"[0-9a-fA-F]{64}", digest) is None:
            error("source_hash", label, "sha256 must contain exactly 64 hexadecimal characters.")
            continue
        if path is None:
            continue
        try:
            if not path.is_file():
                raise OSError("Preserved source must be an existing regular file.")
            actual = hashlib.sha256()
            with path.open("rb") as handle:
                for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                    actual.update(chunk)
            counts["hashes_checked"] += 1
            if actual.hexdigest() != digest.lower():
                error("hash_mismatch", source["path"], f"Expected {digest.lower()}; observed {actual.hexdigest()}.")
        except OSError as exc:
            error("source", source.get("path"), f"Cannot read preserved source: {exc}")
    return result()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", help="Project root to inspect")
    parser.add_argument("--manifest", default="brain.json", help="Manifest path relative to root")
    args = parser.parse_args()
    report = audit(args.root, args.manifest)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
