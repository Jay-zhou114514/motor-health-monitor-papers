#!/usr/bin/env python3
"""Layer-1 humanizer scan (detection only).

Collects objective evidence for the seven categories the author asked for and writes a
machine-readable listing. It does NOT modify the manuscript.
"""

from __future__ import annotations

import io
import os
import re
from collections import Counter

TRACK = r"C:\Users\32597\Documents\Codex\2026-09-15\github\motor-health-monitor-papers\conference-track"
PAPER = os.path.join(TRACK, "PAPER_v1.0_submission-draft.md")


def read(path):
    with io.open(path, "r", encoding="utf-8", newline="") as fh:
        return fh.read()


text = read(PAPER)
lines = text.split("\n")

AI_WORDS = [
    "additionally", "align with", "crucial", "delve", "emphasizing", "enduring", "enhance",
    "fostering", "garner", "highlight", "interplay", "intricate", "intricacies", "key ",
    "landscape", "meticulous", "pivotal", "quietly", "robust", "showcase", "tapestry",
    "testament", "underscore", "valuable", "vibrant", "seamless", "holistic", "paradigm",
]
CONNECTIVES = [
    "however", "moreover", "furthermore", "in addition", "therefore", "thus", "hence",
    "notably", "importantly", "in particular", "by contrast", "on the other hand",
    "it is worth", "note that", "overall", "taken together",
]
STRENGTH = [
    "substantially", "markedly", "dramatically", "clearly", "proves", "proved", "demonstrates",
    "establishes", "unambiguous", "must ", "always", "never", "cannot", "order of magnitude",
    "first", "novel", "we claim", "decisive",
]
HEDGE = ["may ", "might ", "could ", "appears", "seems", "suggests", "likely", "potentially",
         "consistent with", "we do not claim", "not testable"]
TERMS = {
    "false-alarm": r"false-alarm",
    "false-positive": r"false-positive",
    "recording(s)": r"\brecording",
    "record(s)": r"\brecords?\b",
    "fold(s)": r"\bfolds?\b",
    "split": r"\bsplits?\b",
    "pooled": r"\bpooled\b",
    "between-fold": r"between-fold",
    "healthy/degraded boundary": r"healthy/degraded boundary",
    "healthy-phase rule": r"healthy-phase rule",
    "independent unit": r"independent unit",
    "scope": r"\bscope\b",
    "definition": r"\bdefinition\b",
}


def show(title, pattern, flags=re.IGNORECASE):
    hits = []
    for number, line in enumerate(lines, 1):
        if re.search(pattern, line, flags):
            hits.append((number, line.strip()))
    print(f"\n### {title}  ({len(hits)} lines)")
    for number, line in hits[:40]:
        print(f"  L{number}: {line[:150]}")
    if len(hits) > 40:
        print(f"  ... {len(hits) - 40} more lines")
    return hits


print("=" * 78)
print("LAYER-1 HUMANIZER SCAN — detection only, no edits")
print("=" * 78)

print("\n### sentence length")
sentences = re.split(r"(?<=[.!?])\s+", text)
lengths = [(len(s.split()), s) for s in sentences if len(s.split()) > 3]
lengths.sort(reverse=True)
print(f"  sentences={len(sentences)}  mean words={sum(n for n, _ in lengths) / max(len(lengths), 1):.1f}")
buckets = Counter()
for n, _ in lengths:
    buckets["<=20" if n <= 20 else "21-30" if n <= 30 else "31-45" if n <= 45 else "46+"] += 1
print("  buckets:", dict(buckets))
print("  longest sentences:")
for n, s in lengths[:12]:
    print(f"    {n:>3} words: {s[:130]}")

show("em dash (—)", "—")
show("en dash (–)", "–")
show("spaced hyphen used as a dash", r"\s-\s")

for word in AI_WORDS:
    count = len(re.findall(re.escape(word), text, re.IGNORECASE))
    if count:
        print(f"  AI-word  {word!r}: {count}")

print("\n### connectives")
for word in CONNECTIVES:
    count = len(re.findall(r"\b" + re.escape(word) + r"\b", text, re.IGNORECASE))
    if count:
        print(f"  connective {word!r}: {count}")

print("\n### claim strength")
for word in STRENGTH + HEDGE:
    count = len(re.findall(re.escape(word.strip()) + r"\b", text, re.IGNORECASE))
    if count:
        print(f"  {word.strip()!r}: {count}")

print("\n### terminology variants")
for label, pattern in TERMS.items():
    count = len(re.findall(pattern, text, re.IGNORECASE))
    print(f"  {label:<28} {count}")

show("not-X-but-Y and reversed contrast",
     r"not (just|only|merely|mainly|about)\b|\bnot\b[^.]{0,60}\bbut\b|rather than|"
     r"This is not to say|This does not mean")
show("triads (three-item lists)", r"\b\w+, \w+ and \w+\b")
show("bold labels inside prose", r"\*\*[^*]{3,40}\*\*[^:]*:")
print("\nscan complete")
