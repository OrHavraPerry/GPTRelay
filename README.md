# GPTRelay

Codex skill for coordinating GPT-6 subagents inside the **current task**. Adapted from [Forward-Future/gpt-5-6-relay](https://github.com/Forward-Future/gpt-5-6-relay) for OpenAI Codex.

GPTRelay keeps user dialogue, scope, routing, tracking, acceptance, and final synthesis with the conversation agent. Substantive ownable coding, research, and long-source extraction go to standard in-process subagents. It uses one worker for a sequential phase and fans out only independent workstreams. An optional persistent chat requires an explicit human request for a new chat/task; it is a user-owned task, with destination capabilities verified before dependent work. See [persistent-chat handoff](.agents/skills/GPTRelay/references/persistent-chat.md).

The skill checks required tools, resource/session access, and approval flow before choosing an owner. Eligible bounded nonvisual extraction, classification, data processing, inventories, formatting, focused coding, tests, and docs default to Luna: Medium for mechanical volume, High for focused coding/synthesis. Sol needs a named ambiguity, coupling, failed check, exact requirement, or verified capability/evidence exception. Reassess at each phase boundary; a stronger model does not replace a missing tool. Non-exact Sol routes use `gpt-6.1-sol` when surfaced, with an explicit `gpt-6-sol` availability fallback; exact model requests remain exact. It favors independent benchmark evidence and local checks over vendor claims or token prices alone. It preserves one writer per checkout and independent review for consequential work. See the [routing policy](.agents/skills/GPTRelay/SKILL.md), [task-specific benchmark evidence](.agents/skills/GPTRelay/references/task-benchmarks-2026-10-03.md), current [GPT-6.1 Sol evidence](.agents/skills/GPTRelay/references/gpt-6.1-sol-evidence.md), historical [GPT-6 model evidence](.agents/skills/GPTRelay/references/model-evidence.md), historical [cost-quality curves](.agents/skills/GPTRelay/references/cost-curves.md), [AA graph](.agents/skills/GPTRelay/references/aa-cost-quality.png), [Vals graph](.agents/skills/GPTRelay/references/vals-cost-quality.png), and [source points](.agents/skills/GPTRelay/references/cost-curves.json).

User routing policy: visual creation, inspection, judgment, and all browser interactions require `gpt-6-astra` at least Light (`low`), including routine actions. No Sol/Luna fallback for those phases; text/API research and nonvisual coding retain ordinary routes. Higher effort follows task difficulty. This floor does not replace required independent review or switch the conversation model.

## Install

Copy the entire [GPTRelay skill directory](.agents/skills/GPTRelay) to your project's `.agents/skills/GPTRelay` or your personal `~/.codex/skills/GPTRelay`. Keep its `references/` and `scripts/` directories with `SKILL.md`.

For global always-on use, add one instruction to AGENTS.md: “At start of every turn, read and follow ~/.codex/skills/GPTRelay/SKILL.md completely.” Resolve that path to your personal skill location if different.

## Use

Invoke GPTRelay with a concrete task: “Use $GPTRelay to implement and verify this task.”

Collaboration tools must be available for subagent execution and independent review. The conversation agent cannot change its own model or effort through this skill; it reports worker settings only when runtime surfaces them. A requested model/effort is not proof of the actual setting. Persistent-chat creation does not guarantee all tools or wider permissions; verify actual destination capabilities and preserve model floors. Creating this option does not authorize opening chats, messaging another chat, experimental runs, or automatic archival.

## License

MIT. See [LICENSE](LICENSE). Original project copyright and fork lineage remain in Git history.
