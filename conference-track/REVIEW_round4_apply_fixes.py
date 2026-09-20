#!/usr/bin/env python3
"""Apply the round-4 (Reviewer C) completeness/reproducibility corrections.

Every replacement is an exact-match, single-occurrence substitution with an assertion, so the
script fails loudly rather than editing the wrong sentence. Run from anywhere:

    python REVIEW_round4_apply_fixes.py
"""

from __future__ import annotations

import io
import os
import re
import sys

PAPERS = r"C:\Users\32597\Documents\Codex\2026-09-15\github\motor-health-monitor-papers"
TRACK = os.path.join(PAPERS, "conference-track")


def read(path):
    with io.open(path, "r", encoding="utf-8", newline="") as fh:
        return fh.read()


def write(path, text):
    with io.open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


def flex(text):
    """Turn a plain-text target into a whitespace-tolerant regex."""
    return r"\s+".join(re.escape(word) for word in text.split())


def sub_once(text, target, replacement, label):
    pattern = flex(target)
    hits = len(re.findall(pattern, text))
    if hits != 1:
        raise SystemExit(f"FAIL [{label}]: expected exactly 1 match, found {hits}")
    print(f"  ok  {label}")
    return re.sub(pattern, lambda _m: replacement, text, count=1)


def replace_all(text, target, replacement, label, expected):
    pattern = flex(target)
    hits = len(re.findall(pattern, text))
    if hits != expected:
        raise SystemExit(f"FAIL [{label}]: expected {expected} matches, found {hits}")
    print(f"  ok  {label} ({hits})")
    return re.sub(pattern, lambda _m: replacement, text)


# ------------------------------------------------------------------ the manuscript
paper_path = os.path.join(TRACK, "PAPER_v1.0_submission-draft.md")
paper = read(paper_path)
print("PAPER_v1.0_submission-draft.md")

# RC-M1: name the experiment behind each result block.
paper = sub_once(
    paper,
    "we compared two evaluation scopes over the six healthy bearings:",
    "we compared two evaluation scopes over the six healthy bearings\n"
    "(EXP-V2-03; `experiments/EXP-V2-03-summary.csv`, regime `R2_bearing_holdout`, arm "
    "`S2_new_records`):",
    "RC-M1 section 3.1 source",
)

paper = sub_once(
    paper,
    "Holding the sample size fixed at 20 recordings and restricting training bearings to the "
    "**same operating condition** as the held-out bearing:",
    "Holding the sample size fixed at 20 recordings and restricting training bearings to the "
    "**same operating condition** as the held-out bearing (EXP-V2-05 for the Isolation Forest "
    "row, EXP-V2-06 for the 3σ RMS and Mahalanobis rows;\n"
    "`experiments/EXP-V2-05-summary.csv`, `EXP-V2-06-summary.csv`):",
    "RC-M1 + RB-m2 section 3.2 source",
)

paper = sub_once(
    paper,
    "and swept five variants (fraction 5/10/20%, floor 10/20/30) on two independently collected "
    "run-to-failure datasets:",
    "and swept five variants (fraction 5/10/20%, floor 10/20/30) on two independently collected "
    "run-to-failure datasets (EXP-V2-04; the per-rule result is recorded with its rule labels in "
    "`experiments/EXP-V2-04-xjtu-pronostia.md` §3, while the archived CSVs carry the main and "
    "sensitivity arms without a rule column):",
    "RC-M3 section 3.3 source",
)

paper = sub_once(
    paper,
    "did not reproduce in any **independent** fold: 0 of 26.",
    "did not reproduce in any **independent** fold: 0 of 26 (EXP-V1-06 and EXP-V1-07; "
    "`experiments/EXP-V1-07-folds.csv`).",
    "RC-M1 section 3.4 source",
)

# RC-m3: the determinism sentence is true of one arm only.
paper = sub_once(
    paper,
    "In the within-bearing arm the training budget of 96 recordings equals the entire training "
    "pool, so all 100 replicates draw the same subset and the 0.00% figure is a single "
    "deterministic evaluation rather than a distribution.",
    "In the new-records arm of the within-bearing scope the training budget of 96 recordings "
    "equals the entire training pool, so the draw is the identity and the 0.00% figure is a "
    "single deterministic evaluation rather than a distribution; the resampling arm at the same "
    "nominal size does not coincide in that way, and its within-bearing replicates vary "
    "(mean 4.96%, SD 12.1 pp).",
    "RC-m3 within-bearing determinism",
)

