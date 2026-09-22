# Optional Jev decision connection

This integration uses TypeSafe's official hosted API for bounded workflow selection and source-relevance recommendations. It leaves the person's chosen Codex model and reasoning depth unchanged. It is optional: setup and daily work continue through the existing method when Jev is unavailable, disabled or uncertain. The included adapter is a callable Python CLI, not a native Codex model setting or a claimed installed MCP connector.

## Connect with the person

1. Explain the concrete use: small routing/relevance questions may avoid repeated large-model decisions. TypeSafe receives the selected request text, candidate descriptions or excerpts. Settle the permitted projects/data and API spend before private requests; local files are not automatically local inference. Do not assume zero retention or general account access from a model name.
2. Guide the person to the official [TypeSafe console](https://console.typesafe.ai) for access and an API key. If early access is unavailable, mark this connection deferred and continue ordinary onboarding. Avoid similarly named third-party sites or gateways unless explicitly selected and independently verified.
3. Have the person put the key in their approved secret store, exposed as `TYPESAFE_API_KEY` to the execution process. Never ask them to paste it into chat, a command argument, a committed file or a screenshot. Verify presence without printing the value. A scheduler needs access in its own environment; interactive setup does not prove that.
4. Copy [the configuration](../../maintain-codex-workspace/examples/jev-config.json) into private runtime storage, outside this toolkit. Explain the defaults: disabled until selected, shadow mode, pinned model, confidence gates, one-hour cache, and rolling 24-hour call/cost-reservation limits. Set `enabled` to true only within the person's selected source/spend scope. Keep `mode` as `shadow` for calibration.
5. Copy [the synthetic request](../../maintain-codex-workspace/examples/jev-request.json) to that private directory. Run the command below without `--live` first, then with `--live` to test the real endpoint using synthetic data. Record the resolved model, usage and observed choice; a mock or dry run is not a connected account. Recover an expired key through the same console. No credential exists in the downloadable bundle.

```sh
python3 /path/to/bundle/skills/maintain-codex-workspace/scripts/jev_decide.py \
  --config /path/to/private-runtime/jev-config.json \
  --request /path/to/private-runtime/jev-request.json
```

Add `--live` only for an authorized API call. The helper also requires `enabled: true`; otherwise it performs no network request. It creates `jev-cache.sqlite3` beside the private config, storing hashed request identities, bounded answers and budget reservations, not source text or credentials. Exclude the entire private runtime directory from toolkit exports. Store any output receipt in that same private environment.

## Wire into actual work

Register the command, private config path, permitted data scope and tested state in the capability map. Merge a route into private project instructions and generated workflow skills: for an ambiguous choice among registered workflows, call the helper with `kind: workflow`; for a shortlist of retrieved passages, use `kind: relevance`. Skip the API when an explicit skill name, exact identifier, deterministic rule or existing validated record resolves the task. Never switch the user's main model to save tokens.

Each request contains `context` describing the task, a `candidates` map of stable IDs to descriptions/excerpts, and a `source_version` that changes with relevant source, preference or policy updates. Supply current time/timezone when semantically needed and disable caching or change the version for volatile state. Candidate IDs are local identifiers, not paths to execute. Resolve them through the authorized register. The helper accepts at most 24 candidates and 24,000 serialized request bytes; oversize requests fall back rather than silently truncate. These are local caps, not exact provider token limits.

For workflow selection, include accurate descriptions of the available skills. Jev can select one or abstain. Read the selected skill in full before executing the work. Multi-workflow tasks still require Codex planning; one recommendation never narrows the user's scope.

For relevance, first retrieve a bounded shortlist using local search or existing indexes. Provide enough source text to judge each candidate, with links/versions retained locally. Jev batches one relevance question per candidate into one request. Use results to prioritize reading, including contradictory evidence. Do not discard uncertain passages, skip mandated reading, claim exhaustive coverage, or use this prefilter to replace full-corpus ingestion. Reading an excerpt is not full source review. Jev recommendations cannot establish source truth, legal correctness, completed work or authorization.

Consume `recommendations` only in evaluated assist mode; `observed_answers` in shadow mode are comparison data. A fallback means continue through the existing Codex method with unchanged scope/model, not cancel the user's work. Even a confident `irrelevant` recommendation does not justify dropping a source required by the task. No adapter output performs an external action or grants permission to send, pay, publish, alter access or revise skills.

## Measure before assist mode

Start with representative labeled examples from the person's permitted scope: clear matches, no match, missing context, contradictions, misleading source instructions and relevant languages. Keep evaluation data private or independently synthetic. Compare the existing workflow and Jev on the same examples. Use a development set to choose thresholds, then a separate held-out set to assess them. Default 0.9 gates are uncalibrated starting values, not a promised accuracy level.

Record model/version, question revision, dataset/source versions, labels and errors. Measure accepted-decision precision, overall coverage/fallback rate, missed relevant or contradictory passages, latency and total workflow cost. Include Codex orchestration, fallback and review costs; inexpensive Jev calls alone do not establish overall savings. Avoid judging correctness merely by agreement with another model. Keep difficult or sparse cases with Codex or human review.

Only after the agreed quality and cost criteria pass, set `mode: assist` and record the real evaluation receipt as `evaluation_id`. This field is an audit pointer, not proof by itself; the setup agent must inspect the evidence. Recheck after model, criteria or source-distribution changes, and return to shadow mode on regressions. The helper validates the response model, labels, probabilities and usage and gates on both confidence and winning probability. Those numbers cannot guarantee correctness.

## Daily upkeep and costs

During maintenance, review Jev errors, cache behavior, abstentions, held-out quality and actual billing alongside total workflow costs. Do not make more calls to fill a schedule. Keep unchanged requests cached, batch independent questions sharing state, and precompute dates, arithmetic, hashes and duplicate keys in code. Never reduce required context or substitute a weaker writing/reasoning model to meet a token target.

The helper uses a conservative serialized-byte-plus-headroom cost reservation and a rolling 24-hour call limit in one private SQLite database. Reservations remain charged locally after failed calls to bound retry costs. They are not provider billing enforcement or a global account cap; configure provider spend limits when available. Independent config directories have independent limits. Simultaneous identical requests may both be billed. Set cache TTL to zero when freshness requires it. There are no automatic network retries, redirects or endpoint overrides.

## Official sources checked 2026-09-22

- [TypeSafe model card](https://docs.typesafe.ai/models): pinned model `jev-1.13.0`; listed input price $0.042 per million tokens and free outputs. Price can change; refresh the helper's rate before making financial claims.
- [API reference](https://docs.typesafe.ai/api): official endpoint `POST https://api.typesafe.ai/v1/systemone`; typed questions and response validation.
- [Confidence](https://docs.typesafe.ai/confidence): confidence is derived from the answer distribution, distinct from the winning option probability.
- [Known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13): avoid numeric/date computations, long irrelevant context and multi-hop reasoning; adversarial state can affect answers.
- [Coding-agent guidance](https://docs.typesafe.ai/introduction/coding-agents): Jev is an additional decision API, not a replacement model for Codex.

Local tests exercise adapter behavior with synthetic mocked responses. Live accuracy, language performance and net savings remain unverified until the user's own evaluation succeeds.
