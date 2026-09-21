#!/usr/bin/env python3
"""Apply the user's tightened Layer-2 claim (unit effect) to the paper and the claim map.

Old framing: "simple detectors show a stable low false-alarm rate / the unit effect holds 6 of 6".
New framing: with limited healthy data the apparent stability depends on how cross-fold variation
is defined and estimated, and under between-fold variation the preregistered 80% stability
criterion is not met.
"""

from __future__ import annotations

import io
import os
import re

TRACK = r"<WORKDIR>\Documents\Codex\2026-09-15\github\motor-health-monitor-papers\conference-track"
PAPER = os.path.join(TRACK, "PAPER_v1.0_submission-draft.md")
CLAIMS = os.path.join(TRACK, "CLAIM_EVIDENCE_MAP.md")


def read(path):
    with io.open(path, "r", encoding="utf-8", newline="") as fh:
        return fh.read()


def write(path, text):
    with io.open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


def sub_once(text, target, replacement, label):
    pattern = r"\s+".join(re.escape(w) for w in target.split())
    hits = len(re.findall(pattern, text))
    if hits != 1:
        raise SystemExit(f"FAIL [{label}]: expected 1 match, found {hits}")
    print(f"  ok  {label}")
    return re.sub(pattern, lambda _m: replacement, text, count=1)


paper = read(PAPER)

paper = sub_once(
    paper,
    "At a fixed sample size, increasing the number of distinct training bearings reduced the pooled "
    "spread of the reported rate for two of three detectors (6 of 6 conditions each under the pooled "
    "definition; 2 of 6 and 4 of 6 under the between-fold definition), whereas the third saturated "
    "and could not be evaluated this way.",
    "At a fixed sample size, whether the reported rate looks stable depends on how cross-fold "
    "variation is defined and estimated: under the pooled definition the spread falls for two of the "
    "three detectors in every condition, but under between-fold variation the preregistered 80% "
    "stability criterion is not met (2 of 6 conditions for Isolation Forest, 4 of 6 for the 3σ RMS "
    "threshold, and 0 of 6 for the third detector, which saturates).",
    "abstract",
)

paper = sub_once(
    paper,
    "We report both readings and treat the pooling as an open adjudication item rather than a settled "
    "result.",
    "We report both readings, and the claim we make here is the weaker one: with this little healthy "
    "data, the stability of detector performance depends on how cross-fold variation is defined and "
    "estimated, and evaluated by between-fold variation the preregistered 80% stability criterion is "
    "not met. The pooled reading is reported as a sensitivity, not as the result.",
    "section 3.2 verdict",
)

paper = sub_once(
    paper,
    "At a fixed sample size, and under the pooled SD definition, adding distinct training bearings "
    "reduced the spread for two detectors by 10–45% and 14–68% respectively (2 of 6 and 4 of 6 cells "
    "under the between-fold definition), while the third saturated at 67–100% false alarms and became "
    "uninformative rather than unstable.",
    "At a fixed sample size, whether the detectors look stable depends on how cross-fold variation is "
    "defined and estimated. Under the pooled SD the spread of the reported rate fell in every "
    "condition for two detectors, by 10–45% and 14–68%; under between-fold variation the "
    "preregistered 80% criterion is met in neither, at 2 of 6 and 4 of 6, and the third detector "
    "saturated at 67–100% false alarms. We therefore report detector stability in this setting as "
    "definition-dependent rather than as an established improvement.",
    "conclusion",
)

paper = sub_once(
    paper,
    "reduces the spread; the effect holds for 3σ RMS and Isolation Forest (6 of 6 operating conditions "
    "each under the pooled SD definition, 4 of 6 and 2 of 6 under the between-fold definition) but not "
    "for the Mahalanobis detector, which saturates at 67–100% false alarms and is therefore not "
    "testable this way.",
    "reduces the spread under the pooled SD definition (6 of 6 conditions for 3σ RMS and Isolation "
    "Forest) but not under between-fold variation (4 of 6 and 2 of 6), so the preregistered 80% "
    "stability criterion holds only under the pooled reading; the Mahalanobis detector saturates at "
    "67–100% false alarms and is not testable this way.",
    "figure caption",
)

paper = sub_once(
    paper,
    "2. Report resampling variability from at least two sources — split composition and random seed.",
    "2. Report resampling variability from at least two sources — split composition and random seed — "
    "and state how that variability is estimated (pooled across evaluations or between folds), since "
    "the two definitions can reverse the verdict.",
    "checklist item 2",
)

write(PAPER, paper)

claims = read(CLAIMS)

claims = sub_once(
    claims,
    "| **C9** | **单元数效应**：工况固定时，训练轴承数 1→3/4 显著降低报告误报率的 SD —— "
    "**3σ RMS 6/6、Isolation Forest 6/6**；k=1 时均值误报 54–58%（XJTU-SY）/17–21%（PRONOSTIA）。"
    "**马氏距离因 k=1 饱和（67–100%）不在适用范围内** | EXP-V2-05 + EXP-V2-06（两个数据集） | "
    "`EXP-V2-05-*`、`EXP-V2-06-*` | **B** |",
    "| **C9** | **单元数效应（2026-09-20 已收紧）**：在有限健康数据下，检测器性能的**稳定性依赖于"
    "如何定义与估计跨折变异**。按池化 SD，训练轴承数 1→k_max 降低报告误报率的 SD"
    "（3σ RMS 6/6、Isolation Forest 6/6）；**按折间变异评估时，预注册的 80% 稳定性标准未被达到**"
    "（Isolation Forest 2/6、3σ RMS 4/6）。**马氏距离因 k=1 饱和（67–100%）不在适用范围内** | "
    "EXP-V2-05 + EXP-V2-06（两个数据集）；口径对照见 `REVIEW_round4_sd_definition_check2.txt` | "
    "`EXP-V2-05-*`、`EXP-V2-06-*` | **B（口径依赖，措辞已降级）** |",
    "claim map C9",
)

claims = sub_once(
    claims,
    "| \"单元效应对所有检测器成立\" | 马氏距离 k=1 饱和（67–100% 误报），不可检验 | EXP-V2-06 |",
    "| \"单元效应对所有检测器成立\" | 马氏距离 k=1 饱和（67–100% 误报），不可检验 | EXP-V2-06 |\n"
    "| \"单元效应在任意口径下都成立\"（\"6/6 稳定\"） | 只在**池化 SD** 下成立；换成**折间 SD** 后 "
    "2/6 与 4/6，低于预注册 Y2 的 80% 门槛 | `REVIEW_round4_sd_definition_check2.txt` |",
    "claim map forbidden list",
)

write(CLAIMS, claims)
print("layer-2 claim tightened in paper and claim map")
