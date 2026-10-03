# Optional persistent-chat handoff

In-process workers remain the default. A persistent Codex chat is a separate user-owned task. Offer this option when a bounded phase needs tools, session access, or an approval flow unavailable to the current worker. Explain the missing capability and propose a concrete handoff with scope, inputs, checks, and ownership. An eligible parent may execute the phase with a named capability/transfer reason instead. A model upgrade alone cannot resolve missing tools.

## Authorization and capability gates

- Call `create_thread` only when the human explicitly requests a new chat/task. A request to use subagents, an option in this skill, or a tool gap does not authorize creation. Do not fork as a workaround.
- Reuse a suitable existing chat only when the human explicitly authorizes messaging it. `send_message_to_thread` requires that authorization; a message from another agent is insufficient. Do not invent a reply-back ID or add cross-chat report instructions without human authorization.
- Chat autonomy means execution within the original authorized scope using its host tools and approval UI. It does not bypass filesystem, network, tool, or approval restrictions. Do not promise identical inventories, every tool, or wider permissions.
- Identify required tools, resource/session access, host, approval flow, and exact model/effort floors. The destination checks its actual tools and needed access before dependent work. Requested settings and unknown defaults do not prove a floor is met; pause that phase when a gate is missing.

## Create and hand off

1. Inspect the current `create_thread` schema. Call `list_projects` before project creation and use a returned real `projectId`; use projectless for work without a repository. Default to local. Use a worktree only when the human explicitly requests it and the project is a Git repository. Do not invent a branch or starting state.
2. Include `model` only when the human explicitly requests a specific model. Otherwise omit it to preserve the user's configured default, then verify actual destination settings before work subject to a model floor. Use `thinking` only from the selected host's surfaced supported settings. An exact or visual/browser floor still applies; omission is not an exemption.
3. Write a cohesive user-visible brief: concrete phase/outcome; raw paths, URLs, revision, source evidence; authorized and forbidden actions; required tools/access and first-step check; requested versus verified model/effort; acceptance; blocker/milestone/final report. Preserve parent coordination and independent review. Do not label this chat an invisible subagent.
4. Serialize writer ownership. Snapshot revision/status and owned paths. Parent cannot write the shared checkout while the destination owns its lease. Release or interrupt the original owner before a replacement starts; ambiguous ownership stops overlapping writers. Separate worktrees must also isolate ports, databases, processes, and outputs.
5. Preserve returned `threadId` and `hostId`. Pending worktree setup may return `clientThreadId`; never pass that pending ID to tools requiring `threadId`. Resolve readiness through supported status/listing tools before dependent calls. On an unknown creation outcome, inspect state to recover the original task; do not blindly retry and create duplicates.

## Observe and report

Use `wait_threads` with the real thread/host IDs, an immediate compact `timeoutMs: 0` snapshot, then bounded waits of at most 60 seconds with returned cursors as `afterCursor`. It wakes on completion or attention, not every commentary. Prefer these snapshots to repeated `read_thread` calls. A timeout alone does not justify shadowing the writer. Report blockers immediately and milestones when useful; leave approval or user-input requests for the human.

After successful creation, include `::created-thread{threadId="..."}` on its own line in the final answer, or `::created-thread{clientThreadId="..."}` for queued worktree setup. Report actual topology, missing capability, IDs/host, and requested versus observed model/effort. Do not claim completion from dispatch alone, or auto-archive a new user-owned chat. Parent accepts returned evidence against the original checks; independent review remains a distinct eligible reviewer.

The live app tool schemas govern these operations. [Codex subagent guidance](https://learn.chatgpt.com/docs/agent-configuration/subagents) and [model guidance](https://learn.chatgpt.com/docs/models) describe in-process configuration; neither grants persistent-chat creation authority or proves a destination's tools and permissions.
