# Repository work

This repository contains reusable methods, not a user's private second brain. Keep client files, account identities, credentials, runtime memory and real project evidence outside it. Use synthetic examples for testing.

Preserve the first-time-user onboarding: ask project purpose and whether a local folder exists, then guide one needed connection at a time and verify it. Do not assume a ZIP upload, installed plugin or completed sign-in proves that the full workflow works.

After connections, agree the person's mail/calendar discovery scope. Learn only from authorized history, distinguish self-authored voice and observed cadence from confirmed preferences, review the workflow map, and create/test actual personalized skills. All user-specific evidence, profiles and generated personal skills live outside this repository in that person's private workspace. Never use the repository author's history as example data.

Keep the two skill folders as siblings so direct-file routing works. The general builder must preserve originals, create complete Markdown clones or explicit gaps, track actual reading coverage and organize source-linked topic clusters.

After method edits, inspect the diff, refresh MANIFEST.json deliberately, then run:

```sh
python3 -B scripts/build_bundle.py --check
python3 -B -m unittest discover -s skills/create-project-second-brain/scripts -p 'test_audit_brain.py' -v
python3 -B -m unittest discover -s scripts -p 'test_build_bundle.py' -v
python3 -B scripts/build_bundle.py
```

Do not claim a novice-user or live-account test from structural checks. Keep the verification report candid about tested scope.