# RC-m5: the k_max ceiling has two causes, not one.
paper = sub_once(
    paper,
    "the sweep reaches k_max = 4, 4, 2 and 3, 3, 4 respectively, and the ratios above are taken "
    "at those points.",
    "the sweep stops at the smaller of the bearings available in the condition and four training "
    "bearings, so k_max = 4, 4, 2 for the three PRONOSTIA conditions and 3, 3, 4 for the three "
    "XJTU-SY conditions, and the ratios above are taken at those points. The record budget is the "
    "binding constraint in three cells (PRONOSTIA C1 and C2, XJTU-SY 40Hz10kN); in the other "
    "three (PRONOSTIA C3, XJTU-SY 35Hz12kN and 37.5Hz11kN) the number of bearings left in the "
    "condition binds instead, after one is held out for testing.",
    "RC-m5 k_max ceiling cause",
)

# RC-m4: state what the Section 3.2 rate is computed over.
paper = sub_once(
    paper,
    "*Boundary*: the bearings left in a condition after the healthy-phase rule number 7, 7 and 3 "
    "for the three PRONOSTIA conditions and 4, 4 and 5 for the three XJTU-SY conditions.",
    "The rate in this table is computed over the windows of the held-out bearing, and the number "
    "of scored windows differs between folds, so per-evaluation resolution is not constant across "
    "cells — the stored values imply denominators of 60, 30, 20 and 15 windows in the PRONOSTIA "
    "cells and 20, 10 and 5 in the XJTU-SY cells. Cells are therefore compared on the SD scale "
    "rather than on absolute rates.\n\n"
    "*Boundary*: the bearings left in a condition after the healthy-phase rule number 7, 7 and 3 "
    "for the three PRONOSTIA conditions and 4, 4 and 5 for the three XJTU-SY conditions.",
    "RC-m4 rate unit and resolution",
)

# RC-m1 (echo of RB-m8): the "fourteen classes" total is not in the cited file.
paper = sub_once(
    paper,
    "Fourteen classes of analysis error are listed in the project's disclosure register "
    "(`docs/EXPERIMENT_AFTERCARE.md`) and were found and corrected during the study. Eleven lie "
    "in summary, verdict and verification logic, and three concern data handling such as seed "
    "derivation and file counting; none lies in the model fitting itself.",
    "Analysis errors were found and corrected during the study; the project keeps a standing "
    "register of the classes involved (`docs/EXPERIMENT_AFTERCARE.md`, an internal working-tree "
    "document). They lie in summary, verdict and verification logic and in data handling such as "
    "seed derivation and file counting; none lies in the model fitting itself.",
    "RC-m1 analysis-error register",
)

# RC-m6: the checklist's own first item.
paper = sub_once(
    paper,
    "1. Report the number of training windows behind the threshold, not the dataset size.",
    "1. Report the number of training windows behind the threshold, not the dataset size — and "
    "where the budget is set in recordings, say how many windows each recording contributes.",
    "RC-m6 checklist item 1",
)

# RC-m6 and RC-m4 in Limitations.
paper = sub_once(
    paper,
    "8. Literature scope: the search covered Scopus and arXiv; Chinese-language venues and PHM "
    "conference proceedings are not comprehensively covered. References [11] and [13] are cited "
    "at title level only because their abstracts were not retrievable.",
    "8. Literature scope: the search covered Scopus and arXiv; Chinese-language venues and PHM "
    "conference proceedings are not comprehensively covered. References [11] and [13] are cited "
    "at title level only because their abstracts were not retrievable.\n"
    "9. Window construction is fixed in the frozen protocol for IMS and MFPT only; for Paderborn, "
    "PRONOSTIA and XJTU-SY it is defined in the experiment code.\n"
    "10. The rates in §3.2 are window-level and their resolution differs between folds, so "
    "absolute rates are not directly comparable across cells; the comparisons are made on the SD "
    "scale.",
    "RC-m4/RC-m6 limitations",
)

# RC-M2: a data and code availability statement.
paper = sub_once(
    paper,
    "## 7. Conclusion",
    "## Data and code availability\n\n"
    "The experiment registry, preregistrations, scripts, run logs, per-fold CSVs, hash files and "
    "figures behind this paper are archived under `experiments/` and `docs/` of "
    "`github.com/Jay-zhou114514/motor-health-monitor`, using the naming convention `EXP-V1-0X` / "
    "`EXP-V2-0X`; the manuscript sources, claim-to-evidence map and review records are in "
    "`github.com/Jay-zhou114514/motor-health-monitor-papers` under `conference-track/`. Paths of "
    "the form `docs/…` and `experiments/…` cited in the text are paths inside the first "
    "repository, and `docs/EXPERIMENT_AFTERCARE.md` is an internal working-tree document rather "
    "than a published artefact. All five datasets are third-party public datasets used under "
    "their own terms: IMS (NASA Prognostics Data Repository), MFPT (distributed by MathWorks), "
    "Paderborn (doi above), XJTU-SY (Wang et al., 2020) and PRONOSTIA (IEEE PHM 2012 Data "
    "Challenge, FEMTO-ST). No new data were generated. The AI-use disclosure required by the "
    "target venue is maintained in `docs/AI_USE_DISCLOSURE.md`.\n\n"
    "---\n\n"
    "## 7. Conclusion",
    "RC-M2 data and code availability",
)

