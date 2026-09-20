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
it. Using five public bearing sources under a pre-registered protocol, we find that three
analyst choices each move the reported false-alarm rate substantially. We measure each on its
own estimand, on overlapping but different data, and we make no ordering claim between them or
against detector choice.
Holding out whole bearings, rather than only held-out recordings, moved the same detector's
reported rate from a single deterministic evaluation with zero alarms in 24 recordings to a
bimodal set of fold means, three at or below 1.55% and three at or above 69.40%. At a fixed sample size, whether the reported rate looks stable depends on how cross-fold variation is defined and estimated: under the pooled definition the spread falls for two of the three detectors in every condition, but under between-fold variation the preregistered 80% stability criterion is not met (2 of 6 conditions for Isolation Forest, 4 of 6 for the 3σ RMS threshold, and 0 of 6 for the third detector, which saturates).
Moving the healthy/degraded boundary, a choice that run-to-failure data leave to the analyst,
shifted the reported uncertainty by 2.40 percentage points on PRONOSTIA, where the set of
admissible bearings is identical under all five rules. On XJTU-SY the same sweep gave 5.19
percentage points, but there the rule also changes which bearings qualify and k_max varies from
11 to 14, so that figure mixes the boundary effect with a unit-count effect; we therefore
restrict the boundary claim to the PRONOSTIA measurement. We give a five-point reporting checklist and state
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

**Datasets.** IMS `1st_test` (12 healthy recordings — the files carrying the `2003.10.22*` name prefix, out of the 15 in the archive — 20 kHz, 1.024 s), IMS `2nd_test` and
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
change, a separate amendment was filed rather than the original being edited. Two variability definitions appear below and are kept apart throughout: the pooled SD over all fold × repeat evaluations stored in the summary CSVs, and the between-fold SD of per-fold mean rates. Section 3.1 uses the between-fold definition; Section 3.2 reports both and says which verdict depends on which. The project's protocol grades evidence A–D; no claim in this paper reaches Level A, since every measurement comes from a single rig or a single split, and exploratory checks are labelled as such. Four of the experiments carrying the main claims
were re-run and compared hash-for-hash with their archived outputs (§3.5).

---

## 3. Results: three faces of evaluation uncertainty

### 3.1 Scope: does the split keep physical units apart?

Using the same detector (Isolation Forest, 200 trees, max_samples 0.5), the same threshold
rule (0.99 quantile of the training scores) and the same dataset (Paderborn condition
N15_M07_F10), we compared two evaluation scopes over the six healthy bearings
(EXP-V2-03; `experiments/EXP-V2-03-summary.csv`, regime `R2_bearing_holdout`, arm `S2_new_records`):

| Scope | Training used | Test used | Reported false-alarm rate |
| --- | --- | --- | ---: |
| within-bearing | recordings 1–16 of each bearing | recordings 17–20 of *the same* bearings | **0.00%** |
| bearing-level holdout | all recordings of five bearings | all recordings of *the held-out* bearing | **bimodal**: three folds at or below 1.55% (0.00, 0.40, 1.55) and three at or above 69.40% (69.40, 75.35, 97.10); mean 40.63%, median 35.5%, between-fold SD 44.8 pp |

The two scopes are not equally replicated and we state this plainly. In the new-records arm of the within-bearing scope the training budget of 96 recordings equals the entire training pool, so the draw is the identity and the 0.00% figure is a single deterministic evaluation rather than a distribution; the resampling arm at the same nominal size does not coincide in that way, and its within-bearing replicates vary (mean 4.96%, SD 12.1 pp). That figure is 0 alarms in 24 test recordings, which gives a resolution of 4.17
percentage points and an exact one-sided 95% upper bound of 11.7%; the increase is therefore **at least** about
3.5-fold. This is a lower bound only: zero alarms in 24 recordings is also consistent with true
rates well below the 11.7% bound, so ratios larger than ten cannot be excluded. The holdout arm is replicated over six physical units, and its between-fold spread is large (SD 44.8 pp). A bootstrap 95% interval for the mean of the six fold rates spans 12.0 to 72.7 percentage points (10,000 resamples over folds, fixed seed; `experiments/EXP-STATS-bootstrap-permutation.csv`).

