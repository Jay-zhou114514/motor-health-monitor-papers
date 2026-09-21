#!/usr/bin/env python3
"""Apply the Layer-1 de-AI pass to the English manuscript.

Targets only the categories identified by POLISH_L1_humanizer_scan.md: staged bold openers,
meta-discourse, dash overuse, over-long sentences, one over-strong claim, and terminology drift.
No number, scope statement or claim strength is altered except the two remaining
"order of magnitude" residues, which round 3 required removed.
"""

from __future__ import annotations

import io
import os
import re

TRACK = r"<WORKDIR>\Documents\Codex\2026-09-15\github\motor-health-monitor-papers\conference-track"
PAPER = os.path.join(TRACK, "PAPER_v1.0_submission-draft.md")


def read(path):
    with io.open(path, "r", encoding="utf-8", newline="") as fh:
        return fh.read()


def write(path, text):
    with io.open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


EDITS = [
    # dashes
    ("IMS `1st_test` (12 healthy recordings — the files carrying the `2003.10.22*` name prefix, out "
     "of the 15 in the archive — 20 kHz, 1.024 s),",
     "IMS `1st_test` (12 healthy recordings, namely the files carrying the `2003.10.22*` name prefix "
     "out of the 15 in the archive, 20 kHz, 1.024 s),",
     "datasets list dash"),

    ("so per-evaluation resolution is not constant across cells — the stored values imply",
     "so per-evaluation resolution is not constant across cells; the stored values imply",
     "section 3.2 dash"),

    ("not the dataset size — and where the budget is set in recordings, say how many windows each "
     "recording contributes.",
     "not the dataset size, and where the budget is set in recordings, say how many windows each "
     "recording contributes.",
     "checklist item 1 dash"),

    ("and random seed — and state how that variability is estimated (pooled across evaluations or "
     "between folds), since the two definitions can reverse the verdict.",
     "and random seed, and state how that variability is estimated (pooled across evaluations or "
     "between folds), since the two definitions can reverse the verdict.",
     "checklist item 2 dash"),

    ("and in one cell on 100% exactly — the metric has no room left to vary",
     "and in one cell on 100% exactly, so the metric has no room left to vary",
     "section 5.2 dash"),

    ("in different datasets — a floor of 20 windows in one, a cap of 60 in the other.",
     "in different datasets: a floor of 20 windows in one, a cap of 60 in the other.",
     "section 5.3 dash"),

    ("that dataset takes precedence — none of our evidence is from our own hardware.",
     "that dataset takes precedence, since none of our evidence is from our own hardware.",
     "section 5.5 dash"),

    # over-long openers
    ("Using the same detector (Isolation Forest, 200 trees, max_samples 0.5), the same threshold "
     "rule (0.99 quantile of the training scores) and the same dataset (Paderborn condition "
     "N15_M07_F10), we compared two evaluation scopes over the six healthy bearings (EXP-V2-03; "
     "`experiments/EXP-V2-03-summary.csv`, regime `R2_bearing_holdout`, arm `S2_new_records`):",
     "Detector, threshold rule and dataset are held fixed across the six healthy bearings: Isolation "
     "Forest with 200 trees and max_samples 0.5, a 0.99 quantile of the training scores, and the "
     "Paderborn condition N15_M07_F10. We compared two evaluation scopes over those bearings "
     "(EXP-V2-03; `experiments/EXP-V2-03-summary.csv`, regime `R2_bearing_holdout`, arm "
     "`S2_new_records`):",
     "section 3.1 opener split"),

    ("Holding the sample size fixed at 20 recordings and restricting training bearings to the "
     "**same operating condition** as the held-out bearing (EXP-V2-05 for the Isolation Forest row, "
     "EXP-V2-06 for the 3σ RMS and Mahalanobis rows; `experiments/EXP-V2-05-summary.csv`, "
     "`EXP-V2-06-summary.csv`):",
     "The sample size is fixed at 20 recordings, and training bearings are restricted to the **same "
     "operating condition** as the held-out bearing. The Isolation Forest row comes from EXP-V2-05, "
     "the 3σ RMS and Mahalanobis rows from EXP-V2-06 (`experiments/EXP-V2-05-summary.csv`, "
     "`EXP-V2-06-summary.csv`):",
     "section 3.2 opener split"),

    ("We froze one rule (H = clip(max(20, 0.10·N), 20, 60), requiring H/N ≤ 0.25) and swept five "
     "variants (fraction 5/10/20%, floor 10/20/30) on two independently collected run-to-failure "
     "datasets (EXP-V2-04;",
     "We froze one healthy-phase rule, H = clip(max(20, 0.10·N), 20, 60) with H/N ≤ 0.25, and call "
     "the resulting cut the healthy/degraded boundary. We swept five variants of it (fraction "
     "5/10/20%, floor 10/20/30) on two independently collected run-to-failure datasets (EXP-V2-04;",
     "section 3.3 rule sentence split"),

    # staged bold openers
    ("**The reported rate has a noise floor.** With the test set held fixed,",
     "The reported rate also has a noise floor. With the test set held fixed,",
     "3.6 opener 2"),

    ("**Resampling is not a substitute for data.** On the Paderborn bearings,",
     "Resampling cannot substitute for new data. On the Paderborn bearings,",
     "3.6 opener 3"),

    ("**Search cost and stability trade off.** With hyperparameters selected inside the training data,",
     "Search cost trades off against stability. With hyperparameters selected inside the training data,",
     "3.6 opener 4"),

    # meta-discourse and connectives
    ("The two scopes are not equally replicated and we state this plainly.",
     "The two scopes are not equally replicated.",
     "3.1 meta"),

    ("the increase is therefore **at least** about 3.5-fold",
     "the increase is **at least** about 3.5-fold",
     "3.1 therefore"),

    ("We also report a preregistered criterion that failed.",
     "One preregistered criterion failed.",
     "3.1 meta 2"),

    ("The comparison reported here is therefore the new-records arm",
     "The comparison reported here is the new-records arm",
     "3.1 therefore 2"),

    ("The direction is unambiguous; the magnitude depends on the depth of the split",
     "The direction is the same across all six held-out bearings; the magnitude depends on the depth "
     "of the split",
     "3.1 claim strength"),

    ("We report both readings, and the claim we make here is the weaker one: with this little "
     "healthy data,",
     "The claim we make here is the weaker of the two readings: with this little healthy data,",
     "3.2 meta"),

    ("Cells are therefore compared on the SD scale rather than on absolute rates.",
     "Cells are compared on the SD scale rather than on absolute rates.",
     "3.2 therefore"),

    ("We therefore make no verification claim for those three experiments.",
     "We make no verification claim for those three experiments.",
     "3.5 therefore"),

    ("and we flag this as a remaining limitation",
     "and we list it as a remaining limitation",
     "3.5 meta"),

    # round-3 residue: a lower bound must not be described as an upper bound
    ("the defensible ratio is about 3.5-fold rather than an order of magnitude (§3.1).",
     "the increase is at least about 3.5-fold, and these data do not bound it from above (§3.1).",
     "5.1 order of magnitude"),

    ("resolution, the defensible ratio is about 3.5-fold rather than an order of magnitude.",
     "resolution, the increase is at least about 3.5-fold.",
     "7 order of magnitude"),

    # terminology
    ("yields mean false-positive rates of 16.9–57.6% for",
     "yields mean false-alarm rates of 16.9–57.6% for",
     "caption false-positive"),

    ("4. The healthy-phase rule was chosen by us and is defended by a sensitivity sweep",
     "4. The healthy/degraded boundary was chosen by us and is defended by a sensitivity sweep",
     "limitations terminology"),
]


text = read(PAPER)
for target, replacement, label in EDITS:
    pattern = r"\s+".join(re.escape(w) for w in target.split())
    hits = len(re.findall(pattern, text))
    if hits != 1:
        raise SystemExit(f"FAIL [{label}]: expected 1 match, found {hits}")
    text = re.sub(pattern, lambda _m: replacement, text, count=1)
    print(f"  ok  {label}")

write(PAPER, text)
print(f"\n{len(EDITS)} edits applied; dashes and openers reworked, no numbers changed")
