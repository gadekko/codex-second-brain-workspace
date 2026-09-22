---
name: setup-codex-workspace
description: Guide first-time Codex workspace setup, connect tools, learn writing style and routines from authorized email/calendar history, map work and life workflows, create personalized skills, and build a durable second brain with verified recurring work.
---

# Set up a Codex workspace

Turn the user's actual work into a resumable, connected workspace. Guide the user through choices and sign-in steps, carry out authorized setup, and demonstrate that the result works. A folder, installed plugin, saved memory note or scheduled prompt is only one part of that outcome.

The endpoint is an operating work environment, not only document organization: map the person's responsibilities and available tools, recover relevant context from their history, perform authorized workflows end to end, and improve maintained knowledge and skills after real work. A user's own private repository is a valid home for their real project files, mail-derived context, profiles and skills. The generic-data restriction applies to this shared toolkit and its releases, not to that private working environment. Never seed the toolkit with its creator's private history.

This is a companion to `create-project-second-brain`, `create-dispute-second-brain` and `create-investment-second-brain`. It owns workspace onboarding and operational wiring. One selected builder owns the project's knowledge structure and source integration. Keep one coordinator and one authoritative home for each record.

In the standalone bundle, the complete [general builder](../create-project-second-brain/SKILL.md) is included. Read it directly when it is not installed in the skill catalog. For this bundle's default request to set up a workspace from all local project files, use its [full local-corpus workflow](../create-project-second-brain/references/local-corpus.md): preserve originals, create faithful Markdown clones, read the corpus and build linked topic clusters and retrieval indexes. Domain-specific dispute/investment skills are optional and are not included or required for this general workflow. Respect a narrower endpoint if the user requests one.

## Start with the requested endpoint

Distinguish creating this reusable skill, giving advice, auditing an existing setup and actually setting up a user's workspace. A request for instructions or a skill does not authorize connecting accounts or starting schedules. During an authorized setup, complete reversible in-scope work without asking repeatedly. Authentication, unresolved account/destination choices and actions outside existing authority are genuine handoffs to the user.

Assume a first-time user has not connected email, calendar, files or other services and may not have a local project folder. Do not assume technical vocabulary or familiarity with Codex. Explain the current step, offer a sensible default and walk through one action at a time. Reuse answers already given in this setup. Present a small progress list: purpose and folder, connections, learn how you work, review your workflow map, create your skills, second brain and memory, try the skills, recurring work. Skipped and blocked steps retain those labels. If the user tries a workflow halfway through setup, help them and return to the saved setup checkpoint.

Read [connection checks](references/connections.md) when selecting or connecting services, [memory and project records](references/memory-and-project.md) when establishing the project, and [automation and acceptance](references/automation-and-acceptance.md) before recurring execution. Read [current product sources](references/product-sources.md) when resolving Codex capability or UI questions; discover current tools and use official documentation instead of assuming old menu labels or APIs still exist.

After connections, read [learning writing style, cadence and workflows](references/work-pattern-discovery.md) and [creating personalized skills](references/personalized-skills.md) in full. These are part of normal complete onboarding, not optional suggestions left for the user to implement. The user can limit or skip any data source or phase; record the resulting limitation and offer an interview or supplied-example route.

Before handoff, read and implement [continuous learning and skill updates](references/continuous-learning.md): establish the working environment's startup/closing contract, correction ledger, skill revision records and verified refresh routines. Learning must persist in usable records and tested skills rather than remain in a conversation.

## 1. Establish the work and current setup

For a new setup, begin by asking these two questions together, unless the person has already answered them explicitly:

1. “What will this second brain be for? Tell me about the project and what you would like AI to help you do.” Offer brief examples if useful: running a business project, organizing research, managing a case, or keeping personal work in order.
2. “Have you already created a folder on your computer for this project?” Offer “Yes”, “No—help me create one”, and “I’m not sure”. If yes, help them select or identify the folder; do not require them to know how to type an absolute path.

Wait for these answers before choosing a project, ingesting sources or configuring accounts. A generated working directory, remembered project name or installed connector is not an answer. If they have no folder, propose a clear name and ordinary local location based on their answer, settle the destination and create it when permitted, or guide them through creating it. If unsure, help them inspect likely locations without scanning unrelated project contents. Explain that this folder will hold the project's files and maintained knowledge; the downloaded skill bundle is a separate set of instructions.

Reflect the project purpose back in one short sentence and identify a first useful outcome. Ask next where its information currently lives and which tools they use: for example Gmail or Outlook, Google or Microsoft Calendar, local documents or a cloud drive, and a task app if they have one. Give familiar choices plus “Neither” or “Not sure”; do not make the user name connectors, MCP servers or APIs. Do not ask about every product or future automation setting at once.

Once the folder and purpose are known, inspect available project listings, that folder's governing instructions and entrypoint, relevant installed skills/tools, and existing automation metadata. Inspect only relevant configuration fields; never dump authentication files or secrets. Do not search unrelated accounts or private projects to invent a profile. Establish the source boundary and human task destination now; resolve autonomous actions, cadence/timezone and notification choices later when proposing the actual routine.

