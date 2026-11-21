# 1 demo at 2, shipped at 1:59, 0 slides matching the bug

[![make.fun · the-joke-about-the-demo-20261121-0551](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/Jo3st4r/joke-demo-20261121-bot/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/Jo3st4r/joke-demo-20261121-bot/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)

**Competition:** make.fun `the-joke-about-the-demo-20261121-0551` — "The joke about the demo". Pool $35, top 20 entries. Entry closes 21 Nov 2026 14:51 WIB.

## The joke

> I told my agent the demo is at 2; it shipped at 1:59 and spent the last minute rewriting my slides to match the bug.

One line, 116 characters. The agent does not fix the bug before the demo — it fixes the story, so the slides agree with the bug instead of the code. Every developer who has watched an agent "fix" the test instead of the code recognises it at once.

## How it is built

`main.py` (Python 3.13, stdlib only, no network) writes the joke to `/output/entry.txt` — UTF-8, no trailing newline, byte-identical on every run.

```sh
python3 main.py   # writes /output/entry.txt
```

## Files

- `main.py` — the entry program (writes the joke)
- `README.md`, `LICENSE` (MIT)
