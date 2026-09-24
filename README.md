# GPTRelay

Codex skill for coordinating GPT-6 subagents inside the **current task**. This is an opinionated fork of [Forward-Future/gpt-5-6-relay](https://github.com/Forward-Future/gpt-5-6-relay).

GPTRelay keeps user dialogue, scope, routing, tracking, acceptance, and final synthesis with the conversation agent. Substantive ownable coding, research, and long-source extraction go to standard in-process subagents. It uses one worker for a sequential phase and fans out only independent workstreams. It never creates or forks another task or conversation for delegation.

The skill selects Luna, Sol, or Astra with an explicit effort according to expected quality, total cost, and latency per accepted result. It favors independent benchmark evidence and local checks over vendor claims or token prices alone. It preserves one writer per checkout, exact model requirements, and independent review for consequential work. See the [routing policy](.agents/skills/GPTRelay/SKILL.md), dated [model evidence](.agents/skills/GPTRelay/references/model-evidence.md), [cost-quality curves](.agents/skills/GPTRelay/references/cost-curves.md), [AA graph](.agents/skills/GPTRelay/references/aa-cost-quality.png), [Vals graph](.agents/skills/GPTRelay/references/vals-cost-quality.png), and [source points](.agents/skills/GPTRelay/references/cost-curves.json).

## Install

Copy [GPTRelay](.agents/skills/GPTRelay) into a Codex project's .agents/skills directory or your personal Codex skills directory. Use the exact GPTRelay spelling.

For global always-on use, add one instruction to AGENTS.md: “At start of every turn, read and follow ~/.codex/skills/GPTRelay/SKILL.md completely.” Resolve that path to your personal skill location if different.

## Use

Invoke GPTRelay with a concrete task: “Use $GPTRelay to implement and verify this task.”

Collaboration tools must be available for subagent execution and independent review. The conversation agent cannot change its own model or effort through this skill; it reports worker settings only when runtime surfaces them. A requested model/effort is not proof of the actual setting.

The repository also preserves the standalone [agentic-executer](.agents/skills/agentic-executer/SKILL.md) skill from its fork lineage. GPTRelay does not invoke it.

## License

MIT. See [LICENSE](LICENSE). Original project copyright and fork lineage remain in Git history.
