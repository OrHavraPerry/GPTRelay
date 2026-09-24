# GPT-6 operating-point curves (24 September 2026)

Use this reference when model **and effort** might change a route. [Machine-readable points](cost-curves.json) retain each value's source URL. Measurements are API benchmark observations, not Codex credit costs or accepted-result rates. Keep the [routing and review policy](../SKILL.md) and [model evidence](model-evidence.md) in force.

## Artificial Analysis: one comparable suite

[AA Intelligence Index v4.3.2](https://artificialanalysis.ai/methodology/intelligence-benchmarking) combines 10 evaluations, weighted agent 30%, coding 20%, general 30%, science 20%. Index points are a **composite**, not percent of tasks accepted. USD is suite-weighted API token spend **per Index task**; it is not cost per Terminal-Bench task. Time below is AA's estimated output decode time per Index task. It excludes first-token delay, tools, agent overhead, retries, and full task wall time. Performance and latency snapshots can drift; observations were collected on 24 September 2026 from AA's [Luna/Astra](https://artificialanalysis.ai/models/releases/comparisons/gpt-6-luna-vs-gpt-6-astra) and [Sol/Astra](https://artificialanalysis.ai/models/releases/comparisons/gpt-6-sol-vs-gpt-6-astra) release tables. AA estimates less than ±1 point 95% CI for overall Index; subtest uncertainty can differ.

| Model | Effort | Index points | API USD / Index task | Estimated decode, s |
| --- | --- | ---: | ---: | ---: |
| Luna | low | 21 | 0.0045 | 17 |
| Luna | medium | 29 | 0.02 | 80 |
| Luna | high | 32 | 0.03 | 152 |
| Luna | xhigh | 34 | 0.04 | 207 |
| Luna | max | 37 | 0.07 | 373 |
| Sol | low | 34 | 0.13 | 35 |
| Sol | medium | 40 | 0.25 | 60 |
| Sol | high | 43 | 0.37 | 103 |
| Sol | xhigh | 44 | 0.53 | 157 |
| Sol | max | 48 | 1.06 | 279 |
| Astra | low | 46 | 0.82 | 97 |
| Astra | medium | 50 | 1.54 | 212 |
| Astra | high | 51 | 1.73 | 243 |
| Astra | xhigh | 52 | 2.31 | 330 |
| Astra | max | 53 | 3.26 | 525 |

The [AA graph](aa-cost-quality.png) plots all 15 points on a log cost axis. Its connected lines join effort settings, not interpolated operating points. Read exact values from the table or JSON; decode estimates above are rounded to avoid implying stable latency precision.

**Crossover checks.** [Luna xhigh and Sol low](https://artificialanalysis.ai/models/comparisons/gpt-6-luna-xhigh-vs-gpt-6-sol-low) both score 34 Index points, at $0.04 vs $0.13 per Index task, but estimated decode is about 207 vs 35 seconds. Sol wins some subtests and Luna wins another, so neither substitutes for task acceptance. [Sol max and Astra low](https://artificialanalysis.ai/models/comparisons/gpt-6-sol-vs-gpt-6-astra-low) score 48 vs 46; Sol's $1.06 suite spend exceeds Astra's $0.82 while its decode estimate is about 279 vs 97 seconds. Sol and Astra split subtest wins. Astra low can be a bounded candidate for a named hard task that would otherwise use Sol max; the aggregate is no universal Astra upgrade. [Sol high to xhigh](https://artificialanalysis.ai/models/comparisons/gpt-6-sol-high-vs-gpt-6-sol-xhigh) raises the Index 43 to 44 at $0.37 to $0.53 while some subtests fall. Luna max can be tested for a demanding bounded task, but its greater cost and decode time need a relevant acceptance gain.

## Vals: independent suite, max effort only

[Vals methodology](https://www.vals.ai/methodology) reports a separate Index. These **percent scores are not AA points** and do not estimate local task acceptance. Costs are API USD per Vals Index test, unrelated to AA Index task costs. Reported errors are standard errors, not 95% confidence intervals. Latency is response completion or agentic wall time under Vals' harness, not AA decode time. Snapshot 24 September 2026:

| Model, max effort | Vals Index % ± SE points | API USD / Vals Index test | Listed latency |
| --- | ---: | ---: | ---: |
| [Luna](https://www.vals.ai/models/openai_gpt-6-luna) | 58.45 ± 1.11 | 0.419 | 26m 30s |
| [Sol](https://www.vals.ai/models/openai_gpt-6-sol) | 62.57 ± 0.95 | 7.564 | 26m 34s |
| [Astra](https://www.vals.ai/models/openai_gpt-6-astra) | 66.61 ± 1.09 | 19.09 | 25m 11s |

The [separate Vals graph](vals-cost-quality.png) uses its own score and cost axes. Vals provides no effort curve on these pages. Luna beats Sol on some Vals workloads, while Sol leads Code Migration and Terminal-Bench 2.1. Neither those benchmark versions nor their task mixes match AA's Terminal-Bench 4.0.

## Editorial and vendor evidence

[Forward Future's Astra review](https://signals.forwardfuture.com/astra-review/) describes hands-on browser, creative, research, and presentation work, including fixes and steering needed on ambitious tasks. Its benchmark table transcribes **OpenAI-reported** maximum scores, and its prices come from OpenAI. The [23 September newsletter](https://forwardfuture.com/newsletter/daily/2026-09-23/anthropic-s-claude-5-5-openai-s-gpt-6-ai-copyright) summarizes Sol/Luna prices without an independent cost curve. [OpenAI's launch post](https://openai.com/index/introducing-gpt-6-sol-and-luna/) reports benchmark-specific scores and task costs, such as AutomationBench Sol xhigh 33.2% at $0.27/task; those are vendor measurements with their own harness, not another AA or Vals point.

Matthew Berman's [22 September livestream](https://www.youtube.com/watch?v=5MFORiebZks) and [channel listing for the 23 September Luna review](https://www.youtube.com/@matthew_berman/videos) were checked through YouTube metadata and third-party summaries. No full direct watch or primary transcript was available. Summaries describe launch-chart commentary, but their numeric labels conflict with the OpenAI source in one case; no independently measured cost curve could be verified. Exclude those secondary figures from the canonical points and graphs. See dated [Forward Future research](forwardfuture-research.md) for details.

## Apply to Relay

Enforce quality, capability, safety, and independent-review floors first. Pick candidates whose **subtask** evidence fits the work and compare model-effort pairs directly. Sol low is worth testing where response latency dominates; Luna xhigh or max where its focused quality clears acceptance at acceptable wall time; Astra low where a named hard problem and relevant evidence justify it versus Sol high/max. Preserve the same-task route, one-writer lease, fallback limits, and bounded Astra exit. A composite score divided into dollars is **not** cost per success.

For local calibration, sample representative tasks per class and record prompt, actual runtime model/effort, acceptance criterion, first-pass and final acceptance, total wall time, and spend for worker, parent, tools, retries, repair, and independent review. Keep Codex credits and API USD separate. Compare total spend and wall time **per accepted result** only from those observed trials; treat subjective outcomes with blind review. Do not revise capability or review floors from these aggregate curves alone.
