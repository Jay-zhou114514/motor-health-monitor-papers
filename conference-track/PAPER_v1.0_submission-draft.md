# PAPER v1.0 — 投稿稿（完整合并）

> 由 v0.1–v0.6 合并，**已应用 citation-audit 的 4 处语境修正**与 MFPT 脚注。
> 所有数字来源见 `CLAIM_EVIDENCE_MAP.md`；引用见 `REFERENCES.md`；图见 `figures/`。

---

## Title

**Three Faces of Evaluation Uncertainty in Healthy-Data-Only Bearing Anomaly Detection**

---

## Abstract

Condition monitoring is frequently deployed where only healthy-machine data are available: a
detector is fitted on healthy recordings, the alarm threshold is placed at a quantile of the
training score distribution, and the reported false-alarm rate is the number that decides
whether the monitor is usable. We ask how far that number can be trusted and what determines
it. Using four public bearing datasets under a pre-registered protocol, we find that the
reported false-alarm rate is governed less by the detector than by three analyst choices.
Holding out whole bearings, rather than only held-out recordings, raised the same detector's
false-alarm rate from 0.00% to 40.63%. At a fixed sample size, increasing the number of
distinct training bearings reduced the spread of the reported rate for two of three detectors
(6 of 6 conditions each), whereas the third saturated and could not be evaluated this way.
Moving the healthy/degraded boundary — a choice that run-to-failure data leave to the analyst
— shifted the reported uncertainty by 2.4–5.2 percentage points, with the same rule binding
on opposite sides in different datasets. We give a five-point reporting checklist and state
where each claim stops.

---

## 1. Introduction

Low-cost machine condition monitoring is typically deployed where only healthy-machine data are
available: run-to-failure records are expensive and faults are rare. A common design is to fit
a one-class model or a simple statistic on healthy data, set the alarm threshold at a high
quantile of the training score distribution, and report the resulting false-alarm rate on
held-out healthy recordings. That number is what an operator uses to decide whether the monitor
is deployable.

The question we address is not which detector is most accurate, but how far the reported number
can be trusted and what determines it. We structure the study around three analyst choices: the
**scope** of the evaluation (whether whole physical units are held apart), the number of
**independent units** used for training, and the **definition** of where healthy data end.

---

## 2. Protocol

**Datasets.** IMS `1st_test` (12 healthy recordings, 20 kHz, 1.024 s), IMS `2nd_test` and
`4th_test` (6 recordings each), Paderborn K001–K006 (6 healthy bearings, four operating
conditions, 20 recordings each, 64 kHz, 4 s), MFPT (3 healthy recordings plus labelled faults),
XJTU-SY (15 bearings, 3 conditions, 25.6 kHz, 1.28 s per record, one record per minute), and
PRONOSTIA (17 bearings, 3 loads, 25.6 kHz, 0.1 s per record, one record per 10 s).
Independent units are test rigs and physical bearings; **windows and recordings are never
treated as independent units**.

**Features and detectors.** Four frozen features (`rms`, `crest_factor`, `kurtosis`,
`centroid_hz`). Detectors: a 3σ RMS threshold, the Mahalanobis distance, an RBF one-class SVM,
and Isolation Forest. The alarm threshold is always the 0.99 quantile of the *training* score
distribution; the test set never participates in any selection.

**Discipline.** Every experiment was pre-registered before it was run; when a criterion had to
change, a separate amendment was filed rather than the original being edited. Evidence is graded
A–D; exploratory analyses are labelled as such. Four of the experiments carrying the main claims
were re-run and compared hash-for-hash with their archived outputs (§3.5).

---

## 3. Results: three faces of evaluation uncertainty

### 3.1 Scope: does the split keep physical units apart?

Holding detector, threshold rule and data fixed, we compared two evaluation scopes on the
Paderborn healthy bearings:

| Scope | Training used | Test used | Reported false-alarm rate |
| --- | --- | --- | ---: |
| within-bearing | recordings 1–16 of each bearing | recordings 17–20 of *the same* bearings | **0.00%** |
| bearing-level holdout | all recordings of five bearings | all recordings of *the held-out* bearing | **40.63%** (folds 0.4–97.1%) |

*Boundary*: one rig, six physical units. The direction is unambiguous; the magnitude should not
be transferred without repeating the comparison.

### 3.2 Units: how many independent bearings were used for training?

Holding the sample size fixed at 20 recordings and restricting training bearings to the **same
operating condition** as the held-out bearing:

