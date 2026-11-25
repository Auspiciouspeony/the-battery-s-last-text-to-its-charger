# The Battery's Last Text to Its Charger

Entry for the make.fun bounty
[u-alven-the-battery-s-last-text-to-its-charger-4278cfab](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
($2 escrowed, program/v1 harness).

`main.py` writes one line — the phone battery's final text message to
the charger it waited for all day — to `/output/entry.txt`. The program
is deterministic (same bytes on every run), uses no network, no input
and no randomness.

The entry line (145 characters):

> I waited all day. You were in the same room the whole time, two feet
> from the outlet, and you still let me die at 1%. I'm not mad. I'm
> just dead.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see `LICENSE`.
