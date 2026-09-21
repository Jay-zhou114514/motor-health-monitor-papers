#!/usr/bin/env python3
"""Fix the brief's paper-status bullets (the earlier target string was wrong)."""

from __future__ import annotations

import io
import os

BRIEF = os.path.join(
    r"<WORKDIR>\Documents\Codex\2026-09-06\github\motor-health-monitor",
    "docs", "plans", "NEXT_SESSION_BRIEF.md",
)

OLD = ("- **稿件**：`PAPER_v1.0_submission-draft.md`（Abstract / Intro / Protocol / Results 含 §3.6 / "
       "Related Work / Discussion 5.1–5.5 / Limitations 8 条 / Conclusion / Fig.1 图注 / 数据集引用）\n"
       "- **主张-证据映射**：`CLAIM_EVIDENCE_MAP.md`（C1–C10 + 禁写清单）\n"
       "- **引用**：`REFERENCES.md`（19 条，已 Crossref/arXiv 核实）＋ `CITATION_AUDIT.md`\n"
       "- **图**：`figures/fig1_three_faces.{png,pdf,svg}` + 三份 QA 报告（碰撞 69 → 0）\n"
       "- **审稿记录**：`REVIEW_round1_reviewer_scope.md`、`REVIEW_round2_serial_reviewerA.md`、"
       "`REVIEW_round3_reviewerB.md`")

NEW = ("- **稿件（英文，投稿与事实来源）**：`PAPER_v1.0_submission-draft.md`（Abstract / Intro / "
       "Protocol / Results 含 §3.6 / Related Work / Discussion 5.1–5.5 / Limitations 10 条 / "
       "数据与代码可用性 / Conclusion / Fig.1 图注 / 数据集引用）\n"
       "- **中文版（派生）**：`PAPER_v1.0_中文版.md` —— 英文稿的逐句对照翻译，文件头写明派生关系与"
       "「以英文稿为准」；数字一致性校验见 `POLISH_zh_translation_check.txt`（144 个不同数字、"
       "434 次出现，两侧一致）\n"
       "- **主张-证据映射**：`CLAIM_EVIDENCE_MAP.md`（C1–C10 + 禁写清单；C9 已于 2026-09-20 收紧）\n"
       "- **引用**：`REFERENCES.md`（19 条，已 Crossref/arXiv 核实）＋ `CITATION_AUDIT.md`\n"
       "- **图**：`figures/fig1_three_faces.{png,pdf,svg}` + 三份 QA 报告（碰撞 69 → 0）\n"
       "- **审稿记录**：`REVIEW_round1_reviewer_scope.md`、`REVIEW_round2_serial_reviewerA.md`、"
       "`REVIEW_round3_reviewerB.md`、"
       "`REVIEW_round4_reviewerC.md`（独立，4 Major / 10 Minor）＋ "
       "`REVIEW_round4_selfcheck_primary.md`（主代理自检版）\n"
       "- **润色状态**：Layer 1 扫描 `POLISH_L1_humanizer_scan.md`；Layer 2 待 venue 确定")

with io.open(BRIEF, "r", encoding="utf-8", newline="") as fh:
    brief = fh.read()

if OLD not in brief:
    raise SystemExit("FAIL: brief paper-status block not found verbatim")
if "PAPER_v1.0_中文版.md" in brief:
    raise SystemExit("already updated")

brief = brief.replace(OLD, NEW, 1)
with io.open(BRIEF, "w", encoding="utf-8", newline="") as fh:
    fh.write(brief)
print("brief updated")