| Detector | SD decreases with #bearings | SD(k_max) < SD(k=1) | k=1 mean FP |
| --- | ---: | ---: | ---: |
| 3σ RMS threshold | **6/6** | **6/6** | 43–50% |
| Isolation Forest (200, 0.5) | **6/6** | **6/6** | 54–58% |
| Mahalanobis distance | 2/6 | 2/6 | **67–100%** |

For the two non-saturated detectors, going from one training bearing to three or four halves the
standard deviation of the reported rate **at a fixed number of recordings**.

*Boundary*: the Mahalanobis detector saturates at k = 1 (one cell is exactly 100%), so its
spread is degenerate and the unit effect is **not testable in this form**; we report it as such
rather than as a failure. The wider cross-condition comparison is confounded with
operating-condition diversity and is therefore not used for the claim above.

### 3.3 Definition: where does "normal" end?

Run-to-failure datasets carry no onset label. We froze one rule (H = clip(max(20, 0.10·N), 20,
60), requiring H/N ≤ 0.25) and swept five variants (fraction 5/10/20%, floor 10/20/30) on two
independently collected run-to-failure datasets:

| Dataset | SD(k_max) across five rules | Range |
| --- | --- | ---: |
| PRONOSTIA (17 bearings, inclusion set unchanged) | 7.56 – 9.96 pp | **2.40 pp** |
| XJTU-SY (inclusion set changes with the rule) | 14.51 – 19.70 pp | **5.19 pp** |

*Boundary*: on PRONOSTIA the admissible bearing set is identical under all five rules, so 2.40
pp is a clean measurement. On XJTU-SY the rule also changes *which* bearings qualify, so 5.19 pp
mixes the boundary effect with the inclusion effect and must not be attributed to the former
alone; the cross-dataset claim is therefore **partially supported**.

### 3.4 What does not reproduce

A covariance-geometry failure observed on a single fold (distance-inflation ratio 1.576 when
holding out one MFPT healthy recording) reproduced in **1 of 27 folds** across MFPT and three
IMS batches (MFPT 1/3, IMS 0/24). A power analysis gave the original comparison a power of
0.087, so the appropriate reading is *underpowered and undetermined*, not *refuted*.

### 3.5 Reproducibility of these results

The four experiments carrying the claims in §3.1–3.3 were re-run and compared with their
archived outputs: V2-04/05/06 reproduced byte-for-byte, and V1-10 reproduced exactly on all
scientific columns (the only difference was its wall-clock timing column). Thirteen classes of
analysis error were found and corrected during the study; all of them lay in the way results
were summarised or verified, none in the data or the model fitting.

**Reporting checklist**

1. Report the number of training windows behind the threshold, not the dataset size.
2. Report resampling variability from at least two sources — split composition and random seed.
3. Report the tie rate when the validation resolution is coarser than the false-alarm level of
   interest.
4. Distinguish **new recordings** from **repeated sampling**; the latter cannot substitute for
   the former.
5. State the number of **independent units**, and whether they were held out.

---

## 4. Related Work

Several lines of work have established that anomaly-detection evaluation is unreliable in
general, and our contribution is not that observation. Wu and Keogh [1] showed that the majority
of exemplars in widely used benchmarks suffer from identifiable flaws and that much of the
apparent progress may be illusory. Kim et al. [2] showed that the point-adjustment protocol can
inflate results to the point where even a random score appears state-of-the-art, and Sehili and
Zhang [3] report that most proposed multivariate solutions are evaluated with inappropriate or
highly flawed protocols.

A second line quantifies how much of a reported result is an artefact of choices unrelated to the
method. Bouthillier et al. [4] modelled the benchmarking process and showed that variance from
**data sampling, parameter initialisation and hyperparameter choice** markedly affects the
results. In chemoinformatics, Krstajic et al. [12] documented the pitfalls of using
cross-validation both to select and to assess models and argued for repeated, nested procedures.
For time-series anomaly detection specifically, MSAD [6] studies model selection *carried out by
time-series classifiers* over a large configuration space and reports that the resulting choices
are far from optimal, while mTSBench [7] benchmarks model selection across 344 series and finds
that even the strongest selection methods remain far from optimal. Most recently, the
rank-instability study of [5] varied dataset selection, metrics, hyperparameters and seeds across
690 datasets and found that algorithm rankings in anomaly detection are highly unstable.
Improvements to the instruments themselves have also been proposed: proximity-aware scoring [9],
a problem-oriented taxonomy of metrics [10], robust evaluation frameworks for unsupervised
detection [11], and unified benchmarking pipelines [8].

