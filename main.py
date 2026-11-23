#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes — entry program.

Writes one office joke (a single line, under 200 characters) to
/output/entry.txt. Python 3.13 standard library only; deterministic;
no network, no randomness, no environment input beyond the output
directory override used for local testing.
"""

import os
from pathlib import Path

# Chosen joke (candidate 7 of 10, revised after self-critique): the reply-all
# spiral. The fix for the problem becomes the problem, and the punchline
# escalates it onto the speaker — I am now the subject of the meeting.
# Triple "reply-all" mirrors the storm itself. v1 said "hit reply-all ...
# a meeting about my email"; v2 tightens the verb and lands the
# consequence on the speaker.
JOKE = "I replied-all asking everyone to stop replying-all, and now I'm the subject of a meeting about reply-all."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = JOKE.strip()
    assert 1 <= len(text) <= 199, f"joke must be 1-199 chars, got {len(text)}"
    assert "\n" not in text, "joke must be a single line"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