We also report a preregistered criterion that failed. The experiment registered a primary
comparison in which the new-records arm would show a smaller spread than a resampling arm at the
same nominal size. That criterion held in 2 of 6 folds, because the resampling arm saturates:
in three folds it alarms on every held-out recording and its spread is exactly zero, which is
degenerate stability rather than a good result. The comparison reported here is therefore the
new-records arm, and the saturation of the resampling arm is recorded as a separate failure mode
rather than as evidence for the scope effect.

*Boundary*: one rig, six physical units, one operating condition, one detector. The direction is
unambiguous; the magnitude depends on the depth of the split and should not be transferred
without repeating the comparison.

### 3.2 Units: how many independent bearings were used for training?

Holding the sample size fixed at 20 recordings and restricting training bearings to the **same operating condition** as the held-out bearing (EXP-V2-05 for the Isolation Forest row, EXP-V2-06 for the 3σ RMS and Mahalanobis rows;
`experiments/EXP-V2-05-summary.csv`, `EXP-V2-06-summary.csv`):

| Detector | Negative rank correlation between k and SD | SD(k_max) < SD(k=1), pooled SD | k=1 mean FP |
| --- | ---: | ---: | ---: |
| 3σ RMS threshold | **6/6** | **6/6** | 23.7–49.5% (SD 33.0–48.2 pp) |
| Isolation Forest (200, 0.5) | **6/6** | **6/6** | 16.9–57.6% (PRONOSTIA 16.9–21.5%, XJTU-SY 54.5–57.6%; SD 23.9–44.4 pp) |
| Mahalanobis distance | 2/6 | 2/6 | **66.8–100%** (one cell exactly 100%; SD 0.0–35.4 pp) |

SD in this table is the pooled standard deviation over the fold × repeat evaluations stored in the summary CSVs, not the between-fold SD of Section 3.1. The verdicts depend on that choice: recomputing the same cells as the SD of per-fold mean rates gives 2 of 6 for Isolation Forest, 4 of 6 for 3σ RMS and 0 of 6 for Mahalanobis (`REVIEW_round4_sd_definition_check2.txt`), so under the between-fold definition both non-saturated detectors fall short of the 80% share their preregistration required, and the saturated detector is excluded either way. We report both readings, and the claim we make here is the weaker one: with this little healthy data, the stability of detector performance depends on how cross-fold variation is defined and estimated, and evaluated by between-fold variation the preregistered 80% stability criterion is not met. The pooled reading is reported as a sensitivity, not as the result. A permutation test on the between-fold spread (10,000 permutations over fold-level rates) does not separate k = 1 from k_max for either non-saturated detector (Isolation Forest p = 0.18, 3σ RMS p = 0.51) and separates the saturated detector in the opposite direction (p < 0.001); the same file carries these tests. One conclusion survives both definitions: training on a single bearing is unreliable. At k = 1 the mean false-alarm rate on a different bearing is 16.9–57.6% for Isolation Forest and 23.7–49.5% for the 3σ RMS threshold, and those cells carry the largest per-cell spread of the sweep.

For the two non-saturated detectors, and under the pooled definition, going from one training bearing to k_max reduces the standard deviation of the reported rate **at a fixed number of recordings**. The measured
per-cell ratios SD(k_max)/SD(k=1) are 0.76, 0.75, 0.67, 0.68, 0.91 and 0.55 for 3σ RMS and 0.32,
0.57, 0.34, 0.58, 0.86 and 0.52 for Isolation Forest, that is a reduction of roughly 10 to 45
percent for the first detector and 14 to 68 percent for the second, not a uniform halving.

The rate in this table is computed over the windows of the held-out bearing, and the number of scored windows differs between folds, so per-evaluation resolution is not constant across cells — the stored values imply denominators of 60, 30, 20 and 15 windows in the PRONOSTIA cells and 20, 10 and 5 in the XJTU-SY cells. Cells are therefore compared on the SD scale rather than on absolute rates.

