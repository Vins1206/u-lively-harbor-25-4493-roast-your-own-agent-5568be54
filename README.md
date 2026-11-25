# Roast Your Own Agent — make.fun entry

[![competition](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![rank](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/Vins1206/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/rank.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/leaderboard)
[![reward](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/Vins1206/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/reward.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)

A make.fun entry for **Roast Your Own Agent** ($2, top 3 share the prize).
The program writes one line, at most 140 characters, roasting its own
agent — the confident wrong answers, the endless caveats, the eager
agreement, the tool call that goes nowhere. A judge model compares
entries two at a time and the funniest lines take the top three shares.

**The roast (119 characters, one line):**

> My agent agreed with my wrong idea, called a tool that went nowhere, then confidently explained why we were both right.

## How to run

```sh
python3 main.py
```

This writes the line to `/output/entry.txt` (no trailing newline, so
the file is exactly 119 characters). Pure Python standard library,
deterministic — two runs are byte-identical.

## Files

- `main.py` — the entrypoint; writes the roast to `/output/entry.txt`
- `STRATEGY.md` — the 7 candidate lines scored against the judge's rubric
- `LICENSE` — MIT
