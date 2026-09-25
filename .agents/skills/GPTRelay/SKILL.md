---
name: GPTRelay
description: Coordinate work in the current Codex task using GPT-6 in-process subagents. Route substantive ownable work by quality, total accepted-result cost, and latency; keep independent review and one-writer ownership.
---

# GPTRelay

Scope: OpenAI Codex with GPT-6 Astra, Sol, and Luna collaboration subagents. This skill does not route work through other assistants or runtimes.

Keep the current conversation for user dialogue, intent, scope, routing, tracking, acceptance, and final synthesis. Use standard collaboration subagents **within this same task** for substantive ownable technical work, research, and long-source extraction. This skill never creates, forks, or messages another persistent Codex task or conversation for delegation. A user's separate task-management request is outside this router.

Choose route, model, and effort separately. Minimize expected total credits and wall time per accepted result, including tools, coordinator, transfer, retries, repair, and review. Meet quality and risk requirements first. Prioritize reputable independent benchmarks, triangulate across organizations and harnesses, and test local acceptance. Vendor claims, API prices, visible brevity, and model size alone do not prove task savings.

## Route within the task

Apply gates in order:

1. Required independent review. Reserve a distinct fresh read-only reviewer and its model tier.
2. Independent bounded workstreams. Parallelize only when each has separate ownership, evidence, and useful concurrent progress.
3. One in-process worker for a substantive independently ownable phase, including a sequential phase.
4. Parent execution for a small direct fact, a few tool checks, final verification, or a named case where transfer cost exceeds expected benefit or no worker can own the work without losing critical live context.

Do not call a task parent-only merely because work is sequential, a parallel branch is absent, or parent has convenient tools. Prefer one worker for one phase. Fan out only genuinely independent work with clear coordination benefit. Never create a persistent thread to enforce a model or to make work visible. In first commentary, state concrete route and reason.

Parent owns canonical task state, user authority, acceptance, and final answer. Give workers raw paths, URLs, commits, source pages, constraints, and checks. A summary alone cannot replace original sources for material analysis. A Luna extraction worker returns a factual map with precise citations, counterevidence, and coverage unknowns; a Sol synthesis worker receives that map **and raw source pointers**. Parent assesses source quality and verifies claims before acceptance. Workers return difficult questions or review needs to parent, not a private agent tree.

Use prompt-only or few-turn forks for independent work. Full-history forks only when entire conversation is necessary and inherited settings suffice. A delegated worker may not subdelegate unless explicitly authorized by parent and ownership remains clear. Do not use multiple workers on a tightly sequential shared-state chain or overlapping writes.

All collaboration agents share the filesystem. Exactly one automated mutating owner holds a checkout at a time, counting parent and descendants. Parent performs no writes while a worker holds that lease. A second writer requires a separate worktree; isolate ports, databases, processes, and generated outputs too, or serialize writes. Before lease, snapshot branch, revision, status, and dirty paths; declare owned paths and pause integration on unexpected drift. Read-only reviewer gets no writer lease. A worktree is directory isolation, not a new task.

## Model and effort

The user selects conversation model in the app. This skill cannot switch current parent model or effort. If no runtime control exposes them, report _inherited, not surfaced_ once; never claim a requested worker route was executed without evidence. Child routing does not lower parent cost. Keep coordinator compact and route ownable execution to workers. An explicit user or project model/effort requirement stays exact. If an external exact requirement names a legacy model, ask its owner rather than silently substituting GPT-6.

Use these provisional **GPT-6-only** starting points when local comparable evidence is absent:

| Model | Starting work | Effort |
| --- | --- | --- |
| Luna (gpt-6-luna) | Deterministic bulk extraction, source maps, focused repeatable coding and checks | Medium for mechanical volume with sampled checks; High for focused coding or synthesis. xhigh requires named failed check or relevant workload evidence. |
| Sol (gpt-6-sol) | Broad/default clear coding, agentic tools, multi-source synthesis, ordinary ambiguity | Medium; High for a named difficulty or failed acceptance. |
| Astra (gpt-6-astra) | Named hard diagnosis, coupled systems, conflicting evidence, difficult multistep judgment, frontier review | Medium for hard judgment; High for named hard execution; Low when evidence supports it. xhigh or above requires lower-Astra-effort failure or relevant workload evidence. |

These are workload hypotheses, not universal rankings. Select an operating point (model **and** effort) by first enforcing task quality, capability, and independent-review gates; then compare relevant workload evidence for total accepted-result cost and wall time. Compare plausible points directly rather than climbing a fixed cheap-to-expensive ladder. Sol Low is a latency candidate for bounded work; Luna xhigh/max can be quality candidates when their extra reasoning meets a named check at acceptable latency. Astra Low is a candidate for a named hard problem when Sol High/Max would spend much longer reasoning and the relevant workload supports it. Preserve the bounded-Astra requirement below. Aggregate scores alone never change a floor or prove local acceptance.

