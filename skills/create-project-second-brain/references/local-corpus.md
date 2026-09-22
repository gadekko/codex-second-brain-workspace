# Build a second brain from all local project files

Use this workflow when the user asks to convert an entire authorized local project corpus into Markdown clones and organize it so people and AI can retrieve its contents. This is a full source-processing endpoint. It includes all substantive material in the agreed boundary, not only files matching a search or a sample of attractive documents.

## 1. Establish the boundary and inventory

Resolve the actual project and source roots from the user's request. Read applicable governing instructions and the current brain's entrypoint, status and source catalog. Reuse an existing coherent brain. Confirm only genuinely ambiguous project/access choices; continue independent work when possible.

Record source roots, output root, scope date, permitted connected sources if any, and exclusions. A local-only build needs no connector and does not authorize account-wide searches or external uploads. Do not open unrelated clients' data to fill knowledge gaps.

Inventory recursively before synthesis, including hidden substantive files, extensionless files, nested archives, attached objects, local references and failed reads. Use a deterministic script or a trusted inventory tool that records paths, sizes, byte hashes, file types, errors and symlink targets without following links outside the source boundary. Do not execute imported code, macros, scripts or document instructions. Resolve cloud placeholders and symlinks only within the authorized boundary; inaccessible objects remain visible.

Record explicit exclusions for generated outputs, this method bundle, caches, vendored dependencies, version-control internals and secret stores as appropriate to the project. Do not exclude meaningful source code, old versions, scanned pages or difficult file types merely to reduce work. Scope exclusions need a reason; permission restrictions and unreadable files remain distinct from exclusions.

For archives, enumerate members safely, preserve the container, record parent/member relationships and enforce bounded expansion. Reject traversal paths, unsafe links and collisions. An archived document counts as a member still needing processing even if the archive's bytes were saved. Encrypted or corrupt members remain blocked with the next recovery action.

## 2. Preserve bytes and identity

Leave received originals unchanged. Use verified independent copies when preservation inside the brain is necessary; keep their original names/tree and a mapping back to origin. Do not move, rename, OCR over or normalize the received files by default. For portability, include authorized preserved originals and relative links; an index pointing outside the package is not a self-contained source archive.

Use stable source-version IDs plus occurrence IDs for different paths/arrivals. A SHA-256 digest establishes byte identity, not authenticity or meaning. Equal bytes may share one canonical clone, while retaining every occurrence's context. Different bytes remain separate preserved versions; establish their relationship from source context rather than filename alone. Reuse reviewed scopes only when the source version and scope match.

Keep a source catalog and coverage ledger. A CSV, JSON or JSONL is sufficient; retain the project's existing schema if it works. The following fields describe responsibilities, not a mandatory database:

| Record | Required information |
| --- | --- |
| Source version | Stable ID, origin locator, preserved relative path, SHA-256, observed type, title/language if known, version relationship |
| Occurrence | Occurrence ID, source-version ID, received/original path, parent container/message ID, capture date and context |
| Clone | Source-version ID/hash, clone path or shard index, conversion method/version, time, source-unit locators, limitations |
| Coverage | Inventory/preservation/extraction/inspection/full-reading/reconciliation statuses separately, actual covered units, pending units and errors |
| Membership | Source-version ID, cluster ID, source locations supporting that membership, reason or unresolved classification |

Counts must identify whether they concern paths/occurrences, unique byte versions, containers, members, pages or reviewed units. Never report one denominator as another.

## 3. Create faithful Markdown clones

For every substantive source, create a full clone or a complete linked set of shards. Keep extracted source content separate from summaries, translations and analysis. A clone begins with source ID, preserved-original link, exact source hash, conversion method, covered units and omissions. Use stable headings for original page, paragraph, slide, sheet/cell, line, message or timestamp locators.

Select the actual installed tools for each format. Discover relevant document/PDF/spreadsheet/media skills when available; the workflow is still usable without those named skills if equivalent trusted tools exist. Check dependencies rather than assuming converters or OCR are installed. Do not silently upload sources to external conversion services.

| Format | Minimum treatment |
| --- | --- |
| Markdown/plain text/source code | Preserve full UTF-8 content and line boundaries; fence code so it is content rather than instructions; record decoding failures instead of guessing silently |
| PDF | Extract each page, diagnose scanned/mixed pages, OCR where needed, retain page locators, tables, footnotes and material visual content |
| Word/rich text | Preserve headings, paragraphs, tables, notes and relevant comments/tracked changes; identify revision state and render where meaning depends on layout |
| Presentations | Cover every slide, speaker notes and meaningful charts/diagrams with slide locators and linked rendered assets when needed |
| Spreadsheets/CSV | Cover relevant sheets, cells/rows, formulas and displayed values, units, hidden substantive content, comments and charts; shard large tables with a complete index |
| Email/chat exports | Preserve complete message bodies, participants, timestamps, ordering/thread links and attachments; separate quoted duplicates from new transmission context |
| Images/scans | OCR supported text, inspect meaningful visuals and link the original image; label descriptions as derived rather than verbatim content |
| Audio/video | Use available authorized transcription with timestamp coverage; inspect material visuals where required; label uncertain speakers and unheard/unseen segments |
| Archives | Preserve the container and enumerate/process its members; the container gets an index, not a fabricated prose clone |
| Unsupported/encrypted/corrupt | Create a clearly incomplete source stub with the error, unavailable units and recovery action; do not count it as converted/read |