write(paper_path, paper)

# ------------------------------------------------------- the round-4 report typo
report_path = os.path.join(TRACK, "REVIEW_round4_reviewerC.md")
report = read(report_path)
report = replace_all(report, "preregistered criterios", "preregistered criteria",
                     "report typo", 1)
write(report_path, report)

# ---------------------------------------------------------------- STATUS.md note
status_path = os.path.join(TRACK, "STATUS.md")
status = read(status_path)
note = """

---

## 2026-09-20 更新：第 4 轮审稿（Reviewer C）——侧重报告完整性与读者可复现性

**过程事故（必须记录）**：本轮**未能获得独立审稿**。为这一轮启动了四个子代理实例
（两次直接 spawn + 两个孙代理），**每一个都没有收到任务文本**；短 ASCII 探针同样未被回执。
本会话的多代理消息通道不可用。因此 `REVIEW_round4_reviewerC.md` 由**主会话代理**写成，
与三轮修正的执行者是同一个实例，**独立性未达成**，该报告应读作"带全量复算的自检"。
真正的第 4 轮需要在子代理通道可用的会话里、或以独立任务重跑。

**内容结论**：复算脚本 `REVIEW_round4_number_check{,2,3,4}.py`（输出同名 `.txt`）逐项重算
§3.1–§3.6、§5.1 与 Fig.1 图注的数字：**本轮未发现任何算术不一致**（两处小口径核对：
2.40/5.19 pp 与 5.20/4.39/5.18 pp 均逐位吻合）。问题集中在"数字→来源"的可追溯链与
读者可复现性：

- **RC-M1（Major）**：§3.1–§3.4 通篇不出现实验编号（唯一出现处是 §3.5 的验证深度段），
  读者无法从论文走到归档产物。第 3 轮 RB-m2 的同类要求**未落实**。
- **RC-M2（Major）**：全文没有代码/数据可用性声明（仅 Paderborn 有 DOI），却把
  `docs/EXPERIMENT_AFTERCARE.md` 这类**内部路径**当作证据引用。
- **RC-M3（Major）**：§3.3 的五条健康阶段规则**在任何 CSV 中都没有规则标签**，
  2.40 pp / 5.19 pp 只能追溯到实验记录里的散文表格。
- 6 条 Minor：14 类错误计数与所引文件（15 条反模式）不符；§3.6 的 86% 在汇总 CSV 中无列且
  复制文件的 R=50/R=200 两臂不可分离；§3.1 "100 次复制取同一子集"只对新记录臂成立；
  §3.2 未说明误报率的单位与分辨率（n=350 是 折×重复，不是窗口数）；k_max 上限的原因
  在六个格里被统一归给记录预算（其中三格实际由轴承数决定）；运行至失效数据集的窗口构造
  在论文与冻结协议中都没有。

**收敛判定**：第 3 轮 3 条 Major **全部已解决**；10 条 Minor 中 7 条已解决，
3 条未解决（RB-m2 / RB-m8 / RB-m10），且三条未解决项属同一类型——**文中断言了某个量，
但归档里没有对应产物**。

**已应用的修正**（见 `REVIEW_round4_apply_fixes.py`，全部为精确匹配替换并带断言）：
§3.1–§3.4 补实验编号与 CSV 名；§3.1 确定性语句限定到新记录臂；§3.2 补误报率单位/分辨率、
修正 k_max 成因；§3.3 标注规则标签所在位置；§3.5 改为定性表述并注明该文件是内部文档；
§3.6 检查清单第 1 条补"记录数→窗口数"；Limitations 新增第 9、10 条；
新增 **Data and code availability** 一节。

**仍待人工决定/后续**：(a) 把五条规则以带标签的 CSV 落盘（RC-M3）；
(b) 在臂级汇总里补 zero-minimum 占比列、并给复制文件加 arm 列（RC-m2）；
(c) 是否公开仓库与许可信息、以及目标会议的 AI 使用披露口径（S-3 决策的一部分）。
"""
write(status_path, status.rstrip("\n") + "\n" + note)

print("\nall edits applied")
sys.exit(0)