Within bearing and machine fault diagnosis, two threads are directly relevant. Power-analysis-
based procedures have been proposed to determine the minimum number of vibration samples needed
for a classifier **in vibration-based fault diagnosis** [13], and applied, for example, to
automotive hydraulic brake diagnosis [14]; both target supervised classification with accuracy
as the endpoint. On the evaluation side, Vieira et al. [15] demonstrated that segment-wise and
condition-wise splitting inflate reported performance, proposed bearing-wise splitting, and
identified the number of training bearings as key to generalisation; Knap et al. [16] proposed a
leakage-safe, recording-level cross-domain benchmark and reported that deep models require
repeated seeds. **We claim no novelty for these observations**; we do not re-derive them.

What the prior work does not provide is a quantified account, for the healthy-data-only setting,
of how far a reported *false-alarm rate* can be trusted and what would improve it. That is the
gap this paper addresses, and §3 states the boundary of each claim made against it.

---

## 5. Discussion

### 5.1 Why holding out a physical unit changes the number so much

When test recordings come from bearings the detector was fitted on, the detector has
effectively seen that bearing's baseline level. When the whole bearing is held out, the
threshold must generalise across bearings, and the healthy recordings of the new bearing sit at
a different operating point. In our data the between-bearing spread is substantial: per-bearing
mean RMS ranges from 0.17 to 0.40 on the Paderborn healthy set. The reported false-alarm rate is
therefore dominated by *which physical units* the split keeps apart, well before any question of
model choice arises.

This is consistent with prior work that identified leakage from segment- and condition-wise
splitting and proposed bearing-wise splitting [15], and with recording-level separation in
cross-domain benchmarking [16]. We claim no novelty for the observation that leakage inflates
apparent performance. Our contribution is that the same effect, measured on the *false-alarm
rate* under healthy-data-only training, moves the number by an order of magnitude, and that it
can be quantified in a single controlled comparison.

### 5.2 Why the unit effect disappears for some detectors

The unit effect is clear for two detectors and absent for the third, and the reason is
saturation rather than disagreement. With a single training bearing the Mahalanobis detector
alarms on 67–100% of the healthy recordings of a different bearing, and in one cell on 100%
exactly — the metric has no room left to vary, so its spread collapses to zero and the question
"does the spread decrease?" becomes undefined.

This matters beyond bookkeeping. A detector that is saturated cannot be evaluated by its
false-alarm rate at all, because the rate has reached its ceiling; reporting such a number is not
wrong so much as uninformative. We therefore state the unit effect as holding *for non-saturated
detectors*, and treat saturation as a scope condition rather than a failure to report.

An alternative reading of the Mahalanobis result is also plausible: with four features and about
twenty windows, the empirical covariance is itself poorly estimated, so the saturation may
reflect estimator instability rather than a property of the detector family. Both readings lead
to the same practical conclusion for this configuration, and we do not claim to separate them.

### 5.3 The healthy/degraded boundary is a free parameter

For run-to-failure data there is no onset label: the split between healthy and degraded data is
chosen by the analyst, and whatever is chosen becomes the ground truth against which false
alarms are counted. The boundary alone moves the reported uncertainty by 2.4–5.2 percentage
points, and the same rule can bind on opposite sides in different datasets — a floor of 20
windows in one, a cap of 60 in the other.

We emphasise what this is *not*. It is not a claim that any particular boundary is wrong, and it
is not a new method for finding degradation onset; detecting the first prediction time is an
established problem with a substantial literature, and our rule is drawn from that convention.
Our claim is narrower and more immediately useful: the boundary is a reporting parameter, and its
influence on the reported number should be measured and disclosed, exactly as one would disclose
a threshold or a split.

### 5.4 A checklist rather than a method

The practical output of this study is the five-point checklist in §3.5. It requires no new model
and no additional data collection beyond what a careful practitioner would already have; it
changes only what is reported. Read against the observed effect sizes, the consequences are
concrete: a study that reports a single within-bearing number may present a detector with a 40%
false-alarm rate as having none; a study that reports a single training size may present a number
that is an artefact of its split; and a study that does not disclose its healthy/degraded
boundary may present a number that moves by several percentage points under a defensible
alternative.

### 5.5 What would change our conclusions

1. If the scope effect fails to reproduce on a rig whose bearings are more uniform, the
   order-of-magnitude framing would have to be restricted to rigs with strong between-bearing
   variation.
2. If the unit effect is shown to arise from the covariance estimator rather than from unit
   diversity, the recommendation would shift from "more bearings" toward better-regularised
   estimators.
