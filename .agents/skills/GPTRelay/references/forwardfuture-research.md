# ForwardFuture coverage of GPT-6 models and routing evidence

Research checked: 2026-09-24. Scope: ForwardFuture material relevant to GPT-6 Astra/Sol/Luna routing, effort levels, and cost per completed task. I traced benchmark and price figures to original sources where linked. ForwardFuture statements are separated from source data and interpretation.

## Findings

ForwardFuture has a substantial first-hand Astra review, but it is qualitative for hands-on work. Its benchmark table explicitly reproduces OpenAI’s reported results and says scores are maximum reported at any effort. Its API price section also cites OpenAI’s September 3 launch brief. The review does not present an independent Astra-versus-Sol/Luna price-per-task or effort curve.

The September 23 Forward Future newsletter is a short summary of OpenAI’s GPT-6 Sol/Luna launch. It repeats OpenAI’s API prices and broad claims, then links the OpenAI announcement. It does not show task-cost graphs or independent task-cost measurements. Searches of Forward Future and Signals for GPT-6 Sol/Luna cost/effort coverage found no other relevant original test. This is a bounded search result, not proof no page exists.

The useful task-cost points are in the linked OpenAI primary post, not independently tested ForwardFuture evidence. The most complete explicit effort/score/cost table is AutomationBench:

| Model and effort | Score | Cost per task | Provenance |
|---|---:|---:|---|
| GPT-6 Sol, xhigh | 33.2% | $0.27 | OpenAI-reported, AutomationBench 1.0.6 |
| GPT-6 Astra, low | 30.3% | 3.9× Sol | OpenAI-reported; absolute cost not printed in this table |

OpenAI describes AutomationBench as end-to-end workflows across 47 tools and business functions. These scores/costs are not ForwardFuture measurements and cannot establish general routing economics outside this benchmark and harness.

Other GPT-6 results in OpenAI’s Sol/Luna announcement (all vendor-reported):

- GPT-6 Sol at max effort scores 56.4% on Agents’ Last Exam. No absolute cost is given in the article text.
- DeepSWE v1.1: GPT-6 Sol max scores 68.8% and GPT-6 Luna max scores 66.6%. Absolute task costs are not stated in extracted text.
- OSWorld 2.0 offline: GPT-6 Sol xhigh scores 60.5%. The cited setting is the offline set from v2026.08.08; partial reward is the metric.

These figures form a useful hypothesis for a routing policy (test Sol at xhigh/max and Luna at max/high on professional-work/code/computer-use classes; reserve Astra for cases where its quality advantage matters), but they remain OpenAI claims. They do not establish Codex credit usage, model/effort token counts, total accepted-result cost, or performance on the user’s local tasks. No API per-token price can substitute for those measurements.

## ForwardFuture material and source provenance

