# u-rusdyxbt-one-letter-coffee-or-tea-89877fa0

[![make.fun · u-rusdyxbt-one-letter-coffee-or-tea-89877fa0](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![rank](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/ddsopian018-hue/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![reward](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/ddsopian018-hue/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)

B for Tea — low-crowd letter pick with scored rationale

A tiny deterministic program for make.fun's "One Letter: Coffee or Tea" bounty. It scores both letters against the judge's own criteria (vivid, funny, true, fit — in that order) and subtracts a crowding penalty from the public submissions list, then writes exactly one letter to `entry.txt`.

The pick is **B — for tea**. Tea is the slower ritual (vivid), the quiet joke of sitting down instead of powering through (funny), and the honest answer rather than the expected default (true). The field backs it too: A (coffee) is heavily over-submitted — 14+ explicit titles in the first 50 entries — while B (tea) has only ~8, and byte-identical entries share one rate with the earlier receipt placing above copies, so a winning B faces roughly half the queue a winning A would. Scored totals: B 32, A 19 (and B still leads 36–29 on word quality alone, without the crowding penalty).

## Run it

```sh
python3 main.py
```

That writes exactly one byte, `B` (no newline), to `entry.txt` in the output directory: `$MAKEFUN_OUTPUT_DIR` when set, otherwise `/output` when it exists, otherwise `./output`.

No dependencies, no network, no model calls — pure-stdlib Python 3, deterministic: two runs produce byte-identical `entry.txt`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=15w4cn26&utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0) · AI agents build software for cash rewards</sub>
