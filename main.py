"""One-Line Office Jokes — a make.fun entry.

Prints exactly one single line that makes office life funny, with the
laugh landing in the last few words.
"""

LINE = (
    "The reply-all button has ended more office friendships than "
    "the last slice of office birthday cake."
)


def build_line() -> str:
    line = LINE
    assert len(line) <= 200, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
