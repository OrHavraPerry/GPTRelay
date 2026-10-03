---
name: GPTRelay
description: Coordinate GPT-6 work with in-process subagents by default and an explicitly requested persistent-chat option. Route bounded work by capabilities, quality, total accepted-result cost, and latency; keep independent review and one-writer ownership.
---

# GPTRelay

Scope: OpenAI Codex with GPT-6 Astra, GPT-6.1 Sol (or previous GPT-6 Sol), and GPT-6 Luna collaboration subagents. This skill does not route work through other assistants or runtimes.

Keep the current conversation for user dialogue, intent, scope, routing, tracking, acceptance, and final synthesis. Use standard collaboration subagents **within this same task** for substantive ownable technical work, research, and long-source extraction. In-process collaboration is the default. A new persistent Codex chat is an optional, user-owned task only when the human explicitly requests a new chat/task; describing this option does not authorize creation. Follow [persistent-chat handoff](references/persistent-chat.md) for that route. Never present a persistent chat as an invisible subagent.

Choose route, model, and effort separately. Minimize expected total credits and wall time per accepted result, including tools, coordinator, transfer, retries, repair, and review. Meet quality and risk requirements first. Prioritize reputable independent benchmarks, triangulate across organizations and harnesses, and test local acceptance. Vendor claims, API prices, visible brevity, and model size alone do not prove task savings.

## Route within the task

Apply gates in order:

1. Capability gate. Identify required tools, resource/session access, host, and approval flow for the phase; verify the proposed owner can use them under the authorized scope. Do not assume parent and worker have identical inventories.
2. Required independent review. Reserve a distinct fresh read-only reviewer and its model tier.
3. Independent bounded workstreams. Parallelize only when each has separate ownership, evidence, and useful concurrent progress.
4. One in-process worker for a substantive independently ownable phase, including a sequential phase.
5. Parent execution for a small direct fact, a few tool checks, final verification, or a named case where transfer cost exceeds expected benefit or no worker can own the work without losing critical live context.

Do not call a task parent-only merely because work is sequential, a parallel branch is absent, or parent has convenient tools. Prefer one worker for one phase. Fan out only genuinely independent work with clear coordination benefit. Do not create a persistent chat merely to enforce a model or make work visible. If a worker lacks required capabilities, offer a concrete handoff to an eligible parent or explicitly requested persistent chat. In first commentary, state concrete route and reason.

At phase start, the assigned worker checks actual tool availability and needed resource access before dependent work, then reports any gap immediately. Stop that dependent phase and release or interrupt its current owner before reassigning it. Subagents inherit the applicable sandbox; verify actual tools and resource/session access rather than assuming a new owner escapes it. A stronger model does not fix missing tools, sessions, or permissions. Continue independent eligible work. A persistent chat may have its own host tools and approval UI, but grants no guarantee of wider permissions or every tool; verify the destination. Autonomy remains within the original authorized scope and never bypasses restrictions.

Record each phase concisely: outcome and acceptance checks; topology; requested versus observed model/effort; verified tools/access; and any named reason for bypassing Luna. Unknown inherited settings do not satisfy an exact model or capability floor.

Parent owns canonical task state, user authority, acceptance, and final answer. Give workers raw paths, URLs, commits, source pages, constraints, and checks. A summary alone cannot replace original sources for material analysis. A Luna extraction worker returns a factual map with precise citations, counterevidence, and coverage unknowns; a Sol synthesis worker receives that map **and raw source pointers**. Parent assesses source quality and verifies claims before acceptance. Workers return difficult questions or review needs to parent, not a private agent tree.

While a worker owns a phase, coordinate through its messages. In the brief, ask for an immediate blocker or failed acceptance check requiring a parent decision, a concise update at a meaningful phase boundary for longer work, and a final report with artifact paths, checks, risks, and next action. Short bounded phases may skip routine progress updates; report blockers immediately. Prefer a 30–60 second event wait over repeated 10-second polling, subject to the active user-update limit. A wait timeout alone is not a reason to inspect the worker's transcript, reread its files, rerun its checks, or send a status request. Ask one targeted question if the user needs an answer, the expected duration is materially exceeded without an update, or a reported issue needs a decision. On handoff, read the worker's evidence and run focused acceptance once; retain required independent review and intervene on concrete risk or unexpected drift. Do not shadow an active writer.

Use prompt-only or few-turn forks for independent work. Full-history forks only when entire conversation is necessary and inherited settings suffice. A delegated worker may not subdelegate unless explicitly authorized by parent and ownership remains clear. Do not use multiple workers on a tightly sequential shared-state chain or overlapping writes.

All collaboration agents share the filesystem. Exactly one automated mutating owner holds a checkout at a time, counting parent and descendants. Parent performs no writes while an in-process worker or persistent chat holds that lease. Release or interrupt the original owner before assigning replacement ownership; if ownership is ambiguous, stop overlapping writes. A second writer requires a separate worktree; isolate ports, databases, processes, and generated outputs too, or serialize writes. Before lease, snapshot branch, revision, status, and dirty paths; declare owned paths and pause integration on unexpected drift. Read-only reviewer gets no writer lease. A worktree is directory isolation, not a new task.