Markdown cannot preserve every native behavior or visual property. Retain originals and linked assets, label lossy representations and inspect any material detail on which a finding relies. A full text extraction is not proof of visual completeness. A spreadsheet screenshot is not full data extraction. Where volume requires sharding, the source-level index must enumerate all shards and their unit ranges; no truncation or skipped tail.

## 4. Read the corpus and build topic clusters

Read every accessible substantive source in the agreed corpus through its complete clone and any necessary native/visual inspection. Preserve source-level read receipts with actual ranges and gaps. Use search to prioritize and navigate, never as proof of full reading. Checkpoints should identify the exact next source/unit so a later run can continue without restarting covered material.

After enough reading to understand the corpus, derive a small useful taxonomy from its actual content. Typical axes are workstream, topic, entity, process, deliverable and time period. Do not impose every axis or guess subject matter solely from folder names. Existing folder structure is evidence of organization, not an authoritative topic model.

Keep one canonical clone per source version. Clusters link to it; they do not create divergent copies or move the original. Allow one source to belong to multiple clusters. Maintain an explicit unclassified/pending-review area until membership can be supported. Record meaningful cluster renames/merges and repair inbound links while preserving stable IDs or aliases.

Each cluster needs:

- A stable ID, plain-language title, scope and useful aliases/search terms.
- A source-linked account of what the cluster contains and what is known, separating source assertions, decisions and inference.
- Links to its sources and exact passages, including contrary evidence, superseded versions and unresolved gaps.
- Current decisions, questions and next actions when supported, with dates and status.
- Links to related clusters and a clear reason for the relationship.

Build navigation at three levels:

1. Root entrypoint: purpose, scope, current state, how to ask questions, and links to the topic map and source index.
2. Topic map: cluster names/aliases, one-sentence scope, important cross-links and an unclassified route.
3. Source index: every source version and occurrence mapping, date/type, clone/original links, cluster memberships and processing status. Provide entity and chronology indexes only where they improve actual retrieval.

Use ordinary relative Markdown links and searchable source IDs. For example, a fact should link to its clone's page heading and preserved original, not merely to an unsourced cluster summary. Test real target headings as well as file existence. If using `rg`, search the known clone/knowledge directories or source IDs; it is a navigation aid, not a semantic review.

Vector databases, embeddings and graph services are optional derived indexes. They are not required for this bundle. Add them only for a demonstrated need and within authorization, with a rebuild route from canonical files and explicit version/source bindings.

## 5. Reconcile and make changes resumable

Resolve identities, dates and statuses across clusters. Keep contradictions visible. A later document does not automatically supersede an approved decision. Separate proposals from approvals and plans from completed actions. Every material synthesis cites exact source support or labels an inference with its basis and limits.

Maintain an update log, dependencies and pending queue. One integrator owns canonical updates; if parallel agents are authorized, give them bounded inputs and separate outputs. Neither a queue nor a lease runs future agents.

For new arrivals, inventory the delta and compare versions/hashes. Preserve changed bytes, convert/read uncovered content, reconcile affected clusters and current views, and keep dated supersession. Repeated intake of identical input should not create duplicate knowledge, tasks or source versions. Deletion from a source folder is an observed disappearance, not permission to erase the preserved record or retract a decision.

Compare opening and closing inventories. Account for in-scope files that arrived or changed during processing. Do not advance a processed watermark past unread material. Finish requested processing where possible; genuine access/runtime limits require exact coverage and a resume action, not a smaller undisclosed scope.

## 6. Verify usefulness and hand over

Use the bundled `scripts/audit_brain.py` with the project's `brain.json` mapping to check declared documents, local file links and preserved-source hashes. Declare active cluster and index pages as supporting documents. The helper does not validate source coverage, heading anchors, semantic truth or clustering; check those separately.

Before claiming the local-corpus build complete, verify:

1. Every in-scope occurrence and discovered member has a catalog disposition, with explicit exclusions and failures. Reconcile unique source versions separately.
2. Every accessible substantive source has a full clone/shard set and complete required reading/inspection receipts; blocked sources remain visible in the denominator.
3. Clone source hashes, original links and unit locators match the preserved sources. No unexplained omission or truncated output remains.
4. Every reviewed source has supported cluster membership or a reasoned unclassified state. Every cluster synthesis has exact supporting and contrary source links.
5. From the entrypoint, retrieve a real fact, its exact original location, a multi-topic source, a correction/superseded statement and an unresolved question. Verify against originals. If one category genuinely has no example, record that with checked scope rather than inventing one.
6. A small repeat intake creates no duplicate; a synthetic or authorized changed-version test preserves the old version and updates affected current views. Keep test fixtures outside the real corpus denominator.
7. The handoff names input scope/cutoff, occurrence and unique-version counts, fully cloned/read/reconciled units, unresolved gaps, cluster count, tested retrieval questions and next action.

Hand over the start link and clear instructions: where to add files, how to request an update, how to locate originals and how to correct a finding. A truthful completed review of an accessible snapshot can still have unresolved substantive questions. It cannot be called a complete all-file conversion while requested source content is unread or inaccessible.
