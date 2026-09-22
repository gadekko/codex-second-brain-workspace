# Codex second-brain workspace bundle

This bundle contains both workflows needed to turn a local project into a connected AI workspace:

1. [Set up the workspace](skills/setup-codex-workspace/SKILL.md): project registration, connectors, project memory, a demonstrated workflow and requested recurring work.
2. [Build the second brain](skills/create-project-second-brain/SKILL.md): inventory local sources, preserve originals, create complete Markdown clones, read them and organize linked topic clusters and source indexes.

All method files and the general builder's structural audit helper are included. No separately installed second-brain skill, database or memory service is required. The specialized dispute and investment builders mentioned as optional routes are not included.

## Use without installation

Extract the ZIP and give Codex the extracted folder. You do not need to have a project folder or any accounts connected yet. Paste this request, replacing only the bundle path (or attach the extracted folder and refer to it):

> Read `/path/to/codex-second-brain-workspace/skills/setup-codex-workspace/SKILL.md` and guide me through setup from the beginning. First ask what my second brain is for and whether I have a local project folder. Help me create or select that folder and add the project in Codex. Find out which tools I use, then walk me through connecting each needed service, including email and calendar where relevant, one step at a time and verify it works. After setup, use the included builder to preserve my local originals, create full Markdown clones, read them and organize linked topic clusters and source indexes. Help me set up project memory and propose a useful recurring workflow.

Codex should stay with you through each sign-in step and check the result before moving on. You can say “I’m not sure”, ask for help finding a button or choose to defer a service. It should not assume accounts are connected or a project folder already exists.

For only the local second brain, without connector or automation setup:

> Read `/path/to/codex-second-brain-workspace/skills/create-project-second-brain/SKILL.md` and its full local-corpus reference. Build the second brain from all substantive files in `/path/to/my-project`, including complete Markdown clones and linked topic clusters. Preserve originals and verify source coverage and retrieval.

Keep the method outside the source corpus if convenient; otherwise the builder must explicitly exclude it and its generated outputs from intake. The skill folder is never the destination for private project knowledge.

## Install for repeated use

Ask Codex to install both skill folders under `skills/` into its current supported user skill location. If a skill with the same name exists, compare versions, preserve a backup and reconcile changes before replacing it. Both folders must remain siblings because the setup skill links directly to the bundled builder. Do not paste the whole bundle into a single `SKILL.md`.

After installation, invoke `$setup-codex-workspace` or `$create-project-second-brain`. Verify that the current app discovers them; filesystem copying alone does not prove discovery. The direct-file instructions above work without registration.

## What the bundle needs

It is a self-contained Codex method package, not a standalone offline application. Codex still needs access to the chosen local files and suitable tools for their formats. The structural audit helper uses Python 3.9+ and the standard library. PDF/Office conversion, OCR and media transcription may require additional installed tools; unsupported inputs remain reported gaps until resolved. The skills guide tool selection and setup rather than silently installing or uploading to a new service.

Connectors require the user's actual sign-in and supported account permissions. Recurring execution requires a real scheduler and an available execution environment. None is activated by downloading or reading this bundle.

## Verification and maintenance

The [verification report](VERIFICATION.md) describes what was checked for this release. `MANIFEST.json` lists the exact distributed files and hashes; it excludes itself to avoid self-referential hashing. Verify the manifest before sharing or installation, and regenerate it only after intentional reviewed changes.

For the completed project, the builder writes its own source catalog, coverage records, topic map and maintenance instructions. Those private records remain separate from this reusable package.