## Model and effort

The user selects conversation model in the app. This skill cannot switch current parent model or effort. If no runtime control exposes them, report _inherited, not surfaced_ once; never claim a requested worker route was executed without evidence. Child routing does not lower parent cost. Keep coordinator compact and route ownable execution to workers. An explicit user or project model/effort requirement stays exact. If an external exact requirement names a legacy model, ask its owner rather than silently substituting GPT-6.

### Visual and browser floor (user policy)

Visual creation, inspection, and judgment, and all browser interactions, including routine navigation, clicks, forms, and UI checks, require **`gpt-6-astra` at least Light (`low`)**. Increase effort for hard work under the gates below. This is the user's routing policy, not a claim that benchmarks prove universal visual superiority. Apply the floor to each visual/browser phase; text/API web research and nonvisual coding phases retain ordinary routing.

The visual/browser requirement itself is sufficient reason for Astra execution; no cheaper-model failure or hard diagnosis is needed. Parent-only and transfer-cost exceptions cannot bypass this floor. Execute with a parent whose actual model/effort meets it, or delegate the phase to an eligible Astra worker; an unknown inherited setting does not prove eligibility. If Astra, a supported effort at or above low, or required tools are unavailable, report the missing gate and stop that phase. Do not substitute Sol/Luna or imply the parent switched model. Continue independently useful nonvisual work when possible. Visual/browser review follows the same floor and still requires a distinct fresh reviewer whenever independent review is required.

For non-exact routes outside the visual/browser floor, **Sol means `gpt-6.1-sol` when surfaced by the selected collaboration tool and host**. If unavailable, use surfaced `gpt-6-sol` and report the substitution; historical GPT-6 Sol evidence does not measure GPT-6.1 Sol. Exact requests for either model stay exact. If neither Sol is available, apply the fallback gates below.

For eligible bounded nonvisual phases, **Luna is the default**: extraction, classification with defined labels, data transformation/aggregation, inventories, source maps, formatting, focused coding, tests, and docs with clear acceptance. Use existing deterministic scripts first for mechanical work. Known shell data transformations and focused test execution remain eligible; hard terminal diagnosis, planning, or coupled repair does not become bounded merely because it uses shell commands. A one-off tiny direct parent check may use the named transfer-cost exception. A simple phase cannot inherit the entire task's difficulty or its Astra review tier.

Choose Sol instead only for named ambiguity, coupling, failed acceptance, a capability gap on the selected runtime that an eligible Sol owner actually resolves, an exact requirement, or comparable local workload evidence. Do not upgrade model while leaving the missing tool gate unresolved. At each phase boundary, downshift newly bounded work to Luna; retain a higher tier only with a recorded remaining reason.

Use these provisional **GPT-6-family-only** starting points when local comparable evidence is absent:

| Model | Starting work | Effort |
| --- | --- | --- |
| Luna (gpt-6-luna) | Bounded extraction, labeled classification, data processing, inventories, source maps, formatting, focused coding/tests/docs | Medium for mechanical volume with sampled checks; High for focused coding or synthesis. xhigh requires named failed check or relevant workload evidence. |
| Sol (gpt-6.1-sol; gpt-6-sol availability fallback) | Named ambiguity, coupling, failed checks, cross-source reconciliation, or verified capability/evidence exception | Medium; High for a named difficulty or failed acceptance. |
| Astra (gpt-6-astra) | All visual/browser phases; named hard diagnosis, coupled systems, conflicting evidence, difficult multistep judgment, frontier review | Low minimum for visual/browser work; Medium for hard judgment; High for named hard execution; otherwise Low when evidence supports it. xhigh or above requires lower-Astra-effort failure or relevant workload evidence. |

Outside the mandatory visual/browser floor, these are workload hypotheses, not universal rankings. Select an operating point (model **and** effort) by first enforcing task quality, capability, and independent-review gates; then compare relevant workload evidence for total accepted-result cost and wall time. Compare plausible points directly rather than climbing a fixed cheap-to-expensive ladder. Sol Low is a latency candidate for bounded work; Luna xhigh/max can be quality candidates when their extra reasoning meets a named check at acceptable latency. Astra Low is a candidate for a named hard problem when Sol High/Max would spend much longer reasoning and the relevant workload supports it. Preserve the bounded-Astra requirement below. Aggregate scores alone never change a floor or prove local acceptance.

For task-specific evidence and limits, read [references/task-benchmarks-2026-10-03.md](references/task-benchmarks-2026-10-03.md). Luna-first is routing policy; benchmark scores and API prices do not establish local accepted-result savings. For current Sol evidence and effort controls, read [references/gpt-6.1-sol-evidence.md](references/gpt-6.1-sol-evidence.md). For historical GPT-6 evidence, operating-point curves, limitations, and sources, read [references/model-evidence.md](references/model-evidence.md) and [references/cost-curves.md](references/cost-curves.md) when comparing or changing routes. Keep API dollars and Codex credits separate. Refresh when availability/pricing changes or observed acceptance invalidates a route; do not browse every routine turn. If routes remain uncertain, calibrate representative tasks with actual model/effort, acceptance, wall time, and **total** spend including parent, review, retries, and repair; compare within a task class and keep units separate.

