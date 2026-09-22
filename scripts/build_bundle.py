#!/usr/bin/env python3
"""Check or build the method-only distribution; no external dependencies."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def payload():
    files = [ROOT / 'START_HERE.md', ROOT / 'VERIFICATION.md']
    for p in (ROOT / 'skills').rglob('*'):
        if p.name == '.DS_Store' or '__pycache__' in p.parts or p.suffix == '.pyc':
            continue
        if p.is_symlink():
            raise ValueError(f'Symlinks cannot be distributed: {p}')
        if p.is_file():
            files.append(p)
    for p in files:
        if p.is_symlink() or not p.is_file():
            raise ValueError(f'Expected a regular release file: {p}')
    return sorted(files)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--check', action='store_true')
    mode.add_argument('--refresh', action='store_true', help='Record intentional changes to release files')
    args = parser.parse_args()
    files = payload()
    hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    manifest_path = ROOT / 'MANIFEST.json'
    if args.refresh:
        manifest_path.write_text(json.dumps({'schema_version': 1, 'files': hashes,
                                            'note': 'MANIFEST.json excludes itself.'}, indent=2) + '\n')
        print('Refreshed manifest. Review and commit this change with the method edits.')
        return
    manifest = json.loads(manifest_path.read_text())
    if manifest.get('schema_version') != 1 or manifest.get('files') != hashes:
        raise ValueError('Release files differ from MANIFEST.json. Inspect changes before --refresh.')
    helper = ROOT / 'skills/create-project-second-brain/scripts/audit_brain.py'
    spec = importlib.util.spec_from_file_location('brain_audit', helper)
    audit = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(audit)
    links = 0
    for p in files:
        if p.suffix != '.md':
            continue
        for target, line in audit.inline_links(p.read_text(encoding='utf-8')):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            destination = (p.parent / unquote(url.path)).resolve()
            if not destination.is_relative_to(ROOT) or not destination.exists():
                raise ValueError(f'Broken/escaping link: {p.relative_to(ROOT)}:{line}: {target}')
            if destination.is_file() and destination not in files and destination != manifest_path:
                raise ValueError(f'Link is outside distributed payload: {p}:{line}: {target}')
            links += 1
    print(f'Verified {len(files)} payload files and {links} local file links; anchors not checked.')
    if args.check:
        return
    destination = ROOT / 'dist/codex-second-brain-workspace.zip'
    destination.parent.mkdir(exist_ok=True)
    members = files + [manifest_path]
    with zipfile.ZipFile(destination, 'w', zipfile.ZIP_DEFLATED) as archive:
        for p in members:
            archive.write(p, Path('codex-second-brain-workspace') / p.relative_to(ROOT))
    with zipfile.ZipFile(destination) as archive:
        if archive.testzip() is not None or len(archive.namelist()) != len(members):
            raise ValueError('ZIP integrity or member-count check failed')
        for p in members:
            name = str(Path('codex-second-brain-workspace') / p.relative_to(ROOT))
            if archive.read(name) != p.read_bytes():
                raise ValueError(f'ZIP byte mismatch: {name}')
    print(f'Built and byte-verified {destination.relative_to(ROOT)} ({len(members)} files).')


if __name__ == '__main__':
    main()
