# Draft v0.3 — Part IV: Three Faces of Evaluation Uncertainty

> 说明：本节**取代** `DRAFT_v0.1.md` 的 §3（Results）。
> 每个数字的来源见 `CLAIM_EVIDENCE_MAP.md`（C8/C9/C10）；未登记的主张不得出现。
> 写作纪律：只写 B 级及以上；边界与混杂必须与结论同段出现。

---

## 3. Results: three faces of evaluation uncertainty

We organise the results around a single question: **in healthy-data-only bearing anomaly
detection, what determines whether the reported false-alarm rate can be trusted?**
Three factors emerged, each quantified on more than one dataset.

### 3.1 Scope: does the split keep physical units apart?

Holding the detector, the threshold rule and the data fixed, we compared two evaluation
scopes on the Paderborn healthy bearings (six physical bearings, 20 recordings per
operating condition):

| Scope | Training used | Test used | Reported false-alarm rate |
| --- | --- | --- | ---: |
| **within-bearing** | recordings 1–16 of each bearing | recordings 17–20 of *the same* bearings | **0.00%** |
| **bearing-level holdout** | all recordings of five bearings | all recordings of *the held-out* bearing | **40.63%** (folds: 0.4%–97.1%) |

The same detector that appears to produce no false alarms under within-bearing
evaluation alarms on two of every five held-out healthy recordings when evaluated with
the physical unit held out. In individual folds the rate reached 97.1%.

*Boundary*: this comparison was run on one rig with six physical units. The direction is
unambiguous; the magnitude should not be transferred to another rig without repeating it.

### 3.2 Units: how many independent bearings were used for training?

Because a detector can only be as stable as the population it was fitted on, we varied
the number of *distinct training bearings* while holding the sample size fixed at 20
recordings, and restricting all training bearings to the **same operating condition** as
the held-out bearing (so that operating-condition diversity is held constant).

| Detector | SD decreases with #bearings | SD(k_max) < SD(k=1) | k=1 mean FP |
| --- | ---: | ---: | ---: |
| 3σ RMS threshold | **6/6** | **6/6** | 43–50% |
| Isolation Forest (200, 0.5) | **6/6** | **6/6** | 54–58% |
| Mahalanobis distance | 2/6 | 2/6 | **67–100%** |

For the two non-saturated detectors, going from one training bearing to three or four
reduces the standard deviation of the reported false-alarm rate by roughly a factor of
two, **at a fixed number of recordings**. With a single training bearing the mean
false-alarm rate on a different healthy bearing reaches 54–58%.

*Boundary*: the Mahalanobis detector saturates at k = 1 — its mean false-alarm rate is
67–100%, and one cell is exactly 100%, so its spread is degenerate. The unit effect is
therefore **not testable in this form** for saturated detectors, and we report it as
such rather than as a failure. We also note that the wider cross-condition comparison
(k up to 16) is confounded with operating-condition diversity; the claims above are
restricted to the within-condition design where that confound is removed.

### 3.3 Definition: where does "normal" end?

Run-to-failure datasets carry no onset label: the boundary between healthy and degraded
data must be chosen by the analyst. We froze one rule
(H = clip(max(20, 0.10·N), 20, 60), requiring H/N ≤ 0.25) and then swept five
variants (fraction 5/10/20%, floor 10/20/30) on two independently collected
run-to-failure datasets (XJTU-SY, 15 bearings; PRONOSTIA, 17 bearings).

| Dataset | SD(k_max) across the five rules | Range |
| --- | --- | ---: |
| PRONOSTIA (17 bearings, unchanged inclusion set) | 7.56 – 9.96 pp | **2.40 pp** |
| XJTU-SY (inclusion set changes with the rule) | 14.51 – 19.70 pp | **5.19 pp** |

The same detection task therefore yields a reported uncertainty that moves by 2.4–5.2
percentage points depending only on where the healthy/degraded boundary is drawn.

*Boundary*: on PRONOSTIA the set of admissible bearings is identical under all five
rules, so 2.40 pp is a clean measurement of the boundary effect. On XJTU-SY the rule
also changes *which* bearings qualify (12–15 bearings, k_max 11–14), so 5.19 pp mixes
the boundary effect with the inclusion effect and must not be attributed to the former
alone. We report the cross-dataset claim as **partially supported** for this reason.

### 3.4 What does not reproduce

For completeness we record a negative result that shaped the study. A covariance-geometry
failure observed on a single fold (distance-inflation ratio 1.576 when holding out one
MFPT healthy recording) reproduced in **1 of 27 folds** across MFPT and three IMS
batches (MFPT 1/3, IMS 0/24). A power analysis gave the original comparison a power of
0.087, so the appropriate reading is *underpowered and undetermined*, not *refuted*.

### 3.5 Reproducibility of these results

Every experiment reported above was pre-registered before execution. The four
experiments carrying the claims in §3.1–3.3 were re-run and compared hash-for-hash with
their archived outputs: EXP-V2-04/05/06 reproduced byte-for-byte, and EXP-V1-10
reproduced exactly on all scientific columns (the only difference was its wall-clock
timing column). In total, thirteen classes of analysis error were found and corrected
during the study — all of them in the way results were summarised or verified, none in
the data or the model fitting.

**Reporting checklist**

1. Report the number of training windows behind the threshold, not the dataset size.
2. Report resampling variability from at least two sources — split composition and
   random seed.
3. Report the tie rate when the validation resolution is coarser than the false-alarm
   level of interest.
4. Distinguish **new recordings** from **repeated sampling**; the latter cannot
   substitute for the former.
5. State the number of **independent units**, and whether they were held out.