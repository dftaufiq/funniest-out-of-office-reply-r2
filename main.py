import os

# Round 2 resubmit line (135 chars / 135 bytes, single line, ASCII).
# 2-beat + reveal: setup names the cover person, twist lands in the final
# clause ("read none of them"). Specific number (312) + named character
# (Greg) + specific office-truth detail ('noted'). Chosen by internal
# pairwise tournament over 8 new variants: 7-0, then beat the R1 line
# (score 505964, #915 of 1897, below the 500 cut) by margin 2.
LINE = "I'm back Tuesday. Between now and then, my inbox is being handled by Greg, who has replied 'noted' to 312 emails and read none of them."

# Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-160 chars,
# not only whitespace, a single line. Fail loudly instead of shipping an
# invalid entry. ASCII-only is enforced too: the tie-break counts bytes,
# and a non-ASCII character would make bytes exceed the counted chars.
if not LINE.isascii():
    raise SystemExit("entry line must be ASCII so bytes equal chars")
if not 1 <= len(LINE) <= 160 or not LINE.strip() or "\n" in LINE:
    raise SystemExit("entry line violates the 1-160 char single-line gate")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
entry_path = os.path.join(out_dir, "entry.txt")
with open(entry_path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

# Read-back verification: prove the file the grader reads is byte-identical
# to LINE. Fail loudly rather than ship a corrupted or truncated entry.
with open(entry_path, "r", encoding="utf-8", newline="") as f:
    written = f.read()
if written != LINE:
    raise SystemExit(
        f"entry.txt verification failed: read back {len(written)} chars, "
        f"expected {len(LINE)} chars identical to the entry line"
    )

# Byte check: the tie-break counts bytes, so confirm the file on disk is
# exactly the entry's UTF-8 bytes — no trailing newline, no BOM.
if os.path.getsize(entry_path) != len(LINE.encode("utf-8")):
    raise SystemExit("entry.txt byte length does not match the entry line")
print(f"wrote {len(LINE)} chars / {len(LINE.encode('utf-8'))} bytes to {entry_path}")
