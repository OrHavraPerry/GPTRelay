# GPTRelay

Codex skill for coordinating GPT-6 subagents inside the **current task**. Adapted from [Forward-Future/gpt-5-6-relay](https://github.com/Forward-Future/gpt-5-6-relay) for OpenAI Codex.

GPTRelay keeps user dialogue, scope, routing, tracking, acceptance, and final synthesis with the conversation agent. Substantive ownable coding, research, and long-source extraction go to standard in-process subagents. It uses one worker for a sequential phase and fans out only independent workstreams. It never creates or forks another task or conversation for delegation.

The skill selects Luna, Sol, or Astra with an explicit effort according to expected quality, total cost, and latency per accepted result. Non-exact Sol routes use `gpt-6.1-sol` when surfaced, with an explicit `gpt-6-sol` availability fallback; exact model requests remain exact. It favors independent benchmark evidence and local checks over vendor claims or token prices alone. It preserves one writer per checkout and independent review for consequential work. See the [routing policy](.agents/skills/GPTRelay/SKILL.md), current [GPT-6.1 Sol evidence](.agents/skills/GPTRelay/references/gpt-6.1-sol-evidence.md), historical [GPT-6 model evidence](.agents/skills/GPTRelay/references/model-evidence.md), historical [cost-quality curves](.agents/skills/GPTRelay/references/cost-curves.md), [AA graph](.agents/skills/GPTRelay/references/aa-cost-quality.png), [Vals graph](.agents/skills/GPTRelay/references/vals-cost-quality.png), and [source points](.agents/skills/GPTRelay/references/cost-curves.json).

User routing policy: visual creation, inspection, judgment, and all browser interactions require `gpt-6-astra` at least Light (`low`), including routine actions. No Sol/Luna fallback for those phases; text/API research and nonvisual coding retain ordinary routes. Higher effort follows task difficulty. This floor does not replace required independent review or switch the conversation model.

## Install

Copy the entire [GPTRelay skill directory](.agents/skills/GPTRelay) to your project's `.agents/skills/GPTRelay` or your personal `~/.codex/skills/GPTRelay`. Keep its `references/` and `scripts/` directories with `SKILL.md`.

For global always-on use, add one instruction to AGENTS.md: “At start of every turn, read and follow ~/.codex/skills/GPTRelay/SKILL.md completely.” Resolve that path to your personal skill location if different.

## Use

Invoke GPTRelay with a concrete task: “Use $GPTRelay to implement and verify this task.”

Collaboration tools must be available for subagent execution and independent review. The conversation agent cannot change its own model or effort through this skill; it reports worker settings only when runtime surfaces them. A requested model/effort is not proof of the actual setting.

## License

MIT. See [LICENSE](LICENSE). Original project copyright and fork lineage remain in Git history.