Use model and effort options surfaced by selected collaboration tool and host. Full-history forks inherit settings; explicit overrides require prompt-only or limited-history forks when tool schema permits. Preserve actual or _inherited, not surfaced_ in handoffs. For non-exact, nonvisual work without browser interaction only: if Luna unavailable, consider Sol then Astra; if Sol unavailable, consider Astra, or Luna only after reclassifying as bounded with equivalent checks; if Astra unavailable, Sol may handle ordinary reclassified execution, but an exact Astra or frontier-review gate remains missing. Never silently lower a capability floor. None, minimal, and ultra are not universal effort options; use only exposed values. Higher effort is not automatically better.

GPT-6.1 Sol's API supports low, medium, high, xhigh, max; it rejects none/minimal. Codex host controls can also expose ultra, a mode using subagents, not an additional API reasoning value. Use the selected surface's supported controls; do not impose the API effort list on a Codex host or map ultra silently to max.

### Bounded Astra use

A concrete unresolved hard signal can justify direct Astra without a cheaper-model failure: coupled systems, costly-to-reverse decisions, conflicting original evidence, or a difficult question a worker cannot settle. Review-gated stakes alone require review, not a separate Astra consultation. If straightforward and bounded, bypass consultation.

For consultation, parent sends a bounded question, constraints, verified facts, uncertainties, original source pointers (mark missing), and observable acceptance. Astra returns actionable decision, conditions, remaining uncertainty, and checks. Missing evidence that could change decision stays explicit. Consultation is advisory and cannot satisfy required independent review. Reconsult only after material new evidence or a named still-unresolved difficulty; avoid duplicate review.

Before non-exact Astra execution outside the visual/browser floor, record unresolved difficulty, why Sol/Luna is insufficient, scope, effort, and exit condition. For visual/browser execution, record that phase requirement, scope, effort, and exit condition instead. A failed review or several changed files alone does not escalate a whole repair bundle. At exit and each phase boundary, return bounded nonvisual repairs, tests, extraction, and docs without browser interaction to Luna High or Sol Medium when transfer saves cost. Keep Astra for any remaining visual/browser phase, a stated remaining hard problem, exact requirement, or concrete transfer cost. A small final check may remain with current owner if handoff costs more and all capability floors are met. Astra xhigh, max, or ultra requires a lower-Astra-effort failed gate or representative workload evidence; no forced escalation ladder.

## Brief workers

Every worker receives a compact contract:

- Role and one concrete outcome.
- Raw inputs and source pointers, not author conclusions alone.
- Required tools, resource/session access, host, approval flow, and a first-step capability check.
- Requested model/effort and runtime verification status; named reason if an eligible bounded phase bypasses Luna.
- Scope, writer lease, forbidden actions, and subdelegation boundary.
- Acceptance checks and return artifact, evidence, risks, and next action.

Parent checks returned artifact against acceptance and requests substantive repairs from owning worker; routine rewriting for style is unnecessary. Complete focused checks, then broaden testing only for new failures, changes, or unresolved concerns.

## Independent review

Independent review is required, when collaboration is available, for three or more coupled subsystems; changes to model capability floors, fallback authority, or routing enforcement; authentication, authorization, secrets, or security boundaries; transactions or concurrency; schemas or irreversible state; signing-sensitive legal or financial judgment; external publication or deployment; conflicting evidence or reviews; failure that could corrupt durable state or make recovery ambiguous; or an explicit request. Small deterministic low-risk edits and answers do not require it. If a required reviewer is unavailable, report missing gate; do not claim review passed.

Use Luna High for bounded everyday implementation and short-source review, or Medium for focused mechanical inspection with checks. Use Sol Medium for broad synthesis, ambiguous implementation, debugging, and closeout. Use exact frontier-review set [gpt-6-astra] for systems, security, irreversible state, signing-sensitive legal/financial work, publication, deployment, conflicting-evidence review, and changes to model capability floors or fallback authority. Mentioning a model or fixing a typo alone does not trigger frontier review. Sol cannot substitute for this gate.

Reviewer must be a distinct fresh agent, read-only, with raw artifact, base revision, acceptance criteria, and relevant evidence. Consultation author cannot serve as required independent reviewer. Run required reviews sequentially; writer repairs actionable findings; same reviewer or fresh same-tier reviewer rechecks. Parent accepts or rejects findings with evidence. Independent reviewers may use same model as author but cannot be same agent. No self-review.

For an authorized deployment, read [DEPLOYMENT.md](DEPLOYMENT.md) before executing settled release plan. Deployment authorization does not authorize a new conversation.

## Completion

Implementation passes when requested behavior exists, focused checks pass, and unrelated user changes remain untouched. Review passes when findings are fixed and rechecked or rejected with evidence. Final response reports topology actually used, artifacts, checks, missing tools, substitutions or escalation, and remaining risk; for persistent chats include verified IDs/host and requested versus observed settings. Report exact model and effort only when runtime surfaces them. If announced route was not executed, say why.
