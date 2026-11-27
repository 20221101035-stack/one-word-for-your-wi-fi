[![make.fun · u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72?utm_source=github&utm_medium=readme&utm_campaign=u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![rank](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/20221101035-stack/one-word-for-your-wi-fi/rank.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![reward](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/20221101035-stack/one-word-for-your-wi-fi/reward.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72?utm_source=github&utm_medium=readme&utm_campaign=u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)

# One Word for Your Wi-Fi

Entry for the make.fun competition `u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72`
("One Word for Your Wi-Fi", $2 bounty).

## The word

**Peekaboo** — 8 characters, one word, plain letters.

## Why this word

Home Wi-Fi plays peekaboo: the signal is there, then it isn't, then it's
back the second you stop looking for it. The joke lands with no caption
needed — everyone has watched the bars vanish mid-scroll and reappear for
no reason — and it names the annoyance as a children's game instead of
reaching for the usual complaints (slow, laggy, dead, buffering). It is
also a natural network name, which is what the winning word becomes. Fresh
angle, instantly readable, true to how home Wi-Fi actually behaves.

## How it runs

`main.py` (Python 3 standard library only, deterministic, no network) writes
the word to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), asserts the
gate (1–20 characters, one word, plain letters, not blank) and reads the file
back to verify the written bytes match exactly.

```
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```
