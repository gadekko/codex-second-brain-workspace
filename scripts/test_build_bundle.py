import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile


class BundleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'repo'
        shutil.copytree(Path(__file__).resolve().parents[1], self.root,
                        ignore=shutil.ignore_patterns('.git', 'dist', '__pycache__'))

    def run_builder(self, *args):
        return subprocess.run([sys.executable, '-B', str(self.root / 'scripts/build_bundle.py'), *args],
                              text=True, capture_output=True)

    def test_valid_build_excludes_non_payload(self):
        (self.root / 'private-note.txt').write_text('Synthetic non-release data')
        result = self.run_builder()
        self.assertEqual(result.returncode, 0, result.stderr)
        with zipfile.ZipFile(self.root / 'dist/codex-second-brain-workspace.zip') as z:
            expected = set(json.loads((self.root / 'MANIFEST.json').read_text())['files']) | {'MANIFEST.json'}
            self.assertEqual({n.split('/', 1)[1] for n in z.namelist()}, expected)
            license_bytes = (self.root / 'LICENSE').read_bytes()
            for name in ['LICENSE', 'skills/setup-codex-workspace/LICENSE',
                         'skills/create-project-second-brain/LICENSE']:
                self.assertEqual(z.read('codex-second-brain-workspace/' + name), license_bytes)

    def test_missing_license_blocks_release(self):
        (self.root / 'LICENSE').unlink()
        self.assertNotEqual(self.run_builder('--refresh').returncode, 0)

    def test_changed_or_new_payload_fails_without_refresh(self):
        (self.root / 'skills/setup-codex-workspace/extra.md').write_text('New method file')
        self.assertNotEqual(self.run_builder('--check').returncode, 0)
        self.assertFalse((self.root / 'dist').exists())

    def test_refresh_does_not_hide_broken_link(self):
        p = self.root / 'START_HERE.md'
        p.write_text(p.read_text() + '\n[Missing](not-present.md)\n')
        self.assertEqual(self.run_builder('--refresh').returncode, 0)
        self.assertNotEqual(self.run_builder('--check').returncode, 0)

    def test_symlink_payload_rejected(self):
        (self.root / 'skills/external.md').symlink_to(self.root / 'README.md')
        self.assertNotEqual(self.run_builder('--refresh').returncode, 0)

    def test_private_markers_block_even_manifest_refresh(self):
        p = self.root / 'skills/setup-codex-workspace/private.md'
        markers = ['person@private.invalid', '/Users/synthetic-person/mail.txt',
                   'ghp_' + 'a' * 30, '-----BEGIN PRIVATE KEY-----']
        for marker in markers:
            with self.subTest(kind=marker[:8]):
                p.write_text(marker)
                result = self.run_builder('--refresh')
                self.assertNotEqual(result.returncode, 0)
                self.assertNotIn(marker, result.stderr)

    def test_reserved_example_address_is_allowed(self):
        p = self.root / 'skills/setup-codex-workspace/synthetic.md'
        p.write_text('Synthetic contact: person@example.org')
        self.assertEqual(self.run_builder('--refresh').returncode, 0)
        self.assertEqual(self.run_builder('--check').returncode, 0)


if __name__ == '__main__':
    unittest.main()
