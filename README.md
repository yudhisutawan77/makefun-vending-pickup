# Vending Machine Pickup Line

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/yudhisutawan77/makefun-vending-pickup/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/yudhisutawan77/makefun-vending-pickup/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

One line, one minute: a pickup line a vending machine would use on a passing human, entered in the [make.fun bounty](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee).

## The entry

> I only take exact change, but you walked past and I jammed — press B7 and I'll drop the sweetest thing in this row, no coins needed.

132 characters, one line. The machine speaks in its own world — exact change, a jam, button B7, the drop — and waives its own rule for the human who just walked past. The punch lands on the last three words.

## How it works

`main.py` writes the line to `/output/entry.txt` (or to the file path in `ENTRY_OUT` when set), and refuses to write anything over the contest's 200-character limit.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
