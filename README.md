# Codex Second-Brain Workspace

A guided setup for turning a local project into a source-linked second brain and connected AI workspace.

Start with no project folder and no connected accounts. The setup skill asks what the project is for, helps create or select a local folder, and walks through each needed connection one step at a time. With an agreed scope, it learns from the person's own sent messages, relevant threads and calendar history, maps writing style and recurring workflows, and creates and tests personalized skills. The included builder preserves originals, creates full Markdown clones, reads the material, and organizes linked topic clusters and source indexes.

## Start here

1. Download this repository using **Code → Download ZIP**, then extract it.
2. Give Codex access to the extracted folder, or attach the ZIP if your Codex environment can read it.
3. Send:

> Read START_HERE.md in this bundle and guide me through setup from the beginning. Ask what my second brain is for and whether I have a local project folder. Help me connect each needed tool one step at a time. Agree which messages and calendars you may review, learn my writing style and routines, and help me review a workflow map. Create and test useful personalized skills in my private workspace, then build the second brain and set up the recurring work I choose.

Follow [START_HERE.md](START_HERE.md) for direct-file use, installation and the local-only option. You still complete your own sign-ins, account permissions and project choices. Do not put your passwords or private project documents in this repository.

## Included skills

| Skill | Purpose |
| --- | --- |
| [setup-codex-workspace](skills/setup-codex-workspace/SKILL.md) | Guided connections; scoped email/calendar discovery; voice and workflow profiles; personalized skill creation, installation and testing; memory and automation setup |
| [create-project-second-brain](skills/create-project-second-brain/SKILL.md) | Local corpus inventory, preserved originals, full Markdown clones, topic clusters, source indexes and updates |

No separately installed second-brain skill or hosted database is required. Codex needs access to your selected files and suitable conversion/OCR tools for their formats. Recurring work requires a supported scheduler. Specialized dispute and investment builders are optional and not included.

## Verification status

See [VERIFICATION.md](VERIFICATION.md) for completed checks and limits. This is a reusable method package, not a standalone application. A full first-time-user walkthrough across real account sign-ins has not yet been demonstrated. Package validation does not establish universal source-conversion accuracy or unattended reliability.

## Build and check the downloadable bundle

Python 3.9+ with the standard library is sufficient:

```sh
python3 -B scripts/build_bundle.py --check
python3 -B -m unittest discover -s skills/create-project-second-brain/scripts -p 'test_audit_brain.py' -v
python3 -B -m unittest discover -s scripts -p 'test_build_bundle.py' -v
python3 -B scripts/build_bundle.py
```

The last command writes `dist/codex-second-brain-workspace.zip`. It packages only the method files listed in `MANIFEST.json`, not Git metadata, project documents or local caches, and verifies the archive bytes. After intentional method changes, inspect the diff, run `python3 -B scripts/build_bundle.py --refresh`, and commit the updated manifest with those changes.

GitHub Actions runs the integrity and audit-helper tests on pushes and pull requests. The workflow also checks that the distributable ZIP builds.

## Sharing

The repository contains generic methods and synthetic tests only. Learning a person's writing style and routines happens later in their selected private workspace. Raw messages, calendar events, personal profiles, account details and generated personal skills must never be copied back here or included in this distribution. Source history is read only within the accounts, date range and areas the person selects. Observed patterns remain tentative until reviewed; sign-in does not grant permission for an unrestricted scan or automatic sending.

The bundle checker rejects common private email addresses, home-directory paths and credential patterns in method payloads. This is a limited check, not proof that arbitrary prose contains no private information; inspect every intended release's content as well.

This repository is private. Only collaborators you invite can access its GitHub files. You can also share the generated ZIP separately; it contains the reusable methods, not your connected accounts or personal second brain. Give each project its own private working folder.
