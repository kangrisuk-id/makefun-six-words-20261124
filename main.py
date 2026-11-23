# Six Words, One Story — entry program.
# Writes the six-word story to /output/entry.txt.
# The gate allows 1 to 60 characters of UTF-8 text; the judge's first
# criterion is a complete story in exactly six words.

import os

LINE = "Widow remarried Monday. Husband returned Tuesday."


def validate(line: str) -> None:
    # Exactly six words: the judge's first criterion, and a fragment,
    # a slogan or a list loses to any true six-word story.
    words = line.split()
    assert len(words) == 6, f"the story must be six words, not {len(words)}"
    # Inside the gate: 1 to 60 characters of UTF-8, not only whitespace.
    assert 1 <= len(line) <= 60, "the story must fit the 60 character gate"
    assert line == line.strip(), "the story must not carry stray whitespace"
    assert "\n" not in line and "\r" not in line, "the story is one line"
    # Two beats, two sentences: the remarriage, then the return.
    assert line.endswith("."), "the story must end with a full stop"
    assert line.count(".") == 2, "the story is told in two sentences"


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
