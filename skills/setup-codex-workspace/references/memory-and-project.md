# Project knowledge, memory and task ownership

Map these responsibilities to existing files/services before creating new ones:

| Layer | Authority and use |
| --- | --- |
| Source systems and preserved originals | Original evidence, object identity, versions and transmission context |
| Project second brain | Current supported knowledge, decisions, corrections, coverage and handoffs |
| Human task system | The user's chosen task board/calendar; link IDs instead of maintaining competing status copies |
| Global/native assistant memory | Explicitly requested stable preferences and pointers; optional, governed by the environment's write policy |
| Runtime state | Checkpoints, cursors, deduplication keys, leases and run receipts; separate from reviewed knowledge |
| Shared toolkit skills | Generic method only; no creator/user private data in toolkit releases |
| User's personal skills and profiles | Private workspace/repository context and instructions, with source scope and access controls |

Do not create another `TASKS.md` with independently editable task status when the user already uses an external authoritative board. A local index can link task IDs and record last verified sync time. If the service is unavailable, mark cached status stale and retain an explicit unsynced queue.

## Minimal project setup

The user's private repository may contain their real documents, correspondence-derived knowledge, profiles and personal skills when authorized. The toolkit's generic-distribution rule does not prohibit this. Keep the method copy and the user's private state mapped separately so a toolkit export cannot sweep in their data. Never populate the toolkit with its creator's history as starter content.

Reuse the builder's entrypoint, status, decisions, sources and maintenance records. For a new small project, these can be a few combined documents; no fixed folder tree is required. Add operations notes containing verified account boundaries, connection checks, routine definitions and recovery instructions. Keep technical run state in a clearly identified private runtime directory.

Merge a short startup contract into root `AGENTS.md`:

- Read the named entrypoint, current status, applicable decisions/corrections and task-specific source records before action.
- Resolve the project/account boundary and source of authority for each intended write.
- Route domain work to the selected second-brain method and existing canonical paths.
- Close work by updating actual results, affected records, unresolved scope and the next action.

Use real paths and decisions. Preserve existing instructions and inspect applicable overrides. A bridge for another client should point to the same records only when that client is in scope. Files do not grant filesystem permissions, automatically share conversations or synchronize concurrent work.

## Memory setup

Explain the distinction in everyday language: project files hold the work; optional assistant memory helps find the project and remember stable preferences. Confirm what the running product actually exposes. Do not invent a memory toggle, write internal memory databases or bypass a controlled memory-update mechanism.

For a requested memory entry, retain its scope, origin/date and correction/supersession rule. Project-specific names, facts and sensitive records remain local to the project unless the user specifically authorizes a wider store. Do not import another project's knowledge to fill gaps. Global memory additions require an explicit user request and compliance with the environment's memory rules, even during broad workspace setup.

Test persistence by resolving an actual project decision and its source from the entrypoint. A clean task is useful only when the user requests one; otherwise test from the files and label fresh-task loading unverified. Never claim native memory recall from merely reading the file yourself.

## Maintenance and recovery

New material goes through the builder's intake/update process: preserve, identify the changed version, read the necessary scope, reconcile, propagate corrections and verify. Preserve older conclusions and their dates. Do not convert an unread arrival into a learned fact.

Check existing backup/version-history arrangements. Establish an authorized recovery method if missing; local Git alone is not an off-device backup. Keep secrets and received originals out of unintended commits or exports. Do not create remote storage as an implicit part of setup. For a restoration test, restore a small authorized record into a temporary separate location and compare it; never overwrite current work to test recovery.