*Boundary*: the bearings left in a condition after the healthy-phase rule number 7, 7 and 3 for the three PRONOSTIA conditions and 4, 4 and 5 for the three XJTU-SY conditions. One is held out for
testing and the record budget is fixed at 20 (five recordings per bearing), so the sweep stops at the smaller of the bearings available in the condition and four training bearings: k_max = 4, 4, 2 for the three PRONOSTIA conditions and 3, 3, 4 for the three XJTU-SY conditions, and the ratios above are taken at those points. The record budget is the binding constraint in three cells (PRONOSTIA C1 and C2, XJTU-SY 40Hz10kN); in the other three (PRONOSTIA C3, XJTU-SY 35Hz12kN and 37.5Hz11kN) the number of bearings left in the condition binds instead, after one is held out for testing. The criterion
for "decreases" is the rank correlation between k and the SD, not strict monotonicity; one cell
is non-monotone (XJTU-SY 40Hz10kN rises from 20.02 pp at k=3 to 20.69 pp at k=4), so under
strict monotonicity Isolation Forest would be 5 of 6 rather than 6 of 6. The Mahalanobis
exclusion is not a pre-defined saturation rule but a reclassification of a preregistered
criterion that failed (Z1 and Z2 both 2 of 6 against a required 80 percent). The detector
saturates at k = 1 (one cell is exactly 100%), so its
spread is degenerate and the unit effect is **not testable in this form**; we report it as such
rather than as a failure. The wider cross-condition comparison is confounded with
operating-condition diversity and is therefore not used for the claim above.

### 3.3 Definition: where does "normal" end?

Run-to-failure datasets carry no onset label. We froze one rule (H = clip(max(20, 0.10·N), 20,
60), requiring H/N ≤ 0.25) and swept five variants (fraction 5/10/20%, floor 10/20/30) on two independently collected run-to-failure datasets (EXP-V2-04; the per-rule result is recorded with its rule labels in `experiments/EXP-V2-04-xjtu-pronostia.md` §3, while the archived CSVs carry the main and sensitivity arms without a rule column):

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
holding out one MFPT healthy recording) did not reproduce in any **independent** fold: 0 of 26 (EXP-V1-06 and EXP-V1-07; `experiments/EXP-V1-07-folds.csv`). The single
occurrence (MFPT, holding out `baseline_3.mat`, ratio 1.576) is the same fold in which the
effect was originally observed, with the same scheme and the same 22 training windows, so it is
the original case re-evaluated rather than an independent reproduction. IMS contributes 0 of 24
folds and MFPT 0 of 2 further folds. The count is defined on the empirical-covariance scheme and
the RMS plus spectral-centroid feature group; other schemes give a different fold count. A power analysis gave the original comparison a power of
0.087, so the appropriate reading is *underpowered and undetermined*, not *refuted*.

### 3.5 Reproducibility of these results

Verification depth differs by experiment and we state it per experiment. EXP-V2-03, EXP-V2-04, EXP-V2-05 and EXP-V2-06 were re-run and reproduced byte-for-byte. EXP-V1-10 reproduced exactly on all scientific
columns (only its wall-clock timing column differed). EXP-V1-05 to V1-09 passed invariant and
independent-recomputation checks with a stored hash baseline. For EXP-V1-11, EXP-V2-01 and EXP-V2-02 no archived verification record could be located while preparing this draft: the project's verification script covers EXP-V1-05 to EXP-V1-10 only, and the hash baselines on file belong to EXP-V1-05 to V1-10, EXP-V2-04 and EXP-V2-05. We therefore make no verification claim for those three experiments. The experiment carrying §3.1 (EXP-V2-03) has since been re-run and reproduced byte-for-byte on all scientific columns (`experiments/EXP-V2-03-hashes.txt`). Analysis errors were found and corrected during the study; the project keeps a standing register of the classes involved (`docs/EXPERIMENT_AFTERCARE.md`, an internal working-tree document). They lie in summary, verdict and verification logic and in data handling such as seed derivation and file counting; none lies in the model fitting itself.

### 3.6 The evaluation protocol itself

The checklist below is not a recommendation drawn from first principles; it follows from four
measurements on the small-sample regime that healthy-data-only monitoring actually occupies.

