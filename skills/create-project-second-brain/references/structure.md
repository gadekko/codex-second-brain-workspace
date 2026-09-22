# Structure and record contract

## Start with the existing project

Keep coherent filenames and directories. Map their roles instead of cloning them under a new second-brain folder. A tiny project may use one overview, one working-state document and source links. A larger project may separate context, knowledge, sources, decisions, tasks and handoffs. Never create empty people, chronology, financial or legal modules merely because another project's builder had them.

A useful new-project arrangement is root entry instructions and README, a few current control documents, docs/ for knowledge/sources/handoffs, and an inbox only if arrivals need a visible place. Existing original files can remain where they arrived. Preserve provenance if actual moves are authorized; a folder tree is not itself knowledge.

Root instructions should explain a short startup order and an end-of-task update obligation. They should route to detail rather than include every source or impose unrelated rules. A folder map explains each location's purpose, what is canonical, and where not to put private material.

## Minimal records

Use Markdown prose or tables; these are responsibilities, not mandatory filenames or fixed taxonomies.

| Record | Useful fields |
| --- | --- |
| Scope | Purpose, user/owner if known, actual source boundary, exclusions, cutoff, requested depth |
| Current state | Dated observation, evidence locator, work completed, untested scope, blockers, next action |
| Decision/requirement | Stable ID when useful, text, status, origin/date, rationale, supersedes, affected records |
| Source/findings | Source ID or URL/path, version/date, section/page/range, content claim versus inference, coverage, limitations |
| Task | Action, dependency, owner if known, status, completion evidence |
| Handoff | Scope, result, changed records, validation, unresolved work, external changes, exact resume action |

Distinguish user choices from defaults selected to move reversible work forward. An accurate unresolved record may be complete; processing an unread source is still unfinished. Record important relationships in links and rationale instead of adding a graph database before it solves a retrieval problem.

## Optional source-heavy intake

For an explicitly exhaustive corpus build, account for all agreed sources and failures, including relevant container members and attachments. Use stable source-version identities and separate occurrence/transmission context. Matching bytes can reuse the identical reviewed content scope; a changed context may need separate review.

Preserve originals and use appropriate tools for native extraction, OCR, sheets, visuals and media. Extraction is not reading. Faithful full clones or source-indexed shards are useful when the request requires complete readable coverage; a short summary cannot stand in for them. No need to clone every source-code file during a normal software-project context setup.

Track preserved, extracted, read and reconciled scopes independently. Where claims require stronger verification, record that separately. A source with an unread attachment remains partially covered. Keep errors, unresolved formats, snapshot changes and pending work visible. Use a durable queue for large jobs, with an actual resume cursor rather than a promise of background work.

For ordinary projects, use a concise source register and expand only when volume or evidence requirements justify it. Keep secret stores, private documents, generated outputs, method files and test fixtures out of unintended intake; exclusions describe scope, not proof of security.

## brain.json contract

The optional auditor reads one UTF-8 JSON file at the project root by default. Set schema_version to 1. documents maps each required responsibility to an existing Markdown file; roles may intentionally share one file. Supporting documents are additional maintained Markdown files to check. All paths must be relative and resolve within the project.

```json
{
  "schema_version": 1,
  "documents": {
    "entrypoint": "AGENTS.md",
    "scope": "PROJECT.md",
    "status": "STATUS.md",
    "decisions": "DECISIONS.md",
    "tasks": "TASKS.md",
    "sources": "SOURCES.md",
    "maintenance": "MAINTENANCE.md"
  },
  "supporting_documents": ["README.md"],
  "preserved_sources": []
}
```

This example is a shape, not a request to create those filenames in an existing project. Fill it with the real canonical paths. An empty preserved_sources list means no byte-preservation claims, not that all sources were reviewed.

When original-byte identity matters, each preserved_sources entry has a unique id, relative path and exact SHA-256 hex digest. Preserve the source first, then compute its digest. Record origin, review coverage and exclusions in the source register; a hash alone cannot supply them. Never bless changed bytes by replacing an old digest without investigating the change and preserving its provenance.

The auditor checks only declared documents/sources and their inline local file links. It does not recursively ingest all files, inspect source instructions, follow remote links, validate heading fragments or read imported documents substantively. A pass cannot certify completeness, truth or safe sharing. Keep historical source links outside active-document checks when the archive deliberately preserves earlier wording; hash those originals instead.