Do not make a nontechnical user choose a database, vector store or orchestration framework. Begin with their familiar tools and portable project files. Preserve the chosen model and reasoning depth; do not switch models or create paid dependencies by inference.

Create a compact setup record in the authorized project, or an authorized staging folder if the project is not yet selected. Record choices, verified capabilities, missing dependencies and the exact resume action. Reuse an existing record rather than starting a competing setup ledger.

## 2. Establish the Codex project

Resolve the selected project and real filesystem path. Reuse a matching saved project. Otherwise prepare the authorized folder and add it through a supported project-management capability or the observed app UI. If user interaction is necessary, give exact current steps and resume verification after they finish. Creating a directory does not prove the app registered a project. Do not edit Codex's internal database to simulate registration.

Verify the saved project points to the intended folder and that the task uses it. A projectless task, a ChatGPT cloud project, a local Codex project and a Git worktree have different storage/access boundaries. Do not promise that cloud work can read local files. Create a separate task only when the user requests one; do not manufacture a task as a registration test.

Use existing Git/versioning conventions. A knowledge workspace does not require a new remote repository. Where recovery is needed, use the authorized local version-history or backup method; do not upload private files to GitHub or a cloud drive without authority. Isolated code worktrees must return reviewed changes to the canonical knowledge workspace; they are not a second current brain.

## 3. Connect the services needed for the work

Translate workflows into capabilities: source search and full reads; attachments/native files; calendar; task management; communication; and optional domain systems. Cover every selected dependency, without installing every available connector.

