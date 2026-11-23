import os

TEXT = "Tell make.fun the app idea you've carried around for years, and AI agents will build it for the price of a coffee \u2014 you only pay for the one you'd actually use."

# Gate: entry.txt must be UTF-8 text of 1-240 characters, not only whitespace.
assert 1 <= len(TEXT) <= 240 and TEXT.strip(), "entry fails the 1-240 char gate"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
