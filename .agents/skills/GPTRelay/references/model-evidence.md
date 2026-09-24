# Model routing evidence (GPT-6), 24 September 2026

Scope: current `gpt-6-astra`, `gpt-6-sol`, `gpt-6-luna` only. This report distinguishes documentation, independent measurements, and routing proposals. Research worker was requested as Sol High; actual runtime model and effort were not surfaced to this worker, so execution setting is **inherited, not verified**.

## Documented facts

| Variant | OpenAI position | API reasoning effort | Context / input / output | Short-context Standard API USD per 1M input / cached input / output | Codex credits per 1M input / cached input / output |
| --- | --- | --- | --- | --- | --- |
| [Astra](https://developers.openai.com/api/docs/models/gpt-6-astra) | Most capable; complex reasoning, coding, computer use, research, documents | low, medium, high, xhigh, max | 1.05M / 922k / 128k | $10 / $1 / $50 | 250 / 25 / 1,250 |
| [Sol](https://developers.openai.com/api/docs/models/gpt-6-sol) | Complex coding and agentic workflows | none, low, medium (API default), high, xhigh, max | 1.05M / 922k / 128k | $2 / $0.20 / $10 | 50 / 5 / 250 |
| [Luna](https://developers.openai.com/api/docs/models/gpt-6-luna) | Efficient, focused, high-volume tasks | none, low, medium (API default), high, xhigh, max | 1.05M / 922k / 128k | $0.10 / $0.01 / $0.50 | 2.5 / 0.25 / 12.5 |

All three accept text and images and output text. Their model pages list Responses, Chat Completions, Batch, web/file search, code interpreter, hosted shell, apply_patch, computer use, MCP, skills, tool search, prompt caching. API model availability is separate from plan/client/workspace availability. [API model pages](https://developers.openai.com/api/docs/models); [Codex model availability](https://learn.chatgpt.com/docs/models).

API Standard short-context rates above come from [OpenAI API pricing](https://developers.openai.com/api/docs/pricing#text-tokens). More than 272k **input tokens** doubles input/cache charges and multiplies output price by 1.5 for the entire request, per model pages. API long-context input/output: Astra $20/$75; Sol $4/$15; Luna $0.20/$0.75. Codex rates come from [Codex pricing, Token rates](https://learn.chatgpt.com/docs/pricing#token-rates): separate credits, no cache-write charge, Fast mode 2.5x credits where available. API cache-write rate is 1.25x input. **Do not convert API dollars into Codex credits** or use API price as proof of Codex subscription usage; plan allowances and task token mix vary. At identical uncached input/output tokens, Sol is 20x Luna and Astra 5x Sol on both API and credit rates; actual task cost may differ due to reasoning, retries, cache and output length.

Official Codex guidance says [Sol Medium for everyday/complex coding, Luna High for focused repeatable tasks](https://learn.chatgpt.com/docs/whats-new#choose-gpt-6-sol-and-luna). [Codex subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents#reasoning-effort-model_reasoning_effort) proposes starting Sol Medium, Luna High, Astra Low for explicit settings, then adjusting by task. [GPT-6 model guide](https://developers.openai.com/api/docs/guides/latest-model) describes Astra as strongest for multistep work across browser, code, professional software; those are vendor claims, not measured Codex task outcomes. In an API integration, use Responses for reasoning with tools: Astra tool calling requires Responses, and Sol/Luna Chat Completions function calling requires `reasoning_effort: none`. These API constraints do not establish Codex client tool differences.

## Independent evidence (separate organizations, separate harnesses)

**Artificial Analysis, Intelligence Index v4.3.2.** Its [Luna High vs Sol Medium](https://artificialanalysis.ai/models/comparisons/gpt-6-luna-high-vs-gpt-6-sol-medium) and [Sol Medium vs Astra Medium](https://artificialanalysis.ai/models/comparisons/gpt-6-sol-medium-vs-gpt-6-astra-medium) pages compare candidate operating points. Luna High and Sol/Astra Medium use different effort settings; these figures do not isolate model effects:

| Metric | Luna High | Sol Medium | Astra Medium | What it supports |
| --- | ---: | ---: | ---: | --- |
| Intelligence Index (10-eval weighted composite) | 32 | 40 | 50 | Sol/Astra gain on this broad suite; not a local task success rate |
| Terminal-Bench 4.0, independent AA mini-swe-agent harness | 5% | 19% | 49% | Hard terminal tasks separate strongly |
| AutomationBench-AA | 48% | 58% | 65% | SaaS workflow agent tests favor larger model |
| AA-LCR v1.1 | 79% | 82% | 80% | Near scores on one ~100k-token long-document reasoning test only |
| AA-Omniscience | −6 | 27 | 42 | Calibration/factual reliability varies strongly here |
| Weighted API cost per AA Index task | $0.03 | $0.25 | $1.54 | **Measured on this suite**, not Codex credits or universal task cost |
| Weighted output tokens per task | 20k | 6k | 10k | Effort/model can reverse simple token-price intuitions |
| Measured first-token time | 7.02s | 1.96s | 5.86s | Endpoint and workload specific, not Codex latency SLA |

Method: [AA Intelligence methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) specifies weighted English/text suite; Terminal-Bench 4.0 is 66 tasks, 3 repeats, mini-swe-agent, 500-step maximum, no context compaction; AA-LCR v1.1 has 100 questions across ~100k-token multiple documents, 3 repeats, LLM equality grading. It is **not** a 1M-token recall test and does not prove document synthesis or citation reliability. AA's comparison page sometimes lists Sol context as 872k versus OpenAI's 1.05M; this source discrepancy is unresolved. Use the official advertised maximum, then verify effective runtime limits before relying on them. AA's [methodology](https://artificialanalysis.ai/methodology) defines cost per task as suite-weighted API token spend and output speed after first token. Its measured time per task excludes some overhead and is not a Codex turn-time forecast.

Effort matters: [AA Luna High vs xhigh](https://artificialanalysis.ai/models/comparisons/gpt-6-luna-high-vs-gpt-6-luna-xhigh) reports index 32 vs 34 and TB4 5% vs 8%, at higher token/time use for xhigh. [AA Sol Medium vs High](https://artificialanalysis.ai/models/comparisons/gpt-6-sol-high-vs-gpt-6-sol-medium) reports index 40 vs 43, TB4 19% vs 26%, cost/task $0.25 vs $0.37. Do not use a fixed escalation ladder: effort gains differ by workload.

**Vals AI, separately operated suite, 22 September 2026 updates.** [Astra](https://www.vals.ai/models/openai_gpt-6-astra), [Sol](https://www.vals.ai/models/openai_gpt-6-sol), [Luna](https://www.vals.ai/models/openai_gpt-6-luna) report at **max effort** and no fallback models: Vals Index 66.61% ±1.09 / 62.57% ±0.95 / 58.45% ±1.11; API cost/test $19.09 / $7.56 / $0.42 respectively. Sol and Luna pages say refusals/policy blocks counted as failures. Sol vs Luna: Code Migration 57.20% vs 42.55%; Vibe Code Bench 87.82% vs 81.65%; Terminal-Bench 2.1 83.15% vs 73.03%. But Luna narrowly exceeds Sol on several specific Vals benchmarks (including legal research, finance agent, tax agent): no universal strict capability order per task. Vals has **no Sol/Luna Terminal-Bench 4.0 result** on their pages; do not transfer AA TB4 numbers into Vals comparisons. Max-effort Vals scores cannot directly validate Sol Medium/Luna High route. The [Vals methodology](https://www.vals.ai/methodology) and each benchmark's configuration matter; these are tasks using Vals harness, not local Codex results.

Benchmark-owner spot check: [Terminal-Bench leaderboard](https://www.tbench.ai/) and [SWE-bench official site](https://www.swebench.com/) did not yield a verified exact GPT-6 variant, effort, and harness comparison as of this research. Do not substitute vendor launch scores, another benchmark version, or a family proxy. Two independently operated measurable sources above remain AA and Vals; they use different workload mixes and efforts.

## Proposed route (policy, not documented model fact)

Coordinator remains conversation model the user selected in the app. Keep user intent, task state, tool authority, source assessment, and final synthesis with coordinator. Subagent model choice cannot lower the coordinator's own model/effort. Route substantive ownable work to one worker by default, including sequential phases. Keep parent execution for a concrete transfer-cost or ownership exception. Record model and effort only when runtime actually surfaces them; otherwise report **inherited, not surfaced**.

| Workstream | Starting execution route | Promotion trigger / check |
| --- | --- | --- |
| Deterministic extraction, file inventory, URL/quote collection, classification with exact checks | Luna High (Medium when truly mechanical/high volume and sampled verification passes) | Sol Medium if relationships across sources, ambiguous instructions, or repeated extraction misses |
| Focused small coding fix, test, docs update with clear acceptance | Luna High as experiment; Sol Medium for coupled or ambiguous code | Promote from acceptance failures or known difficult dependencies, not model prestige |
| Complex coding, agentic tool/browser workflows, multi-source research synthesis | Sol Medium | Sol High for a named difficulty; Astra Medium for evidence conflict, coupled systems, high repair cost, or demonstrated Sol failure |
| Hard terminal work, difficult diagnosis, nuanced judgment under conflict, long multistep synthesis | Astra Medium with bounded question and exit condition; High/Max only with task evidence | Downshift bounded repair, test, extraction after hard judgment resolved |
| High-stakes or routing-floor review | Distinct independent reviewer under existing policy; match difficulty, Astra when frontier review required | Review stakes alone do not require Astra to own all implementation |

Long-text route: available window is identical officially. Use Luna for **locating/extracting** scoped fields or citations with deterministic checks; Sol for cross-document reconciliation/synthesis; Astra when evidence conflicts, nuance materially changes decision, or long context makes requirements coupled. AA-LCR at ~100k shows similar scores for one long-context QA test, so choose by task shape, not window size. A controlled local eval should measure exact extraction, citation provenance, synthesis acceptance, total credits, wall time, and repair rate for representative user documents.

Quality/cost/latency objective: minimize **expected total credits and wall time per accepted result**, including coordinator, specialist, tools, failed attempts, repair and independent review. Compare same-task traces. API/token rates indicate feasible starting routes but never prove an Astra pass is cheaper than Sol, or a Luna pass meets the requested quality. Source checks and local acceptance are mandatory before revising model floors.

Sources accessed 24 September 2026. Rankings and pricing can change. Official docs link directly above; independent pages are actual fetched pages, except interactive benchmark-owner row noted as unverified.
