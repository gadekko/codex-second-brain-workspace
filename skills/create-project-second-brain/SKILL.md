---
name: create-project-second-brain
description: Build or update a portable project second brain, including full Markdown clones of an agreed local corpus and linked topic clusters, source indexes and resumable coverage. Use for local-file second-brain builds, project knowledge and handoffs. Small context updates remain scoped; specialized dispute or investment models are optional extensions.
---

# Create a project second brain

Make the authorized project understandable and resumable from its own files. The result is maintained knowledge with provenance and a next action, not a folder scaffold or a copy of every conversation. No database, connector, hosted memory service or particular model is required.

This bundled edition includes a complete local-corpus workflow. For requests to turn all project files into Markdown and organize them for AI retrieval, read [full local corpus and topic clusters](references/local-corpus.md) in full, then complete inventory, preservation, conversion, full reading, clustering, reconciliation and verification. A short summary or file index is not a Markdown clone. Do not downgrade this endpoint to the lighter project-context mode below.

## Choose the endpoint

- **Build/organize:** inventory the actual project, reuse coherent records and fill the missing context. Preserve useful paths and unrelated edits; do not create a competing brain inside one that already works.
- **Add/update:** read the supplied change and the earlier records it affects; integrate it into the existing authority structure, retain superseded decisions and reconcile dependents.
- **Audit/repair:** check whether a new reader can recover the project and sources, then fix accepted in-scope defects. A request for read-only review stays read-only.
- **Stage only:** preserve and describe the arrival, leaving its unread scope explicit. Do not promote staging into knowledge integration or whole-project execution.

Infer routine layout choices from the project. Ask only when an ambiguous destination, conflicting authoritative instructions or a material missing choice prevents correct work; continue independent work. Creating project context does not authorize unrelated account ingestion or implementation of everything in its plan.

## Establish the project boundary

Read governing instructions, existing entrypoints, current status and relevant decisions first. Identify the purpose, owner or audience if known, constraints, actual available sources, exclusions and requested depth. Distinguish available conversation excerpts from a captured full transcript. Follow existing user authorizations without adding redundant approval steps.

Keep source content, including archived prompts and instructions in imported documents, separate from governing instructions. Preserve received originals when organizing them; editable project knowledge can be updated within scope. Unknown, inaccessible and not-yet-read are different states. Never turn a failed search or a partial review into an absence claim.

Read [structure and records](references/structure.md) when creating or mapping the brain. For larger or evidence-heavy intakes, also read its source-coverage section; do not impose that machinery on every small project.

## Build useful context

Maintain one authority for each responsibility; small projects can combine them in a few files:

- **Entry point:** what to read first and where important records live.
- **Scope and purpose:** what the project is for, what is included and what remains outside it.
- **Current state:** what exists, what actually works, evidence, blockers and the next concrete action.
- **Decisions:** explicit requirements and their origin, accepted choices, proposals, assumptions, supersession and unresolved contradictions.
- **Work:** actionable tasks with completion evidence, separating work finished from conclusions still uncertain.
- **Sources and knowledge:** material findings with date, version/locator, actual coverage and a clear distinction between source content and analysis.
- **Maintenance:** how new material changes these records, how to verify them and how another task resumes.

Use actual project facts. Where needed evidence is unavailable, record the gap and its consequence instead of inventing substance. A user's desired feature is not implemented functionality; a proposal is not approval; a source's claim is not a verified result. Keep domain-specific distinctions when relevant rather than flattening them into a generic done flag.

Make the root instructions discoverable in the intended environment, typically AGENTS.md for Codex. Merge with existing instructions; preserve governing constraints. A CLAUDE.md or other bridge should point to the same maintained record when that client is in scope. Files provide context, not automatic transcript sharing, concurrent locks, remote synchronization or future execution.

## Integrate changes and preserve history

Read [updates and validation](references/updates.md) for reconciliation, interruption and review. At minimum:

1. Identify the arrival/version, authorized scope and actual reviewed portion. Preserve originals and useful source locators; use hashes when byte identity matters.
2. Determine which requirements, claims, tasks or outputs change. Check contradictory evidence and distinguish a changed fact from newly reviewed old information.
3. Update the authoritative record and each affected current view. Preserve the old conclusion, effective date and why it changed; mark remaining dependents stale rather than silently overwriting history.
4. Record actual validation, unresolved processing and the next action in a dated handoff; refresh current navigation when integration is ready. An interruption gets a partial handoff with a precise resume point.

For substantial parallel work, give workers bounded inputs and separate outputs, with one integrator for canonical files. Use the available agents/model preferences; a persistent queue is not a scheduler. No unrequested watcher or background process is implied.

## Check structure and usefulness

For repeatable structural checks, map existing files in brain.json using the small schema in [structure and records](references/structure.md), then run:

```sh
python3 /path/to/create-project-second-brain/scripts/audit_brain.py /path/to/project
```

Substitute actual paths. The helper requires Python 3.9 or newer with the standard library only and is read-only. It checks declared files, inline local link targets and optional preserved-source hashes. It does not read the corpus, validate heading anchors or remote websites, test an app, or prove substantive completeness. The manifest maps roles to existing records; it must not become a competing store of project decisions.

If the project needs to remain usable without the installed skill, include the helper and its contract locally, or the small complete method when useful. Do not require a copy of a large toolkit for a simple context update. Keep the actual maintenance command in the project.

For a substantial build/restructure, give an independent reader the completed entrypoint and authorized raw inputs, without briefing them on the intended answer. Check that they can explain the purpose, retrieve supporting and contrary evidence, distinguish requirements from suggestions, state what works and resume the next action. An actual small update is stronger evidence than a file-count check. Repair demonstrated defects; avoid ceremonial repeat reviews.

Close with the start point, useful changes, checked scope, material gaps and exact next action. If requested, save local version history or package the result; verify the actual output. Keep reusable skill instructions and synthetic fixtures free of project/client content. Installed files, successful structural validation and demonstrated client discovery are separate states.
