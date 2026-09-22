# Codex second-brain workspace bundle

This bundle contains three workflows needed to turn a local project into a connected AI workspace:

1. [Set up the workspace](skills/setup-codex-workspace/SKILL.md): project registration, guided connections, learning the person's writing style and routines, reviewing a workflow map, creating and testing personalized skills, project memory and requested recurring work.
2. [Build the second brain](skills/create-project-second-brain/SKILL.md): inventory local sources, preserve originals, create complete Markdown clones, read them and organize linked topic clusters and source indexes.

3. [Maintain the workspace](skills/maintain-codex-workspace/SKILL.md): refresh changed sources, reconcile attention items and review personal skills for tested, evidence-based updates with rollback.

All method files and the general builder's structural audit helper are included. No separately installed second-brain skill, database or memory service is required. The specialized dispute and investment builders mentioned as optional routes are not included.

The goal is an integrated work environment that uses your context across tools and improves its knowledge and skills from your corrections and actual results. Your own private folder or repository is meant to hold your real work and learned context. Only this reusable toolkit stays generic; it contains none of its creator's private work. The included [continuous-learning method](skills/setup-codex-workspace/references/continuous-learning.md) sets up ongoing context maintenance, skill revision, testing and rollback.

## Use without installation

Extract the ZIP and give Codex the extracted folder. You do not need to have a project folder or any accounts connected yet. Paste this request, replacing only the bundle path (or attach the extracted folder and refer to it):

> Read `/path/to/codex-second-brain-workspace/skills/setup-codex-workspace/SKILL.md` and guide me through setup from the beginning. First ask what my second brain is for and whether I have a local project folder. Help me create or select that folder and add the project in Codex. Find out which tools I use, then walk me through connecting each needed service, including email and calendar where relevant, one step at a time and verify it works. Agree which accounts, dates and areas you may examine. Learn my writing style from my own messages, identify routines from relevant threads and calendars, and review a workflow map with me. Create, install and test the personal skills I select, keeping all personal information in my private workspace. Then use the included builder to preserve my local originals, create full Markdown clones, read them and organize linked topic clusters and source indexes. Make short requests automatically use the relevant context and my confirmed writing style. Help me set up project memory, daily workspace and skill maintenance, attention checks and meeting preparation on the schedules I choose.

Codex should stay with you through each sign-in step and check the result before moving on. You can say “I’m not sure”, ask for help finding a button or choose to defer a service. It should not assume accounts are connected or a project folder already exists.

You choose what history Codex may review. It should ask you to correct its draft voice/profile and workflow map, then create real skill files and help you try them. If you have little history or prefer not to share it, it can interview you and use examples you supply. Private messages, calendar data, learned profiles and generated personal skills stay in your own workspace, never in this reusable bundle.

For only the local second brain, without connector or automation setup:

> Read `/path/to/codex-second-brain-workspace/skills/create-project-second-brain/SKILL.md` and its full local-corpus reference. Build the second brain from all substantive files in `/path/to/my-project`, including complete Markdown clones and linked topic clusters. Preserve originals and verify source coverage and retrieval.

Keep the method outside the source corpus if convenient; otherwise the builder must explicitly exclude it and its generated outputs from intake. The skill folder is never the destination for private project knowledge.

## Install for repeated use

Ask Codex to install all three skill folders under `skills/` into its current supported user skill location. If a skill with the same name exists, compare versions, preserve a backup and reconcile changes before replacing it. All three folders must remain siblings because the setup skill links directly to the bundled builder. Do not paste the whole bundle into a single `SKILL.md`.

After installation, invoke `$setup-codex-workspace` or `$create-project-second-brain`; use `$maintain-codex-workspace` for maintenance. Normal daily work should use short requests such as “Draft a reply”, with context and style loaded automatically. Verify that the current app discovers them; filesystem copying alone does not prove discovery. The direct-file instructions above work without registration.

## Optional Jev connection

Ask Codex to follow the [Jev setup guide](skills/setup-codex-workspace/references/jev-decisions.md) if you want to try lower-cost decisions for workflow selection and source relevance. It will help you obtain official TypeSafe access, configure a private API key and test the connection with synthetic data before evaluating your authorized examples. Never paste the key into chat. The included adapter starts disabled and then uses shadow mode until its quality has been checked. Your normal Codex workflow remains available throughout.

## What the bundle needs

It is a self-contained Codex method package, not a standalone offline application. Codex still needs access to the chosen local files and suitable tools for their formats. The structural audit helper uses Python 3.9+ and the standard library. PDF/Office conversion, OCR and media transcription may require additional installed tools; unsupported inputs remain reported gaps until resolved. The skills guide tool selection and setup rather than silently installing or uploading to a new service.

Connectors require the user's actual sign-in and supported account permissions. Recurring execution requires a real scheduler and an available execution environment. None is activated by downloading or reading this bundle.

## Verification and maintenance

The [verification report](VERIFICATION.md) describes what was checked for this release. `MANIFEST.json` lists the exact distributed files and hashes; it excludes itself to avoid self-referential hashing. Verify the manifest before sharing or installation, and regenerate it only after intentional reviewed changes.

For the completed project, the builder writes its own source catalog, coverage records, topic map and maintenance instructions. Those private records remain separate from this reusable package.

## License

This toolkit is licensed under GNU Affero General Public License version 3 only (`AGPL-3.0-only`). The full [LICENSE](LICENSE) is included in this ZIP and each skill folder.