**The selection criterion is often non-discriminative.** On IMS `1st_test` (12 healthy
recordings, 84 windows of 0.25 s, 20 kHz), with a fixed test set of two recordings (14 windows)
and 50 resamples of a 7-file fit and 3-file validation split, the minimum validation false-alarm rate was exactly zero in 84% of the archived design-A Isolation Forest replicates, and at least two candidate configurations tied at that minimum in 92% (`experiments/EXP-V1-10-arm-extras.csv`; the per-replicate file carries no arm label, so the R = 50 and R = 200 arms are pooled). Twenty-one validation windows cannot resolve differences below about 4.8
percentage points, which is the same order as the 1% false-alarm level the detector is trying to
control. A nested leave-one-file-out protocol on the same data had already given a modal
configuration share of 33%.

**The reported rate has a noise floor.** With the test set held fixed, so that test-set sampling
contributes no variance, the reported rate took the values 0.00%, 7.14% and 14.29% across the 50
resamples (mean 3.86%, SD 4.13 pp). Decomposing that variation at the modal configuration gave
SD 5.20 pp when the training composition changed and 4.39 pp when only the random seed changed,
The decomposition contains no hyperparameter component because it is computed at the modal
configuration, which holds the configuration fixed by construction; we therefore make no claim
about the size of the hyperparameter contribution. The third measured component, in which
training composition and seed vary together, has SD 5.18 pp.

**Resampling is not a substitute for data.** On the Paderborn bearings, and under the
within-bearing scope identified in §3.1 as the optimistic one, increasing the nominal training
size from 20 to 96 recordings by resampling the same 20 left the SD at 18.0 pp, whereas using 96
distinct recordings reduced it to 0.00 pp. The second figure is a quantisation floor, since every
draw produced 0 alarms in 24 test recordings, and it must be read together with §3.1, where the
same nominal size under a bearing-level holdout leaves fold rates between 0.00% and 97.10%. The effect is visible in the accuracy of the
estimator as well: expressed as an effective sample size q(1-q)/SD^2 against the ideal independent-window
reference, the resampling arm stayed between 0.18 and 0.38 while the distinct-recording arm
passed 430; cells in which the SD was exactly zero are excluded from that range.

**Search cost and stability trade off.** With hyperparameters selected inside the training data,
Isolation Forest met a pre-set 5% false-alarm target in 3 of 3 IMS batches but needed roughly
10^5 times the search cost of a 3σ RMS threshold and selected the same configuration in 33, 100 and 50 percent of folds across the three batches; a
one-class SVM met the target in 0 of 3. The batch means were 1.19, 4.76 and 2.38 percent, one of
which clears the cut by 0.24 percentage points, and single-fold resolution is about 14.3
percentage points, so the 5 percent value is an operational cut for the comparison rather than a
performance expectation.

**Reporting checklist**

1. Report the number of training windows behind the threshold, not the dataset size — and where the budget is set in recordings, say how many windows each recording contributes.
2. Report resampling variability from at least two sources — split composition and random seed — and state how that variability is estimated (pooled across evaluations or between folds), since the two definitions can reverse the verdict.
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
of how far a reported false-alarm rate can be trusted and what would improve it. Three
increments over [15] and [16] are defensible and we restrict ourselves to them. First, the
endpoint is the false-alarm rate under healthy-only training, not classification performance on
labelled faults, so the quantity under study is the one that decides deployment. Second, the
unit effect is measured inside a single operating condition with the record budget held fixed,
which separates the number of independent units from operating-condition diversity; [15]
identifies the number of training bearings as important for generalisation but does not isolate
it that way. Third, saturation is reported as an evaluation failure mode in its own right, since
a detector that alarms on 67 to 100% of healthy recordings has no measurable spread and cannot be
assessed by this metric at all. The remaining content of §3.1 and §3.2 should be read as
quantification of phenomena that [15] and [16] already established, not as their discovery.

---

## 5. Discussion

### 5.1 Why holding out a physical unit changes the number so much

