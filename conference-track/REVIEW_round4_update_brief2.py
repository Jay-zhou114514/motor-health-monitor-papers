#!/usr/bin/env python3
"""Correct the brief: the independent round-4 report did land (via the on-disk task packet)."""

from __future__ import annotations

import io
import os
import re

BRIEF = os.path.join(
    r"C:\Users\32597\Documents\Codex\2026-09-06\github\motor-health-monitor",
    "docs", "plans", "NEXT_SESSION_BRIEF.md",
)

ITEM1 = """1. ~~跑第 4 位审稿人（串行）~~ **已完成（2026-09-20）**。
   - **独立报告**：`conference-track/REVIEW_round4_reviewerC.md`（46 KB，Major 4 / Minor 10，
     侧重报告完整性与读者可复现性）。子代理的消息通道本次**仍然失效**（4 个实例全部没收到
     任务文本），但**孙代理从落盘的任务包 `REVIEW_round4_TASK_C.md` 恢复了任务**并完成审稿
     ——反模式第 15 条的"任务包落盘"生效了。主代理的自检版另存为
     `REVIEW_round4_selfcheck_primary.md`。
   - **RC-M1（最重要，已复算证实）**：§3.2 的 SD 从未定义；归档 `sd_fp` 是"折 × 重复"池化
     SD，改用 §3.1 的折间 SD 后判据翻转：iForest 6/6→**2/6**、3σ RMS 6/6→**4/6**、
     马氏 2/6→**0/6**（`REVIEW_round4_sd_definition_check{,2}.py/.txt`）。稿件已补口径与两套
     读数，但**"EXP-V2-05 的 Y2 是否改判"是需要人工裁决的假说判定问题**。
   - **RC-M2（已证实）**：EXP-V1-11/V2-01/V2-02 并无 L1+L2/哈希基线记录
     （`verify_paper_experiments.py` 只覆盖 V1-05~V1-10）；稿件已改为如实声明。
   - RC-M3 / RC-M4 与 §5.5 残句已按最小改法修正。
"""

with io.open(BRIEF, "r", encoding="utf-8", newline="") as fh:
    brief = fh.read()

pattern = r"1\. ~~跑第 4 位审稿人~~.*?(?=2\. \*\*补两处归档产物\*\*)"
hits = len(re.findall(pattern, brief, re.DOTALL))
if hits != 1:
    raise SystemExit(f"FAIL: expected 1 match for section 4 item 1, found {hits}")
brief = re.sub(pattern, lambda _m: ITEM1 + "\n", brief, count=1, flags=re.DOTALL)

brief = brief.replace(
    "论文 v1.0 稿**已完成并经过四轮模拟审稿的修正**（第 4 轮于 2026-09-20 完成，但**未取得独立性**，见 §4）",
    "论文 v1.0 稿**已完成并经过四轮模拟审稿的修正**（第 4 轮独立报告于 2026-09-20 完成，"
    "并暴露出一个待人工裁决的口径问题，见 §4）",
)
if "待人工裁决的口径问题" not in brief:
    raise SystemExit("FAIL: section 0 status line not updated")

# also record the new commits in the to-do item
brief = brief.replace(
    "5. **待办**：本地已提交 2 个 commit（`ce1e81a` 审稿记录、`80e1f5e` 稿件修正），",
    "5. **待办**：本会话已提交并推送 4 个 commit（`ce1e81a`、`80e1f5e`、`0745b8d`、`4403120`）；",
)
if "4403120" not in brief:
    raise SystemExit("FAIL: commit list not updated")

with io.open(BRIEF, "w", encoding="utf-8", newline="") as fh:
    fh.write(brief)
print("brief corrected")