1. [Astra: The Full Review](https://signals.forwardfuture.com/astra-review/) (homepage dates it Sep 3, 2026).
   - First-hand work: the reviewer describes building small 3D worlds, games, research/deck tasks, browser workflows, writing, and multi-day SimCity-style work. The reviewer notes failures/revisions too: controls needed fixing, repeated slide layouts, a render stopped for machine slowdown, and long projects still needing review. These are qualitative anecdotes, not controlled comparative measurements.
   - Benchmark table: page says “OpenAI’s reported results” and cites OpenAI’s final post, verified Sep 3, 2026. Values are maximum scores at any effort. The comparison table is therefore a convenient secondary transcription of vendor data, not an independent benchmark.
   - Relevant visible scores: Astra 41.4% AutomationBench, 74.1% DeepSWE v1.1, 64.6% Terminal-Bench Science 0.1, and 72.6% OSWorld 2.0 in the cited OpenAI source’s latency comparison. The FF review does not make these effort-specific in its table. These figures do not establish production Codex performance or one overall score.
   - The page lists Astra API standard at $10 input/$50 output and fast at $20/$100 per million tokens, attributing the numbers to OpenAI’s Sep 3 brief; its fast rate is calculated from OpenAI’s 2× price statement. It reports no task-cost curve.
   - Reviewer’s practical judgment: Astra is their go-to for difficult work; their hands-on reports that it often needed more direction and that many harder tasks ran for about 30 minutes. Useful as user-experience evidence, not a general latency benchmark.

2. [Sep 23 Forward Future newsletter](https://forwardfuture.com/newsletter/daily/2026-09-23/anthropic-s-claude-5-5-openai-s-gpt-6-ai-copyright), “OpenAI Launches Lower-Cost GPT-6 Sol and Luna.”
   - This is a summary attributed to Matthew Berman and Nick Wentz; it says Sol is $2/$10 and Luna $0.10/$0.50 per million input/output tokens. It links directly to OpenAI’s launch post. These are API rates, not costs per task.
   - No hands-on Sol/Luna testing, effort-specific table, cost-per-task chart, or independent method is presented on this page.

3. [Forward Future homepage](https://forwardfuture.com/).
   - Lists the Astra review as “Review · Sep 3, 2026.” At the time checked, homepage’s model-review listing had no dedicated Sol/Luna review.

## Primary-source cross-checks

- [OpenAI: Introducing GPT-6 Sol and Luna](https://openai.com/index/introducing-gpt-6-sol-and-luna/) (Sep 22, 2026): source of the new-family API prices, task-cost claims, effort labels, benchmark definitions, and Luna/Sol comparisons above. The article says values come from OpenAI research/API evaluations. AutomationBench is the only extracted text table here with exact GPT-6 effort, score, and dollar task cost. Its graph/chart content may contain additional observations not exposed in the accessible article text; those were not inferred.
- [OpenAI: GPT-6 Astra](https://openai.com/index/gpt-6-astra/): source of the Astra benchmark values reproduced by the FF review. OpenAI describes the model as the best for computer use, professional work, coding, science, and cybersecurity. Such superlatives are vendor framing. The source reports an OSWorld 2.0 latency simulation point for Astra: 72.6% at about 40 minutes per task; this is vendor-reported and is task time, not a dollar cost curve. OpenAI also describes 1.9× faster completion for Astra plus updated Codex harness on Mind2Web, so do not attribute that speed change solely to the model.

## Routing use and limits

- Treat FF’s qualitative Astra review as useful task-shape evidence: browser/computer use, polished knowledge work, and longer creative builds; expect review and steering on ambitious work.
- Treat FF’s benchmark table and API prices as secondary pointers to OpenAI claims. Use OpenAI directly for data extraction and caveats.
- Consider GPT-6 Sol/Luna cost-per-task claims as hypotheses to validate in the relevant workload and harness. Exact points on AutomationBench are explicit above; several other comparisons have ratios but no absolute cost in text.
- Do not translate API dollars/task or prices per million tokens into Codex credits. No source reviewed provides effort-specific Codex credit-per-accepted-result data for Astra/Sol/Luna.
- Missing provenance/unknowns: the accessible OpenAI article does not state complete raw token counts, full task-cost methodology, trial variance/sample size for every table, or reproducible harness configuration. The FF Astra article’s hands-on projects have no controlled baseline, repeated trials, or aggregate cost/effort accounting. The full task-cost curve/figure datapoints, if visually embedded beyond article text, were not accessible as tabular data and remain unreported here.

## Matthew Berman YouTube fallback (checked Sep 24, 2026)

YouTube pages are JavaScript-rendered and direct watch-page fetch did not expose transcript text in this review. I did not watch the videos end-to-end. Below, “content” means only what was exposed in YouTube search metadata/descriptions or third-party transcript/AI-summary mirrors; those mirrors can mislabel benchmarks and are not primary evidence. No summary should be quoted as a verified transcript.

Relevant latest uploads located:

- [GPT-6 SOL AND LUNA ARE OUT!!!](https://www.youtube.com/watch?v=5MFORiebZks), Matthew Berman, Sep 22, 2026; about a two-hour livestream per third-party index. The YouTube-derived listing gives the title, channel, upload date, and description context; Hexdigest labels its summary AI-generated and describes launch price/benchmark commentary. This is apparently commentary on release charts, not a controlled Berman-run benchmark; transcript and graph details not accessible directly. [Third-party summary](https://hexdigest.dev/t/matthew-berman?sort=top).
- [GPT-6 Luna Might Be the Best Deal in AI](https://www.youtube.com/@matthew_berman/videos) (Sep 23, 2026 per Hexdigest/Alcreon; their pages did not yield a stable matching video URL, so link to the channel listing). Hexdigest’s AI-generated summary describes effort/cost graph discussion and states: Luna max >20% on AutomationBench for <$0.05/task; Luna max at $0.11/task on a “Frontier Code” section; Luna max 66.6% at $0.22/task on an “Agentic Coding Benchmark”; OSWorld Luna 53% vs Astra 73%; Sol xhigh 33% on AutomationBench. These are secondary transcript claims, not independently measured here. There is a source-label mismatch: OpenAI’s primary launch post assigns 66.6% to Luna on DeepSWE v1.1, not FrontierCode, so use OpenAI’s table/source as canonical unless original video confirms the label. Berman’s summary indicates his same-day comparison graphic was made with Astra, making that graphic illustrative/reproduced rather than an independent evaluation. [Hexdigest AI-generated summary](https://hexdigest.dev/e/4979-gpt-6-luna-might-be-the-best-deal-in-ai), [Alcreon summary](https://www.alcreon.com/podcast-digest/gpt-6-luna-might-be-the-best-deal-in-ai).
- Channel aggregation also lists [GPT-6 Sol and Luna Are HERE!](https://www.youtube.com/watch?v=Ima_AVPyQ9E), ~7:26, and an AI-generated synopsis frames it as launch reaction. It does not expose a distinct firsthand test or task-cost evidence; likely overlaps with the announcement coverage above. [Channel feed metadata](https://www.theaigentic.com/).

Assessment: this fallback adds Berman’s public commentary around launch and secondary-reported task-cost plot readings, but it does not supply independently reproducible benchmark evidence. Berman’s demonstrated comparison appears to reuse vendor benchmark results; the task-cost points above are not presented with an accessible method, raw trial data, task count/variance, or audit trail. The separately discussed same-prompt Codex website run (Astra 16 min, Sol 15 min, Luna 20 min) appears in a third-party summary of a different creator’s video, not Berman’s; exclude it from Berman’s evidence.
