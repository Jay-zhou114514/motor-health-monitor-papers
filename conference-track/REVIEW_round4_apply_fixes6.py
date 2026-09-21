#!/usr/bin/env python3
"""Sixth pass: repair hyphen-broken URLs in the availability paragraph and re-wrap it."""

from __future__ import annotations

import io
import os
import textwrap

TRACK = r"<WORKDIR>\Documents\Codex\2026-09-15\github\motor-health-monitor-papers\conference-track"
PAPER = os.path.join(TRACK, "PAPER_v1.0_submission-draft.md")

START = "The experiment registry, preregistrations, scripts, run logs, per-fold CSVs,"
END = "maintained in `docs/AI_USE_DISCLOSURE.md`."

with io.open(PAPER, "r", encoding="utf-8", newline="") as fh:
    paper = fh.read()

start = paper.index(START)
end = paper.index(END) + len(END)
paragraph = " ".join(paper[start:end].split())

for broken, fixed in (
    ("motor-health-monitor- papers", "motor-health-monitor-papers"),
    ("motor- health-monitor", "motor-health-monitor"),
    ("working- tree", "working-tree"),
):
    while broken in paragraph:
        paragraph = paragraph.replace(broken, fixed)
        print(f"  ok  repaired {broken!r}")

checks = [
    "github.com/<ACCOUNT>/motor-health-monitor`",
    "github.com/<ACCOUNT>/motor-health-monitor-papers`",
    "an internal working-tree document",
]
for check in checks:
    if check not in paragraph:
        raise SystemExit(f"FAIL: {check!r} not intact")
if "- " in paragraph:
    idx = paragraph.index("- ")
    raise SystemExit(f"FAIL: hyphen-space remains near: {paragraph[idx - 40: idx + 40]!r}")

wrapped = "\n".join(textwrap.wrap(paragraph, width=100,
                                  break_long_words=False, break_on_hyphens=False))
paper = paper[:start] + wrapped + paper[end:]
with io.open(PAPER, "w", encoding="utf-8", newline="") as fh:
    fh.write(paper)
print("sixth pass applied")
