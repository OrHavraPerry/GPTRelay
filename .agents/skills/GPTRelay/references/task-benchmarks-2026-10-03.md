# Task-specific model evidence, checked 3 October 2026

Scope: `gpt-6-luna`, `gpt-6.1-sol`, and `gpt-6-astra`. Previous `gpt-6-sol` remains historical. Access dates below are 2026-10-03; an access date is not an evaluation date. Live leaderboards can change. Apply [routing policy](../SKILL.md) before these observations.

## Coding: implementation and repository understanding

Artificial Analysis publishes exact model/effort rows using the **Codex harness**. These are independent measurements, not OpenAI launch claims:

| Model / effort | DeepSWE v1.1, % | SWE-Atlas-QnA, % |
| --- | ---: | ---: |
| GPT-6 Luna / max | 64 | 44 |
| GPT-6.1 Sol / medium | 72 | 61 |
| GPT-6.1 Sol / xhigh | 73 | 61 |
| GPT-6 Astra / max | 68 | 62 |

[AA source rows](https://artificialanalysis.ai/agents/coding-agents/comparisons/codex-vs-opencode). Measurement date not stated. [Coding Agent Index v1.5 methodology](https://artificialanalysis.ai/methodology/coding-agents-benchmarking): DeepSWE contains 113 implementation tasks; SWE-Atlas-QnA contains 124 repository questions. Results average three attempts per task. DeepSWE disables internet browsing. Different efforts do not isolate model effects. Repository Q&A is not implementation success.

Separate **Vals** observations, model pages default to **max** effort:

| Model | Code Migration, % ± SE | Vibe Code Bench v1.1, % ± SE |
| --- | ---: | ---: |
| [GPT-6 Luna](https://www.vals.ai/models/openai_gpt-6-luna) | 42.55 ± 4.42 | 81.65 ± 3.38 |
| [GPT-6.1 Sol](https://www.vals.ai/models/openai_gpt-6.1-sol) | 65.12 ± 4.36 | 88.93 ± 1.89 |
| [GPT-6 Astra](https://www.vals.ai/models/openai_gpt-6-astra) | 67.74 ± 4.22 | 89.59 ± 2.17 |

These tasks differ from AA's. Follow benchmark-specific provider/parameter overrides on Vals pages. [Vals methodology](https://www.vals.ai/methodology) reports standard errors, not 95% confidence intervals. Use current tables rather than older launch-update prose on the same page.

Implication: Luna is a provisional choice for focused, checked edits; broad migration and coupled implementation justify Sol. Neither suite directly measures simple local edits at Luna High.

## Terminal: hard agentic work versus routine commands

| Model / effort | AA Codex Terminal-Bench 4.0, % | Vals Terminal-Bench 4.0 at max, % ± SE |
| --- | ---: | ---: |
| GPT-6 Luna / max | 15 | 13.64 ± 1.51 |
| GPT-6.1 Sol / medium | 52 | 55.05 ± 1.82 |
| GPT-6 Astra / max | 56 | 59.60 ± 4.40 |

Sources: [AA Codex rows](https://artificialanalysis.ai/agents/coding-agents/comparisons/codex-vs-opencode), [Vals Luna](https://www.vals.ai/models/openai_gpt-6-luna), [Vals Sol](https://www.vals.ai/models/openai_gpt-6.1-sol), [Vals Astra](https://www.vals.ai/models/openai_gpt-6-astra). The Sol row uses different efforts across columns. AA's 66-task TB4 includes difficult engineering, computing, security, and administration. Keep AA Codex results separate from AA Intelligence Index's mini-swe-agent harness and from Vals runs. TB2.1 scores are not TB4 scores.

Implication: hard terminal planning/diagnosis is a named reason for Sol/Astra. Executing a known script, aggregating CSV data, or running focused tests remains bounded Luna work; tool name alone cannot determine model tier.

## OS and computer use

[CUA Speedrun's independent OSWorld 2.0 subset](https://cuaspeedrun.com/dataset-osworld2-k52.html) measures **52 tasks**, mean verifier score with **partial credit**:

| GPT-6 Astra effort | Partial score, % | Mean active task time, s | API USD/task |
| --- | ---: | ---: | ---: |
| low | 68.17 | 904.2 | 6.3363 |
| medium | 67.18 | 828.1 | 6.5192 |
| high | 75.02 | 914.0 | 7.3909 |
| xhigh | 76.90 | 1237.3 | 8.1746 |

Evaluation date not stated. Setup/grading time excluded. No Luna or 6.1 Sol row verified there. This subset does not establish full-set performance; effort is not monotonically better in these observations.

[OpenAI's Astra launch table](https://openai.com/index/gpt-6-astra/) separately reports **72.6% partial score** on OSWorld 2.0 **v2026.08.08 offline set**. It selects maximum scores across efforts without naming this row's effort: vendor evidence, not CUA Speedrun's measurement. The [6.1 Sol launch](https://openai.com/index/introducing-gpt-6-1-sol/) reports a max-effort result within 2.1 percentage points of Astra at max; the retrieved text did not expose exact chart values, so none are invented here. The [benchmark-owner site](https://osworld-v2.xlang.ai/) defines 108 workflows but its retrieved leaderboard table exposed no exact GPT-6 rows. Partial reward is not percentage of workflows fully completed.

Routing implication: preserve Astra Low minimum for visual/GUI phases as user policy. Evidence gaps cannot establish missing models' inability, and these scores do not prove any local tool/session permissions.

## Browser UI versus web research

Exact-model browser UI comparisons on WebArena/WebVoyager/BrowserGym were not verified in consulted primary pages. OSWorld covers broader GUI workflows, not a separate browser-only comparison. This remains a scoped evidence gap.

Web information discovery **does** have exact-model evidence: [Mercor BrowseComp Extended](https://www.mercor.com/apex/mercor-extended/ots-held-out-browsecomp-leaderboard/) uses 130 public questions. The [model list](https://www.mercor.com/apex/mercor-extended/ots-held-out-browsecomp-leaderboard/sample-task/) shows:

| Model / effort | BrowseComp Extended pass@1, % |
| --- | ---: |
| GPT-6 Luna / max | 47.2 |
| GPT-6.1 Sol / max | 67.7 |

Measurement date and detailed agent/tool configuration are not stated on these pages. No Astra Extended row verified. Mercor's **original BrowseComp** result for 6.1 Sol Max is **95.4%**; OpenAI separately reports Astra **91.5%**, maximum at any effort. Do not merge original and Extended, or vendor and independent snapshots. [BrowseComp's primary paper](https://arxiv.org/abs/2504.12516) evaluates hard-to-find information; its score does not establish mouse/keyboard, screenshot interpretation, form completion, or citation quality.

Routing implication: text/API extraction and source maps may use Luna; hard discovery and cross-source reconciliation justify Sol. Browser UI interactions still require Astra under user policy.

## Extraction, data processing, and research synthesis

No dedicated exact-model extraction accuracy or comparable spreadsheet-processing score was verified in consulted primary pages. AA lists AnalystAgent but retrieved tables did not expose comparable variant results. Do not repurpose hard terminal or broad Index scores as extraction accuracy.

[Official model guidance](https://learn.chatgpt.com/docs/models) recommends Luna for focused repeatable extraction/transformation and Sol for complex work. This supports Luna-first as a **provisional routing policy**, not measured local savings. Use deterministic scripts for known transformations; check row counts, totals, field provenance, and representative difficult cases as appropriate.

Long-document evidence is narrow: [AA Luna High / Astra Medium](https://artificialanalysis.ai/models/comparisons/gpt-6-luna-high-vs-gpt-6-astra-medium) reports AA-LCR v1.1 **79% / 80%**; [6.1 Sol High / Astra Low](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-high-vs-gpt-6-astra-low) reports **82% / 80%**. [Methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking): 100 questions over about 100k tokens, three repeats, answer grading. This is not 1M-token recall, broad synthesis acceptance, or citation verification.

Vals Legal Research Bench at max is Luna **30.29% ±3.19**, 6.1 Sol **38.46% ±3.38**, Astra **39.42% ±3.40**; sources are the [Luna](https://www.vals.ai/models/openai_gpt-6-luna), [Sol](https://www.vals.ai/models/openai_gpt-6.1-sol), and [Astra](https://www.vals.ai/models/openai_gpt-6-astra) tables. Legal research is one domain, not general synthesis.

## Cost, latency, and limits

AA's **coding suite averages**, not per-TB4-task costs: Luna Max **$0.18 / 21.4 min**, 6.1 Sol Medium **$0.70 / 10.9 min**, Astra Max **$7.47 / 29.4 min**. [Source](https://artificialanalysis.ai/agents/coding-agents/comparisons/codex-vs-opencode). Minutes are active agent time; environment startup and grading excluded. Lower API price does not guarantee lower latency. These are API USD, not Codex credits or local cost per accepted result.

No local model bakeoff, experimental chat, or accepted-result credit measurement ran for this update. Compare phases using acceptance plus total parent/worker/tools/retry/repair/review spend and wall time when authorized calibration exists. Preserve exact requests, independent review, and tool/access gates. New chats cannot create missing permissions; use [persistent-chat handoff](persistent-chat.md).
