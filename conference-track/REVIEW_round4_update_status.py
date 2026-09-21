#!/usr/bin/env python3
"""Append the round-4 independent-review outcome (and the open adjudication item) to STATUS.md."""

from __future__ import annotations

import io
import os

STATUS = os.path.join(
    r"<WORKDIR>\Documents\Codex\2026-09-15\github\motor-health-monitor-papers",
    "conference-track", "STATUS.md",
)

ADDITION = """

---

## 2026-09-20 更新（第二次）：第 4 轮**独立**审稿实际完成，并暴露一处判定口径问题

- **独立报告确实产出了**：孙代理从落盘任务包 `REVIEW_round4_TASK_C.md` 恢复任务并完成审稿，
  写入 `REVIEW_round4_reviewerC.md`（46 KB，Major 4 / Minor 10）。主代理的自检版保留为
  `REVIEW_round4_selfcheck_primary.md`（见 commit ce1e81a）。
  反模式第 15 条的"任务包落盘"救回了这一轮；消息通道本身仍然失效。
- **RC-M1（已由主代理复算证实，本轮最重要）**：§3.2 的 SD **从未定义**。归档 summary 里的
  `sd_fp` 是"折 × 重复"**池化** SD；改用 §3.1 所用的**折间** SD 重算同一批单元后判据翻转：
  Isolation Forest 6/6 → **2/6**、3σ RMS 6/6 → **4/6**、马氏 2/6 → **0/6**
  （脚本与输出：`REVIEW_round4_sd_definition_check{,2}.py/.txt`）。按折间口径，两个未饱和
  检测器都达不到 EXP-V2-05 预注册 Y2 所要求的 80% 单元占比。
  → 稿件已补口径定义与两套读数（Abstract / §3.2 / §7 / Fig.1 图注）；
  **但"Y2 是否改判"属于假说判定，留人工裁决，主代理未擅自改判。**
- **RC-M2（已证实）**：§3.5 原称 EXP-V1-11/V2-01/V2-02 具备 L1+L2 与哈希基线；
  实际 `src/verify_paper_experiments.py` 只覆盖 V1-05~V1-10，实验目录内的哈希文件也只有
  V1-05~V1-10、V2-04、V2-05。稿件已改为如实声明"未找到可查证的验证记录"。
- **RC-M3 / RC-M4**：§2 已补 IMS `1st_test` 的 `2003.10.22*` 选取规则（12/15 文件），
  已如实改写 A–D 分级声明；§5.5 中遗留的 order-of-magnitude 残句已清除。
"""

with io.open(STATUS, "r", encoding="utf-8", newline="") as fh:
    text = fh.read()

if "REVIEW_round4_selfcheck_primary" in text:
    raise SystemExit("STATUS already updated; nothing changed")

with io.open(STATUS, "w", encoding="utf-8", newline="") as fh:
    fh.write(text.rstrip("\n") + "\n" + ADDITION)
print("STATUS.md updated")