When test recordings come from bearings the detector was fitted on, the detector has
effectively seen that bearing's baseline level. When the whole bearing is held out, the
threshold must generalise across bearings, and the healthy recordings of the new bearing sit at
a different operating point. In our data the between-bearing spread is substantial: per-bearing
mean RMS ranges from 0.171 to 0.403 on the Paderborn healthy set (`experiments/EXP-V2-03-per-bearing-rms.csv`). The reported false-alarm rate is
therefore dominated by *which physical units* the split keeps apart, well before any question of
model choice arises.

This is consistent with prior work that identified leakage from segment- and condition-wise
splitting and proposed bearing-wise splitting [15], and with recording-level separation in
cross-domain benchmarking [16]. We claim no novelty for the observation that leakage inflates
apparent performance. Our contribution is that the same effect, measured on the *false-alarm
rate* under healthy-data-only training, moves the number from no alarms to about 40%, and that it
can be quantified in a single controlled comparison. Because the within-bearing figure is a single deterministic evaluation with a resolution of 4.17 percentage points, the increase is at least about 3.5-fold; zero alarms in 24 recordings does not bound it from above (§3.1).

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

An alternative reading of the Mahalanobis result is also plausible: with four features and a
training budget of twenty recordings, each contributing a single feature vector, the empirical
covariance is itself poorly estimated, so the saturation may
reflect estimator instability rather than a property of the detector family. Both readings lead
to the same practical conclusion for this configuration, and we do not claim to separate them.

### 5.3 The healthy/degraded boundary is a free parameter

For run-to-failure data there is no onset label: the split between healthy and degraded data is
chosen by the analyst, and whatever is chosen becomes the ground truth against which false
alarms are counted. On PRONOSTIA, where all five rules admit the same 17 bearings, the boundary
alone moves the reported uncertainty by 2.40 percentage points; the XJTU-SY sweep gives 5.19
percentage points, but there the rule also changes which bearings qualify, so that figure is not a
clean boundary effect. The same rule can bind on opposite sides in different datasets — a floor of
20 windows in one, a cap of 60 in the other.

We emphasise what this is *not*. It is not a claim that any particular boundary is wrong, and it
is not a new method for finding degradation onset; detecting the first prediction time is an
established problem with a substantial literature, and our rule is drawn from that convention.
Our claim is narrower and more immediately useful: the boundary is a reporting parameter, and its
influence on the reported number should be measured and disclosed, exactly as one would disclose
a threshold or a split.

### 5.4 A checklist rather than a method

The practical output of this study is the five-point checklist in §3.6. It requires no new model
and no additional data collection beyond what a careful practitioner would already have; it
changes only what is reported. Read against the observed effect sizes, the consequences are
concrete: a study that reports a single within-bearing number may present a detector with a 40%
false-alarm rate as having none; a study that reports a single training size may present a number
that is an artefact of its split; and a study that does not disclose its healthy/degraded
boundary may present a number that moves by several percentage points under a defensible
alternative.

### 5.5 What would change our conclusions

1. If the scope effect fails to reproduce on a rig whose bearings are more uniform, the 3.5-fold lower bound would have to be restricted to rigs with strong between-bearing variation.
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
2. The binding constraint is the number of publicly available independent healthy units, not the volume of healthy data: Paderborn contributes 6 healthy bearings in total and 3–7 per operating condition after the healthy-phase rule, XJTU-SY 15 and PRONOSTIA 17, so the unit effect rests on 3–4 bearings per cell. Adding recordings to the same units does not help (§3.6); adding units would require pooling datasets with different acquisition chains or new hardware.
3. One detector family: all detectors use a quantile of the training score distribution; the
   Mahalanobis result is reported as not testable.
4. The healthy-phase rule was chosen by us and is defended by a sensitivity sweep, not by an
   external label.
5. Confounds are disclosed rather than removed: in the XJTU-SY boundary sweep the rule also
   changes which bearings qualify; the cross-condition unit comparison is confounded with
   operating-condition diversity.
6. Verification is not uniform: four experiments were re-run and compared hash-for-hash; older
   experiments have invariant and recomputation checks plus a stored hash baseline only.
