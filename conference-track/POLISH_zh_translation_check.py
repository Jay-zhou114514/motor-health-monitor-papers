#!/usr/bin/env python3
"""Number-set comparison between the English manuscript and its Chinese counterpart.

Faithful translation of a quantitative paper means every printed number survives. This script
compares the multisets of numeric tokens in the two files and reports any asymmetry.
"""

from __future__ import annotations

import io
import os
import re
from collections import Counter

TRACK = r"<WORKDIR>\Documents\Codex\2026-09-15\github\motor-health-monitor-papers\conference-track"
EN = os.path.join(TRACK, "PAPER_v1.0_submission-draft.md")
ZH = os.path.join(TRACK, "PAPER_v1.0_中文版.md")

NUMBER = re.compile(r"\d+(?:[.,]\d+)?")


def numbers(path):
    with io.open(path, "r", encoding="utf-8", newline="") as fh:
        text = fh.read()
    # drop the repository/URL and hash-like tokens that are not paper quantities
    text = re.sub(r"github\.com/\S+|EXP-[Vv][12]-\d+\S*|`[^`]*`", " ", text)
    return Counter(NUMBER.findall(text))


en = numbers(EN)
zh = numbers(ZH)

missing_in_zh = en - zh
extra_in_zh = zh - en

print(f"distinct numeric tokens: en={len(en)} zh={len(zh)}")
print(f"total numeric tokens:    en={sum(en.values())} zh={sum(zh.values())}")

print("\n### present in English, fewer in Chinese")
for token, count in sorted(missing_in_zh.items(), key=lambda kv: -kv[1])[:40]:
    print(f"  {token:<12} en={en[token]} zh={zh.get(token, 0)}   (en-only count {count})")

print("\n### present in Chinese, fewer in English")
for token, count in sorted(extra_in_zh.items(), key=lambda kv: -kv[1])[:40]:
    print(f"  {token:<12} zh={zh[token]} en={en.get(token, 0)}   (zh-only count {count})")

print("\ntranslation check complete")
