#!/usr/bin/env python3
"""Mark the Chinese counterpart as wording-lagged after the English de-AI pass."""

from __future__ import annotations

import io
import os

ZH = os.path.join(
    r"C:\Users\32597\Documents\Codex\2026-09-15\github\motor-health-monitor-papers",
    "conference-track", "PAPER_v1.0_中文版.md",
)

MARK = ("\n> **同步状态（2026-09-20）**：英文稿随后做过一次 humanizer 去 AI 化改写"
        "（仅词句层面：破折号、同构开场、元话语、超长句、术语统一，并清掉 RB-M2 的两处"
        "「下界当上界」残句）。中文版本文件的数字与主张与之完全一致"
        "（`POLISH_zh_translation_check.txt`），但被改写句子的中文措辞可能略滞后；"
        "下次整体润色时一并刷新。\n")

with io.open(ZH, "r", encoding="utf-8", newline="") as fh:
    text = fh.read()

anchor = "> 数字来源见 `CLAIM_EVIDENCE_MAP.md`；引用见 `REFERENCES.md`；图见 `figures/`。\n"
if "同步状态（2026-09-20）" in text:
    print("  skip: already marked")
else:
    if anchor not in text:
        raise SystemExit("FAIL: header anchor not found")
    text = text.replace(anchor, anchor + MARK, 1)
    with io.open(ZH, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    print("  ok  Chinese counterpart marked as wording-lagged")