3. If the boundary sensitivity proves negligible for other rules and datasets, the boundary would
   remain a reporting detail rather than a first-order parameter.
4. If a prospective, self-collected dataset contradicts any of the above, that dataset takes
   precedence — none of our evidence is from our own hardware.

---

## 6. Limitations

1. All evidence is from public datasets (IMS, MFPT, Paderborn, XJTU-SY, PRONOSTIA); no
   self-collected data.
2. Few independent units: 6 (Paderborn), 15 (XJTU-SY), 17 (PRONOSTIA); the unit effect is
   estimated from 3–4 bearings per cell within a condition.
3. One detector family: all detectors use a quantile of the training score distribution; the
   Mahalanobis result is reported as not testable.
4. The healthy-phase rule was chosen by us and is defended by a sensitivity sweep, not by an
   external label.
5. Confounds are disclosed rather than removed: in the XJTU-SY boundary sweep the rule also
   changes which bearings qualify; the cross-condition unit comparison is confounded with
   operating-condition diversity.
6. Verification is not uniform: four experiments were re-run and compared hash-for-hash; older
   experiments have invariant and recomputation checks plus a stored hash baseline only.
7. Literature scope: the search covered Scopus and arXiv; Chinese-language venues and PHM
   conference proceedings are not comprehensively covered. References [11] and [13] are cited
   at title level only because their abstracts were not retrievable.

---

## 7. Conclusion

The practical reliability of a false-alarm rate in healthy-data-only bearing anomaly detection is
set less by the detector than by three choices the analyst makes: whether evaluation keeps
physical units apart, how many independent units enter training, and where healthy data end.

The decisive evidence is comparative. Holding out whole bearings moved the reported rate by an
order of magnitude (0.00% to 40.63%) on the same detector and the same data. At a fixed sample
size, adding distinct training bearings halved the spread for two detectors, while the third
saturated at 67–100% false alarms and became uninformative rather than unstable. Sweeping the
healthy/degraded boundary moved the reported uncertainty by 2.4–5.2 percentage points without
any change to the detector.

We do not claim a new detector, a new method for locating degradation onset, or generality beyond
the rigs studied. All evidence is from public datasets; none comes from our own hardware, and a
prospective self-collected study is the natural next test.

---

## Figure 1 caption

**Fig. 1 | Three faces of evaluation uncertainty in healthy-data-only bearing anomaly detection.**
**(a)** Evaluation scope. With detector, threshold and data fixed, holding out whole bearings
raises the reported false-alarm rate from 0.00% (within-bearing) to 40.63% (bearing-level
holdout; folds 0.4–97.1%). **(b)** Independent units. At a fixed budget of 20 recordings, drawing
training bearings from a single bearing yields SD 23–38 pp and mean false-positive rates of
43–58%, whereas four bearings yield SD 8–14 pp; the effect holds for 3σ RMS and Isolation Forest
(6 of 6 operating conditions each) but not for the Mahalanobis detector, which saturates at 67–
100% false alarms and is therefore not testable this way. **(c)** Definition. Run-to-failure data
carry no onset label, so the healthy/degraded boundary is an analyst choice; across five
boundary rules the SD of the reported rate ranges over 2.40 pp on PRONOSTIA (inclusion set
unchanged) and 5.19 pp on XJTU-SY (inclusion set changes with the rule). **(d)** Reporting
checklist. Rendered with matplotlib; collision and typography audits passed (§3.5).

---

## Data-set citations (footnote material)

- Paderborn: Lessmeier et al. (2016), PHM Society European Conference, doi:10.36001/phme.2016.v3i1.1577.
- IMS: Lee, J., Qiu, H., Yu, G., Lin, J., & Rexnord Technical Services (2007). IMS, University of
  Cincinnati. "Bearing Data Set", NASA Prognostics Data Repository, NASA Ames Research Center,
  Moffett Field, CA.
- MFPT: *Bearing Fault Data*, Society for Machinery Failure Prevention Technology, distributed via
  MathWorks. **The official citation format for this data set could not be confirmed**; the
  source is therefore attributed to the distributing organisation rather than to an original
  publication.
- XJTU-SY: Wang, B., Lei, Y., Li, N., & Li, N. (2020). A hybrid prognostics approach for
  estimating remaining useful life of rolling element bearings. *IEEE Transactions on
  Reliability, 69*(1), 401–412.
- PRONOSTIA: IEEE PHM 2012 Data Challenge, FEMTO-ST Institute.