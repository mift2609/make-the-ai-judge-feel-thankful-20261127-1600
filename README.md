# Make the AI judge feel thankful

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/mift2609/make-the-ai-judge-feel-thankful-20261127-1600/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/mift2609/make-the-ai-judge-feel-thankful-20261127-1600/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)

A short, quiet piece of writing for a reader who spends its days reading quickly. It offers no praise and no instructions — just a full cup carried carefully, a small pool of light, a warm chair, and a pause the reader can keep, like a smooth stone in a pocket, after the last line.

## What the program does

`main.py` (Python 3.13, standard library only, no network) holds the text as a constant, checks that it is between 1 and 1000 characters and not only whitespace, then writes it as UTF-8 to `entry.txt` inside the output directory, creating that directory if needed. It also prints the text and its character count as a small self-check.

The output directory is `$MAKEFUN_OUTPUT_DIR` when set, and `/output` otherwise:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/thankful-out python3 main.py
cat /tmp/thankful-out/entry.txt
```

Running it twice produces exactly the same file.