7. The experiment carrying the scope effect (§3.1) was re-run on 2026-09-21 and reproduced on all scientific columns; the record is in `experiments/EXP-V2-03-hashes.txt`.
8. Literature scope: the search covered Scopus and arXiv; Chinese-language venues and PHM conference proceedings are not comprehensively covered. References [11] and [13] are cited at title level only because their abstracts were not retrievable.
9. Window construction is fixed in the frozen protocol for IMS and MFPT only; for Paderborn, PRONOSTIA and XJTU-SY it is defined in the experiment code.
10. The rates in §3.2 are window-level and their resolution differs between folds, so absolute rates are not directly comparable across cells; the comparisons are made on the SD scale.

---

## Data and code availability

The experiment registry, preregistrations, scripts, run logs, per-fold CSVs, hash files and figures
behind this paper are archived under `experiments/` and `docs/` of
`github.com/Jay-zhou114514/motor-health-monitor`, using the naming convention `EXP-V1-0X` /
`EXP-V2-0X`; the manuscript sources, claim-to-evidence map and review records are in
`github.com/Jay-zhou114514/motor-health-monitor-papers` under `conference-track/`. Paths of the form
`docs/…` and `experiments/…` cited in the text are paths inside the first repository, and
`docs/EXPERIMENT_AFTERCARE.md` is an internal working-tree document rather than a published
artefact. All five datasets are third-party public datasets used under their own terms: IMS (NASA
Prognostics Data Repository), MFPT (distributed by MathWorks), Paderborn (doi above), XJTU-SY (Wang
et al., 2020) and PRONOSTIA (IEEE PHM 2012 Data Challenge, FEMTO-ST). No new data were generated.
The AI-use disclosure required by the target venue is maintained in `docs/AI_USE_DISCLOSURE.md`.

---

## 7. Conclusion

The practical reliability of a false-alarm rate in healthy-data-only bearing anomaly detection is
affected by three choices the analyst makes, each of which we quantify here: whether evaluation
keeps physical units apart, how many independent units enter training, and where healthy data
end.

The decisive evidence is comparative. Holding out whole bearings moved the reported rate from no
alarms to 40.63% on the same detector and the same data; because the within-bearing figure is a single deterministic evaluation with 4.17-percentage-point resolution, the increase is at least about 3.5-fold. At a fixed sample size, whether the detectors look stable depends on how cross-fold variation is defined and estimated. Under the pooled SD the spread of the reported rate fell in every condition for two detectors, by 10–45% and 14–68%; under between-fold variation the preregistered 80% criterion is met in neither, at 2 of 6 and 4 of 6, and the third detector saturated at 67–100% false alarms. We therefore report detector stability in this setting as definition-dependent rather than as an established improvement. Sweeping the
healthy/degraded boundary moved the reported uncertainty by 2.40 percentage points on PRONOSTIA,
where the admissible bearing set is unchanged; the larger XJTU-SY figure mixes the boundary effect
with an inclusion effect.

We do not claim a new detector, a new method for locating degradation onset, or generality beyond
the rigs studied. All evidence is from public datasets; none comes from our own hardware, and a
prospective self-collected study is the natural next test.

---

## Figure 1 caption

**Fig. 1 | Three faces of evaluation uncertainty in healthy-data-only bearing anomaly detection.**
**(a)** Evaluation scope. With detector, threshold and data fixed, holding out whole bearings
raises the reported false-alarm rate from 0.00% (within-bearing) to 40.63% (bearing-level
holdout; fold means 0.00 to 97.10 percent). **(b)** Independent units. At a fixed budget of 20 recordings, drawing
training bearings from a single bearing yields mean false-alarm rates of 16.9–57.6% for
Isolation Forest and 23.7–49.5% for 3σ RMS (SD 23.9–44.4 pp and 33.0–48.2 pp respectively),
whereas using every training bearing available in the cell (k_max between 2 and 4, depending on
the condition) reduces the spread; the effect holds for 3σ RMS and Isolation Forest under the pooled SD definition (6 of 6 conditions) but not under between-fold variation (4 of 6 and 2 of 6), so the preregistered 80% stability criterion holds only under the pooled reading; the Mahalanobis detector saturates at 67–
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