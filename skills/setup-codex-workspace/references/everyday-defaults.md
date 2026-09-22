# Everyday defaults and routine setup

The person should be able to make a short request without repeating context-retrieval or writing instructions. Implement these defaults in their private project instructions and generated skills, using the scope and preferences agreed during onboarding. Keep automatic skill selection enabled; also write explicit routing in the project's existing AGENTS.md so discovery is not the only route. Resolve real paths before handoff and test in a fresh task when one is available; do not create a separate task without the person's request.

## Requests that carry context automatically

| Natural request | Default behavior to install |
| --- | --- |
| “Prepare me for tomorrow's meetings.” | Resolve tomorrow in the person's timezone. Read the selected live calendars, handle all relevant event instances and cancellations, and prepare each brief from relevant full mail threads, current project documents, prior meeting notes, decisions and open actions. Link evidence and state source gaps. |
| “Draft a reply.” | Resolve the selected message/thread from the current task or visible selection. Read the complete current thread, relevant earlier discussions and current commitments, then use the confirmed voice for this recipient, account, language and channel. Ask only when the target is genuinely ambiguous. Draft within authority; style does not authorize sending. |
| “What needs my attention?” | Refresh the scoped sources and reconcile deadlines, waiting items, changes, blockers and resolved work against native task/mail/calendar state. Report evidence, why each item matters and the next action. |
| “Next time, do it this way.” | Capture the scoped correction, update affected private records and skills under agreed maintenance authority, replay relevant examples and preserve a rollback version. Do not require the words “update the skill”. |

Do not interpret short wording as permission to search unrelated projects or accounts. Retrieve enough source detail to do the job and check volatile facts live. If prior conversations are unavailable, use maintained private decisions/notes and identify the gap instead of claiming complete recall. Missing voice evidence calls for a neutral draft and a focused calibration step. An inaccessible source stays an explicit limitation.

## Write the routing contract

Merge a concise rule into the person's existing project AGENTS.md with actual entrypoint, profile, skill-register and maintenance-skill locations:

> For ordinary work requests, load the relevant registered personal skill and current project context automatically. Meeting preparation includes live calendar details and relevant correspondence, documents, prior decisions and open actions. Reply drafting includes the full thread, relevant earlier context and the confirmed audience-specific voice. Do not require the user to restate these defaults. Apply current explicit instructions over defaults. Persist corrections and unfinished work in the authoritative private records at task close. Use the registered maintenance skill for source refresh, attention reconciliation and tested skill revisions under the agreed authority.

Use stable paths accessible from both interactive tasks and scheduled execution. A prompt or profile file alone does not establish that fresh tasks will load it. Record whether routing was behaviorally tested, only inspected, or blocked.

## Offer a concrete recurring setup

As part of complete onboarding, explain and offer these routines in plain language. Reuse choices already made; do not leave the person to configure them alone.

1. **Daily workspace maintenance:** recommend once every 24 hours, or a chosen daily local time, using [maintain-codex-workspace](../../maintain-codex-workspace/SKILL.md). Refresh changed authorized sources, reconcile attention items, review all registered private skills, and apply only justified tested revisions. Explain that a fixed daily local time differs from an exact 24-hour interval around daylight-saving changes.
2. **Attention checks:** agree a cadence and deadline horizon suited to the selected work. They can share the daily maintenance run when daily checks suffice. If the person needs faster checks, configure a separate compatible routine that references the same attention ledger and notification history, with no overlapping writers. Do not describe periodic polling as instant event delivery.
3. **Meeting preparation:** offer a chosen local-time run for the next day's meetings, or another supported trigger. Reuse the same meeting skill as an on-demand request and update briefs for changed/canceled events. Do not assume attendance or send invitations.

Settle source boundaries, local time/timezone or interval, permitted local updates, output location and notification intent. Recommend automatic reversible private knowledge/skill fixes backed by explicit corrections or demonstrated defects, with inferred preference/authority changes proposed for review. The user may accept, change or skip routines. Once selected, carry out setup using the supported scheduler rather than merely saving a suggested prompt.

Read [automation and acceptance](automation-and-acceptance.md) and discover the live automation tool first. Prefer the supported in-task heartbeat unless independent runs were requested; do not invent a cron workaround. Inspect existing automations for the same purpose before creating one. Configure actual notification settings separately from prompt prose when the tool supports them. Use the user's model/depth and verify host, account and filesystem availability in that execution context.

A daily maintenance prompt should name the real project and skill paths, agreed sources and authority, and ask for source refresh, attention reconciliation and evidence-based skill review with receipts, checkpoints and rollback. Keep it self-contained enough to resume without this onboarding conversation. Stay quiet while unchanged or non-actionable; notify for meaningful changes, failures or required action according to the selected preference.

Manually exercise the routine before activation, then read back its ID, schedule, active state, target and notification settings. Record first scheduler-triggered execution separately. Provide plain requests to run now, change cadence or pause. If a computer must be available, explain that dependency; a ZIP, local ledger or open task cannot run by itself.

## Verify the short-request experience

Try the exact short prompts above against a permitted example, without appending hidden source/style hints to the user's request. Verify actual retrieval, audience-appropriate voice, freshness and evidence. Check one unavailable-source case, a canceled meeting, a resolved attention item, duplicate run and correction replay where applicable. Test that a repeated unchanged run produces no duplicate action or unnecessary notification. Preserve results and remaining gaps; structural package checks do not demonstrate this behavior.