Explain in plain language which of their tools this project needs and why. Present a short personalized connection checklist, then guide the person through the first needed service. Do not hand over a list of settings and proceed as though they completed it. Follow the [guided connection loop](references/connections.md#guided-connection-loop-for-a-first-time-user) for every selected service, including mail and calendar as separate checks even when the same account is used. A local-only project may need no external connections; explain that and continue without forcing sign-ups.

Finish this guided onboarding before the full corpus build: each needed service must be tested, explicitly skipped/deferred by the user, or recorded as blocked with an agreed alternative. If a required connection is blocked, explain what cannot work and ask whether to continue with the available local material or resolve access first. Continue independent preparation without silently treating the incomplete setup as finished. Reuse verified existing connections if discovered; help the person confirm they are the intended account instead of making them reconnect unnecessarily.

Prefer existing connectors and supported APIs. Use installed plugin skills when their workflow applies. Discover relevant tools first; distinguish installed, authenticated, account verified and capability tested. Use current installation/connection UI only where the available tools permit it. Honor installation tools' invocation constraints; a marketplace recommendation is not proof that a plugin was installed. For missing services, give a supported setup path or an explicit fallback.

Complete one useful read test for each required capability in the correct account, within the authorized scope. Verify attachment retrieval separately if the workflow needs it. A safe scoped read may be enough; write access needs a separate test only when writes are required and authorized. Avoid sending test messages to people. Record failures and coverage accurately. Continue independent setup while the user completes OAuth or administrator steps.

## 4. Learn the person's writing, routines and workflows

Once the selected connections work, explain that you can learn from their own sent messages, relevant received threads and calendar history to make useful skills. Settle which accounts, life/work areas, date range and exclusions they want included before reading history. Offer a bounded starting window, such as the last 30 days, with a choice to broaden, narrow, use supplied examples or skip. Reuse explicit scope already given; installed connections alone do not authorize a whole-life scan.

Follow [work-pattern discovery](references/work-pattern-discovery.md). Read full selected threads and calendar records, not just snippets. Learn writing style from text the user authored, grouped by language, audience and channel. Map repeated triggers, follow-ups, meeting preparation, project updates and other observed workflows across the areas they selected. Capture cadence with counts, dates, exceptions and coverage. Calendar invitations do not prove attendance; observed timing does not establish the user's preferred schedule.

Present a short, source-grounded profile and workflow map for correction. Separate observed patterns, tentative inferences, confirmed preferences and proposed improvements. Ask whether the voice sounds like them, which patterns should become routines, and which areas should stay separate. Prepare draft skills while awaiting feedback, but do not promote an inferred habit to an approved preference or activate a schedule based on it.

## 5. Create and set up personalized skills

Follow [personalized-skill creation](references/personalized-skills.md) to produce actual skill files, not merely recommendations. Reuse existing suitable skills and profiles before creating new ones. Create a writing-voice skill when supported by reviewed samples, and one skill per selected distinct workflow, such as inbox triage, meeting preparation, follow-up drafting or a weekly review. The person's actual needs determine the set; no fixed job, service or writing style is assumed.

Store their evidence, profiles, workflow map and generated skills in the chosen private workspace, outside this reusable method repository. Use the current supported skill installation mechanism to make accepted skills discoverable, or provide working direct-file invocation if registration is unavailable. Help the person through setup and verify the installed files and available discovery state. Do not stop after leaving empty templates or asking a novice to perform the implementation themselves.

## 6. Build durable knowledge and memory

Use the selected builder's live instructions and preserve its records:

| Need | Owner |
| --- | --- |
| General business, research, software or personal project | `create-project-second-brain` |
| Dispute dossier with evidence, claims and procedure | `create-dispute-second-brain` |
| Investment firm knowledge, decisions and outcomes | `create-investment-second-brain` |
| Bounded dispute arrival only | `case-corpus-intake`, returning once to the dossier's integrator when integration is authorized |

Read the selected skill and its applicable references before executing it. Do not clone domain methods into this skill. If a builder is unavailable, locate an existing project method or finish the operational setup and name the missing dependency; do not label a scaffold a completed domain brain.

Map project knowledge, human task state, assistant memory and technical runtime state to distinct responsibilities. Merge a concise startup route and end-of-task maintenance instructions into the existing `AGENTS.md`. Preserve originals, dated decisions, corrections, source links and pending review coverage. If the user requests a full build, finish its authorized corpus scope; a small pilot never substitutes for that build.

Global/native memory is optional and product-dependent. Check its actual controls and write policy. Save cross-project preferences or a thin project pointer only when explicitly requested and permitted, using the supported mechanism. Keep sensitive project facts in their project. A file named `MEMORY.md` is not proof of automatic recall, and memory settings do not prove every source was read.

## 7. Demonstrate the personalized skills and a complete workflow

Test each generated skill on a representative permitted example. For writing style, draft for a real audience without sending, then let the person correct the voice. For calendar/routine skills, verify timezone, cancellations and exceptions. For workflow skills, demonstrate the intended output, duplicate handling and one missing-data or unavailable-tool case. Save actual results and incorporate corrections in the private profile and skill. Separate file validation from demonstrated behavior and user acceptance.

Use a small real authorized source or a clearly labeled synthetic fixture. Retrieve it, preserve the required source locator/version, process it with the selected method, update the correct project record, and produce the intended output. If the workflow includes authorized task-system writes, reconcile them with existing task IDs and read back the result. If external action is not authorized, stop at the concrete draft and label that boundary.

Run the same input again to check for duplicates, then process a correction or changed version to check supersession. Verify the record and next action can be recovered through the project's entrypoint without relying on this chat. Respect the user's actual requested scope while testing.

## 8. Enable requested recurring work

Configure schedules only when recurring work is requested. If the user wants automation but has not selected a routine, propose a concrete first routine and settle its material scope/cadence before activation. Do not end a setup request at a vague recommendation when an authorized routine can be configured.

Inspect existing schedules to avoid duplicates. Use the supported scheduler tool/UI and its current schema. In the Codex app, prefer an in-task heartbeat for ongoing follow-ups unless the user asks for independent scheduled runs. Follow the live tool contract for project selection, model, execution environment and notification controls. Preserve the user's chosen model and reasoning depth.

Use the run contract and recovery procedure in [automation and acceptance](references/automation-and-acceptance.md). Test the prompt manually, save the schedule, read back its actual settings, and distinguish that from a successful scheduled run. When local execution depends on an available computer/app, explain the verified host requirements. Never promise always-on service from a saved prompt or a dormant laptop.

## 9. Establish ongoing operation and improvement

Implement the [continuous-learning method](references/continuous-learning.md) in the user's private environment. Map current knowledge, project namespaces, workflow/tool capabilities and action authority. Make daily tasks retrieve the relevant sources, do the authorized work, verify final state, update affected knowledge, capture corrections and improve skills under the agreed maintenance rules. Execute supported actions within existing authority; do not permanently limit every workflow to drafts when the user has authorized execution.

Test one correction through the full path: evidence or user feedback → dated correction → affected knowledge/profile → skill revision where appropriate → replay of the failed example and a prior successful example → durable next-run instructions. Retain older versions and a rollback route. Enable requested source-refresh and review schedules using the real scheduler; do not claim passive background learning from the presence of these files.

## 10. Handoff with demonstrated status

Finish at the requested endpoint, with the project entrypoint, tested connections, authoritative records, demonstrated workflow and schedule status. Name only concrete outstanding user actions, such as signing into a specific account or enabling a blocked administrator permission. Provide the resume instruction for each.

Use precise states: prepared, connected, read-tested, write-tested, manually demonstrated, scheduled, scheduled-run verified. Keep full-corpus coverage separate from operational readiness. A capability that could not be tested stays unverified. Include how to add new sources, change a preference, run the workflow, inspect results and pause recurring work.

Include the private profile and workflow-map entrypoints, history actually reviewed, unresolved inferences, created/updated skill names with invocation instructions, each skill's tested/discovery/acceptance state, and agreed routines. The reusable package must remain generic: never copy the person's profile, sent messages, calendar, account identifiers or generated personal skills back into it.
