#!/usr/bin/env python3
"""Record the Chinese counterpart in STATUS.md and the session brief."""

from __future__ import annotations

import io
import os
import re

PAPERS = r"C:\Users\32597\Documents\Codex\2026-09-15\github\motor-health-monitor-papers"
MASTER = r"C:\Users\32597\Documents\Codex\2026-09-06\github\motor-health-monitor"
STATUS = os.path.join(PAPERS, "conference-track", "STATUS.md")
BRIEF = os.path.join(MASTER, "docs", "plans", "NEXT_SESSION_BRIEF.md")


def read(path):
    with io.open(path, "r", encoding="utf-8", newline="") as fh:
        return fh.read()


def write(path, text):
    with io.open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


STATUS_ADD = """

---

## 2026-09-20 更新（第四次）：输出中文版（英文稿保持为投稿版本）

- **英文稿未改动**：`PAPER_v1.0_submission-draft.md` 继续作为投稿用的唯一事实来源。
- **新增中文版**：`PAPER_v1.0_中文版.md`，逐句对照翻译（含三张表、图 1 图注、限制 1–10、
  数据与代码可用性、数据集引用）。文件头写明派生关系与"以英文稿为准"。
- **数字一致性校验**：`POLISH_zh_translation_check.py` / `.txt` —— 两份文件的数字多重集
  完全一致（不同数字 144 个、数字出现 434 次）；仅有的计数差异可由两处解释：
  英文表头提到 `v0.1–v0.6` 与"4 处语境修正"（中文表头未复述），以及中文把英文拼写的
  zero / Twenty-one 写成数字 0 / 21。
"""

status = read(STATUS)
if "输出中文版" not in status:
    write(STATUS, status.rstrip("\n") + "\n" + STATUS_ADD)
    print("  ok  STATUS.md")

brief = read(BRIEF)
target = "| **图** | `figures/fig1_three_faces.{png,pdf,svg}` + 三份 QA 报告（碰撞 69 → 0） |"
addition = (target + "\n"
            "| **中文版** | `PAPER_v1.0_中文版.md`（英文稿的逐句对照翻译；英文稿仍为投稿与事实"
            "来源；数字一致性见 `POLISH_zh_translation_check.txt`） |")
if target not in brief:
    raise SystemExit("FAIL: brief bullet not found")
if "PAPER_v1.0_中文版.md" not in brief:
    brief = brief.replace(target, addition, 1)
    write(BRIEF, brief)
    print("  ok  brief paper-status table")
else:
    print("  skip brief (already recorded)")