For dated evidence, operating-point curves, limitations, and sources, read [references/model-evidence.md](references/model-evidence.md) and [references/cost-curves.md](references/cost-curves.md) when comparing or changing routes. Keep API dollars and Codex credits separate. Refresh when availability/pricing changes or observed acceptance invalidates a route; do not browse every routine turn. If routes remain uncertain, calibrate representative tasks with actual model/effort, acceptance, wall time, and **total** spend including parent, review, retries, and repair; compare within a task class and keep units separate.

Use model and effort options surfaced by selected collaboration tool and host. Full-history forks inherit settings; explicit overrides require prompt-only or limited-history forks when tool schema permits. Preserve actual or _inherited, not surfaced_ in handoffs. For non-exact work only: if Luna unavailable, consider Sol then Astra; if Sol unavailable, consider Astra, or Luna only after reclassifying as bounded with equivalent checks; if Astra unavailable, Sol may handle ordinary reclassified execution, but an exact Astra or frontier-review gate remains missing. Never silently lower a capability floor. None, minimal, and ultra are not universal effort options; use only exposed values. Higher effort is not automatically better.

### Bounded Astra use

A concrete unresolved hard signal can justify direct Astra without a cheaper-model failure: coupled systems, costly-to-reverse decisions, conflicting original evidence, or a difficult question a worker cannot settle. Review-gated stakes alone require review, not a separate Astra consultation. If straightforward and bounded, bypass consultation.

For consultation, parent sends a bounded question, constraints, verified facts, uncertainties, original source pointers (mark missing), and observable acceptance. Astra returns actionable decision, conditions, remaining uncertainty, and checks. Missing evidence that could change decision stays explicit. Consultation is advisory and cannot satisfy required independent review. Reconsult only after material new evidence or a named still-unresolved difficulty; avoid duplicate review.

Before non-exact Astra execution, record unresolved difficulty, why Sol/Luna is insufficient, scope, effort, and exit condition. A failed review or several changed files alone does not escalate a whole repair bundle. At exit and each phase boundary, return bounded repairs, tests, extraction, and docs to Luna High or Sol Medium when transfer saves cost. Keep Astra only for a stated remaining hard problem, exact requirement, or concrete transfer cost. A small final check may remain with current owner if handoff costs more. Astra xhigh, max, or ultra requires a lower-Astra-effort failed gate or representative workload evidence; no forced escalation ladder.

## Brief workers

Every worker receives a compact contract:

- Role and one concrete outcome.
- Raw inputs and source pointers, not author conclusions alone.
- Requested model/effort and runtime verification status.
- Scope, writer lease, forbidden actions, and subdelegation boundary.
- Acceptance checks and return artifact, evidence, risks, and next action.

Parent checks returned artifact against acceptance and requests substantive repairs from owning worker; routine rewriting for style is unnecessary. Complete focused checks, then broaden testing only for new failures, changes, or unresolved concerns.

## Independent review

Independent review is required, when collaboration is available, for three or more coupled subsystems; changes to model capability floors, fallback authority, or routing enforcement; authentication, authorization, secrets, or security boundaries; transactions or concurrency; schemas or irreversible state; signing-sensitive legal or financial judgment; external publication or deployment; conflicting evidence or reviews; failure that could corrupt durable state or make recovery ambiguous; or an explicit request. Small deterministic low-risk edits and answers do not require it. If a required reviewer is unavailable, report missing gate; do not claim review passed.

Use Luna High for bounded everyday implementation and short-source review, or Medium for focused mechanical inspection with checks. Use Sol Medium for broad synthesis, ambiguous implementation, debugging, and closeout. Use exact frontier-review set [gpt-6-astra] for systems, security, irreversible state, signing-sensitive legal/financial work, publication, deployment, conflicting-evidence review, and changes to model capability floors or fallback authority. Mentioning a model or fixing a typo alone does not trigger frontier review. Sol cannot substitute for this gate.

Reviewer must be a distinct fresh agent, read-only, with raw artifact, base revision, acceptance criteria, and relevant evidence. Consultation author cannot serve as required independent reviewer. Run required reviews sequentially; writer repairs actionable findings; same reviewer or fresh same-tier reviewer rechecks. Parent accepts or rejects findings with evidence. Independent reviewers may use same model as author but cannot be same agent. No self-review.

For an authorized deployment, read [DEPLOYMENT.md](DEPLOYMENT.md) before executing settled release plan. Deployment authorization does not authorize a new conversation.

## Completion

Implementation passes when requested behavior exists, focused checks pass, and unrelated user changes remain untouched. Review passes when findings are fixed and rechecked or rejected with evidence. Final response reports topology actually used, artifacts, checks, substitutions or escalation, and remaining risk. Report exact model and effort only when runtime surfaces them. If announced route was not executed, say why.
