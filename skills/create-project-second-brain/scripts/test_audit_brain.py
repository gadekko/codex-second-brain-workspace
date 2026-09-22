#!/usr/bin/env python3
"""Isolated structural and containment tests for audit_brain.py."""

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from audit_brain import ROLES, audit


class BrainAuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "project"
        self.root.mkdir()
        (self.root / "context.md").write_text("# Context\n", encoding="utf-8")
        self.manifest = {"schema_version": 1, "documents": {role: "context.md" for role in ROLES}}
        self.save()

    def save(self):
        (self.root / "brain.json").write_text(json.dumps(self.manifest), encoding="utf-8")

    def add_source(self):
        source = self.root / "original.txt"
        source.write_bytes(b"original bytes\n")
        self.manifest["preserved_sources"] = [{"id": "input-1", "path": source.name,
                                              "sha256": hashlib.sha256(source.read_bytes()).hexdigest()}]
        self.save()
        return source

    def codes(self, report):
        return {error["code"] for error in report["errors"]}

    def test_valid_lightweight_mapping_and_inline_links(self):
        (self.root / "with spaces(1).txt").write_text("content")
        (self.root / "context.md").write_text(
            '# Context\n[local](<with spaces(1).txt> "title")\n'
            '[encoded](with%20spaces%281%29.txt#not-checked)\n'
            '[site](https://example.com/a) [mail](mailto:test@example.com) [heading](#x)\n'
            '```md\n[example](missing-example.md)\n```\n`[inline](missing.md)`\n')
        self.add_source()
        report = audit(self.root)
        self.assertTrue(report["ok"], report)
        self.assertEqual(report["counts"]["documents_read"], 1)
        self.assertEqual(report["counts"]["local_links"], 2)
        self.assertEqual(report["counts"]["hashes_checked"], 1)

    def test_malformed_json_and_structures_report_errors(self):
        for value in (None, [], {"schema_version": True, "documents": [],
                                 "supporting_documents": {}, "preserved_sources": [None, {"id": []}]}):
            with self.subTest(value=value):
                self.manifest = value
                self.save()
                report = audit(self.root)
                self.assertFalse(report["ok"])
                self.assertTrue(report["errors"])
        (self.root / "brain.json").write_text("{broken", encoding="utf-8")
        self.assertIn("manifest", self.codes(audit(self.root)))

    def test_preserved_source_bytes_changed(self):
        source = self.add_source()
        source.write_bytes(b"altered bytes\n")
        report = audit(self.root)
        self.assertIn("hash_mismatch", self.codes(report))
        self.assertEqual(report["counts"]["hashes_checked"], 1)

    def test_missing_and_escaping_local_links(self):
        outside = self.root.parent / "outside.md"
        outside.write_text("outside")
        (self.root / "context.md").write_text("[missing](missing.md)\n[escape](../outside.md)\n")
        report = audit(self.root)
        self.assertEqual(self.codes(report), {"missing_link", "escape"})
        self.assertEqual(report["errors"][0]["line"], 1)

    def test_source_symlink_cannot_escape_root(self):
        source = self.add_source()
        original = source.read_bytes()
        source.unlink()
        outside = self.root.parent / "external.txt"
        outside.write_bytes(original)
        source.symlink_to(outside)
        report = audit(self.root)
        self.assertIn("escape", self.codes(report))
        self.assertEqual(report["counts"]["hashes_checked"], 0)

    def test_duplicate_source_ids(self):
        self.add_source()
        self.manifest["preserved_sources"] *= 2
        self.save()
        self.assertIn("duplicate_id", self.codes(audit(self.root)))

    def test_invalid_hash_and_missing_source(self):
        self.manifest["preserved_sources"] = [
            {"id": "a", "path": "original.txt", "sha256": "short"},
            {"id": "b", "path": "missing.txt", "sha256": "0" * 64}]
        self.save()
        self.assertEqual(self.codes(audit(self.root)), {"source_hash", "source"})

    def test_documents_and_manifest_must_stay_inside_root(self):
        self.manifest["documents"]["scope"] = "../outside.md"
        self.manifest["supporting_documents"] = [str(self.root / "context.md"), 42]
        self.save()
        self.assertEqual(self.codes(audit(self.root)), {"escape", "path"})
        self.assertIn("escape", self.codes(audit(self.root, "../brain.json")))

    def test_cli_returns_json_and_failure_exit_status(self):
        script = Path(__file__).with_name("audit_brain.py")
        for expected in (0, 1):
            with self.subTest(expected=expected):
                if expected:
                    (self.root / "context.md").unlink()
                run = subprocess.run([sys.executable, str(script), str(self.root)], capture_output=True, text=True)
                self.assertEqual(run.returncode, expected)
                self.assertEqual(json.loads(run.stdout)["ok"], expected == 0)
                self.assertEqual(run.stderr, "")

    @unittest.skipUnless(hasattr(os, "mkfifo"), "Named pipes are unavailable on this platform")
    def test_named_pipes_are_rejected_without_blocking(self):
        script = Path(__file__).with_name("audit_brain.py")
        for filename, code in (("brain.json", "manifest"), ("context.md", "document"),
                               ("original.txt", "source")):
            with self.subTest(filename=filename):
                self.add_source()
                (self.root / "context.md").write_text("# Context\n", encoding="utf-8")
                target = self.root / filename
                target.unlink()
                os.mkfifo(target)
                try:
                    run = subprocess.run([sys.executable, str(script), str(self.root)],
                                         capture_output=True, text=True, timeout=3)
                    self.assertEqual(run.returncode, 1)
                    self.assertIn(code, self.codes(json.loads(run.stdout)))
                    self.assertEqual(run.stderr, "")
                finally:
                    target.unlink()
                self.save()


if __name__ == "__main__":
    unittest.main()
