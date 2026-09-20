#!/usr/bin/env python3
"""Apply the corrections that follow from the independent round-4 report (RC-M1..RC-M4)."""

from __future__ import annotations

import io
import os
import re

TRACK = r"C:\Users\32597\Documents\Codex\2026-09-15\github\motor-health-monitor-papers\conference-track"
PAPER = os.path.join(TRACK, "PAPER_v1.0_submission-draft.md")


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

# RC-M1: the pooled-versus-between-fold definition must be stated, and both outcomes reported.
paper = sub_once(
    paper,
    "| Detector | Negative rank correlation between k and SD | SD(k_max) < SD(k=1) | k=1 mean FP |",
    "| Detector | Negative rank correlation between k and SD | SD(k_max) < SD(k=1), pooled SD | "
    "k=1 mean FP |",
    "RC-M1 table header",
)

paper = sub_once(
    paper,
    "For the two non-saturated detectors, going from one training bearing to k_max reduces the "
    "standard deviation of the reported rate **at a fixed number of recordings**.",
    "SD in this table is the pooled standard deviation over the fold × repeat evaluations stored "
    "in the summary CSVs, not the between-fold SD of Section 3.1. The verdicts depend on that "
    "choice: recomputing the same cells as the SD of per-fold mean rates gives 2 of 6 for "
    "Isolation Forest, 4 of 6 for 3σ RMS and 0 of 6 for Mahalanobis "
    "(`REVIEW_round4_sd_definition_check2.txt`), so under the between-fold definition both "
    "non-saturated detectors fall short of the 80% share their preregistration required, and the "
    "saturated detector is excluded either way. We report both readings and treat the pooling as "
    "an open adjudication item rather than a settled result.\n\n"
    "For the two non-saturated detectors, and under the pooled definition, going from one training "
    "bearing to k_max reduces the standard deviation of the reported rate **at a fixed number of "
    "recordings**.",
    "RC-M1 definition and sensitivity",
)

paper = sub_once(
    paper,
    "increasing the number of distinct training bearings reduced the spread of the reported rate "
    "for two of three detectors (6 of 6 conditions each), whereas the third saturated and could "
    "not be evaluated this way.",
    "increasing the number of distinct training bearings reduced the pooled spread of the reported "
    "rate for two of three detectors (6 of 6 conditions each under the pooled definition; 2 of 6 "
    "and 4 of 6 under the between-fold definition), whereas the third saturated and could not be "
    "evaluated this way.",
    "RC-M1 abstract",
)

paper = sub_once(
    paper,
    "At a fixed sample size, adding distinct training bearings reduced the spread for two detectors "
    "by 10–45% and 14–68% respectively, while the third saturated at 67–100% false alarms and "
    "became uninformative rather than unstable.",
    "At a fixed sample size, and under the pooled SD definition, adding distinct training bearings "
    "reduced the spread for two detectors by 10–45% and 14–68% respectively (2 of 6 and 4 of 6 "
    "cells under the between-fold definition), while the third saturated at 67–100% false alarms "
    "and became uninformative rather than unstable.",
    "RC-M1 conclusion",
)

paper = sub_once(
    paper,
    "reduces the spread; the effect holds for 3σ RMS and Isolation Forest (6 of 6 operating "
    "conditions each) but not for the Mahalanobis detector",
    "reduces the spread; the effect holds for 3σ RMS and Isolation Forest (6 of 6 operating "
    "conditions each under the pooled SD definition, 4 of 6 and 2 of 6 under the between-fold "
    "definition) but not for the Mahalanobis detector",
    "RC-M1 figure caption",
)

# RC-M2: no archived verification record exists for V1-11, V2-01, V2-02.
paper = sub_once(
    paper,
    "EXP-V1-11, EXP-V2-01 and EXP-V2-02 carry invariant and recomputation checks together with an "
    "archived hash baseline, but have not been re-run for comparison. The experiment carrying §3.1 "
    "(EXP-V2-03) is in the same category and we flag this as a remaining limitation.",
    "For EXP-V1-11, EXP-V2-01 and EXP-V2-02 no archived verification record could be located while "
    "preparing this draft: the project's verification script covers EXP-V1-05 to EXP-V1-10 only, and "
    "the hash baselines on file belong to EXP-V1-05 to V1-10, EXP-V2-04 and EXP-V2-05. We therefore "
    "make no verification claim for those three experiments. The experiment carrying §3.1 "
    "(EXP-V2-03) is in the same position and we flag this as a remaining limitation.",
    "RC-M2 verification depth",
)

# residual from the round-3 RB-M2 fix: the paper no longer uses that framing
paper = sub_once(
    paper,
    "If the scope effect fails to reproduce on a rig whose bearings are more uniform, the "
    "order-of-magnitude framing would have to be restricted to rigs with strong between-bearing "
    "variation.",
    "If the scope effect fails to reproduce on a rig whose bearings are more uniform, the 3.5-fold "
    "lower bound would have to be restricted to rigs with strong between-bearing variation.",
    "leftover order-of-magnitude framing",
)

# RC-M3: state the IMS file-selection rule.
paper = sub_once(
    paper,
    "IMS `1st_test` (12 healthy recordings, 20 kHz, 1.024 s)",
    "IMS `1st_test` (12 healthy recordings — the files carrying the `2003.10.22*` name prefix, out "
    "of the 15 in the archive — 20 kHz, 1.024 s)",
    "RC-M3 IMS file selection",
)

# RC-M4: the paper never grades its own evidence.
paper = sub_once(
    paper,
    "Evidence is graded A–D; exploratory analyses are labelled as such.",
    "The project's protocol grades evidence A–D; no claim in this paper reaches Level A, since "
    "every measurement comes from a single rig or a single split, and exploratory checks are "
    "labelled as such.",
    "RC-M4 evidence grading",
)

write(PAPER, paper)
print("independent-report fixes applied")
