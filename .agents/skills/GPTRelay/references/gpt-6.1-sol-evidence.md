# GPT-6.1 Sol routing evidence, 1 October 2026

For newer coding/terminal, OS, browser/research, and extraction evidence with explicit gaps, read [task-specific evidence checked 3 October](task-benchmarks-2026-10-03.md). This file retains its dated snapshot; do not mix its harness scores with the newer Codex-harness tables.

Current Sol is `gpt-6.1-sol` when the collaboration tool and host surface it. This evidence supports a provisional default update, not a universal quality ranking or an Astra review replacement. [Previous evidence](model-evidence.md), [curves and graphs](cost-curves.md), and their JSON remain historical `gpt-6-sol` snapshots.

## Documented facts and vendor guidance

OpenAI's [29 September changelog](https://developers.openai.com/api/docs/changelog) records release. The [model page](https://developers.openai.com/api/docs/models/gpt-6.1-sol) lists a 1,050,000-token context, 128,000 maximum output, text/image input and text output. API effort supports low, medium (default), high, xhigh, max; none/minimal are unsupported. Responses supports tool calling; Chat Completions does not support tool calling for this model. Standard API USD per 1M tokens, up to 272k input: $2 input, $0.10 cached input, $2.50 cache write, $10 output. These are API specifications, not a Codex host's control list or usage allowance.

[Codex models](https://learn.chatgpt.com/docs/models) recommends GPT-6.1 Sol for complex coding/agentic workflows when available, Luna for focused repeatable work, and Astra for hardest work. Availability depends on client, account, workspace, and rollout; the selected runtime is authoritative. Codex controls may expose ultra: official guidance describes it as using subagents, distinct from API reasoning effort. Preserve exact requests and report unavailable gates; never silently convert ultra to max.

[Codex token rates](https://learn.chatgpt.com/docs/pricing#token-rates) separately lists GPT-6.1 Sol at **50 / 2.5 / 250 credits** per 1M input / cached input / output tokens. Previous Sol is 50 / 5 / 250. Equal uncached input/output prices do not imply equal task spend; cache mix, reasoning, retries, review, and coordinator usage matter. Do not convert API dollars to credits. Speed-mode and subscription usage multipliers are separate from Standard token rates.

OpenAI's [model-selection guide](https://developers.openai.com/api/docs/guides/model-selection) suggests Sol Medium for complex technical work and xhigh for polished/conflicting-evidence work. “Near-Astra” is **vendor positioning**, not proof of local acceptance, speed, savings, or review equivalence. Relay keeps Medium provisionally and promotes for a named difficulty or failed check; frontier review remains exact `gpt-6-astra`.

## Independent measurements

**Artificial Analysis, Intelligence Index v4.3.2.** The [release page](https://artificialanalysis.ai/models/releases/gpt-6-1-sol) reports:

| GPT-6.1 Sol effort | Index points | API USD / Index task |
| --- | ---: | ---: |
| low | 42 | 0.13 |
| medium | 48 | 0.21 |
| high | 50 | 0.32 |
| xhigh | 51 | 0.39 |
| max | 52 | 0.72 |

[Same-effort Medium comparison](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-medium-vs-gpt-6-sol-medium) reports 48 versus previous Sol's 40 Index points. [High versus Astra High](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-high-vs-gpt-6-astra-high) reports 50/51 Index, 52%/54% Terminal-Bench 4.0, $0.32/$1.73 per Index task, while SciCode is 56%/55% and AA-LCR 82%/80%. Workload wins differ. [Methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) defines a weighted ten-evaluation composite; points are not acceptance percentages and API task costs are not Codex credits. Output speed excludes reasoning delay, tools and other overhead; it does not establish total accepted-result latency.

**Vals AI, separate harness, current model tables fetched 1 October.** Each page lists default reasoning effort **max**; individual benchmarks may override settings:

| Model | Vals Index % ± SE points | API USD / Vals Index test | Listed latency |
| --- | ---: | ---: | --- |
| [GPT-6.1 Sol](https://www.vals.ai/models/openai_gpt-6.1-sol) | 61.15 ± 1.01 | 3.237 | 43m 10s |
| [GPT-6 Sol](https://www.vals.ai/models/openai_gpt-6-sol) | 57.54 ± 1.01 | 7.581 | 29m 16s |
| [GPT-6 Astra](https://www.vals.ai/models/openai_gpt-6-astra) | 63.13 ± 1.19 | 18.46 | 27m 48s |

6.1 Sol/previous Sol Code Migration is 65.12%/57.20%, but CyberBench v1.1 is 39.29%/77.98%: replacement is not a per-workload dominance claim. Current tables differ from old launch-update prose and search snippets (old Sol 62.57%, Astra 66.61%); do not mix snapshots. [Vals methodology](https://www.vals.ai/methodology) uses its own workloads, aggregation and uncertainty. Vals percentages, costs and harness latency cannot be merged with AA points/costs or treated as local Codex results. Max-effort evidence does not validate Medium directly.

No local model experiments or accepted-result credit measurements were run for this update. Keep quality/capability/review gates first and compare total worker, parent, tools, retries, repair and review spend per accepted result only when observed. Future calibration needs authorization; this document does not authorize benchmark runs or experimental chats.
