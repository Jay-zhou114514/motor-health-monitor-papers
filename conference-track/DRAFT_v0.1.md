# Conference Draft v0.1（2026-09-18）

> 说明：本稿只写**证据已完全确定**的部分（Abstract / Introduction / Protocol / Results）。
> Related Work 与 Discussion 待写；每句话的依据见 `CLAIM_EVIDENCE_MAP.md`。
> 所有数字直接取自 Master 仓库的 CSV，未做任何再加工。

---

## Title

**Nominal Sample Size Is Not Effective Information: Reporting Uncertainty in
Healthy-Data-Only Bearing Anomaly Detection**

## Abstract

Bearing condition monitoring is often deployed with only healthy data available for
training, and the alarm threshold is estimated from a quantile of the training score
distribution. We ask how much a reported false-alarm rate can be trusted under this
setting, and whether collecting more healthy data improves it. Using two public test
rigs (IMS; Paderborn, K001–K006) and a frozen protocol, we find that (i) at ten healthy
recordings the training-internal selection criterion was non-discriminative in 92% of
resamples, with the minimum validation false-alarm rate exactly zero in 86%; (ii) with
the test set held fixed, the reported false-alarm rate still varied between 0% and
14.3% (SD ≈ 4 pp), driven in comparable measure by *which* recordings were used for
training (SD 5.20 pp) and by the detector's random seed (SD 4.39 pp); (iii) increasing
the *nominal* training size by resampling the same recordings did not reduce this
uncertainty (SD 18.0 pp at n = 96), whereas using 96 *distinct* recordings reduced it to
0.0 pp; and (iv) across four operating conditions the direction held in 3/4 cases but
the required number of recordings varied (80–96). We conclude that in this regime the
reported false-alarm rate carries a noise floor far above classical expectations, that
nominal sample size is not effective information, and we give a five-point reporting
checklist.

## 1. Introduction

Low-cost machine condition monitoring is typically deployed in the regime where only
healthy-machine data are available: acquiring run-to-failure data is expensive, and
faults are rare. A common and reasonable design is therefore to fit a one-class model
(or a simple statistic) on healthy data, set the alarm threshold at a high quantile of
the training score distribution, and report the resulting false-alarm rate on held-out
healthy recordings.

That reported number is what an operator uses to decide whether the monitor is
deployable. The question we address is not which detector is most accurate, but:
**how much can this number be trusted, and does collecting more healthy data help?**

We structure the study around three questions:

1. At realistic sample sizes, can a training-internal selection criterion distinguish
   between candidate configurations?
2. With the test set held fixed, how much does the reported false-alarm rate vary?
3. Does increasing the nominal training size reduce that variation?

## 2. Protocol

Datasets. IMS `1st_test` (12 healthy recordings, 20 kHz, 1.024 s), IMS `2nd_test` and
`4th_test` (6 recordings each), Paderborn K001–K006 (6 healthy bearings; four operating
conditions, 20 recordings each, vibration channel at 64 kHz, 4 s), and MFPT (three
healthy recordings plus labelled faults, 97.656 kHz). Independent units are test rigs and
physical bearings, never windows.

Features and detectors. Four frozen features (`rms`, `crest_factor`, `kurtosis`,
`centroid_hz`). Four detectors with different risk profiles: a 3σ RMS threshold, the
Mahalanobis distance, an RBF one-class SVM, and Isolation Forest. The alarm threshold is
always the 0.99 quantile of the *training* score distribution; the test set never
participates in any selection.

Discipline. Every experiment was pre-registered before it was run; when a criterion had
to change, a separate amendment was filed. Evidence is graded A–D and exploratory
analyses are labelled as such.

## 3. Results

### 3.1 What does not reproduce

A covariance-geometry failure observed on a single fold (inflation ratio 1.576 when
holding out one MFPT healthy recording) did not reproduce: across 27 folds spanning
MFPT and three IMS batches, exactly one fold showed the effect (MFPT 1/3, IMS 0/24).
A follow-up power analysis gave the original test a power of 0.087, so the correct
reading is "underpowered, undetermined" rather than "refuted".

### 3.2 The selection criterion at small sample sizes

On IMS `1st_test` with a fixed two-recording test set and repeated 7-fit / 3-validation
resampling (R = 50), the minimum validation false-alarm rate was exactly zero in 86% of
resamples and at least two candidate configurations tied at that minimum in 92%. The
selected configuration was therefore frequently determined by the tie-breaking rule
rather than by validation performance. An independent nested leave-one-file-out protocol
on the same data had already shown a modal configuration share of 33%.

### 3.3 The noise floor and its sources

With the test set held fixed — so that test-set sampling contributes no variance — the
reported false-alarm rate still ranged over 0%, 7.1% and 14.3% across resamples
(SD 4.13 pp, mean 3.86%). Decomposing this variation, changing which recordings formed
the training set gave SD 5.20 pp, while changing only the Isolation Forest random seed
gave SD 4.39 pp (ratio 1.18); restricting to the 44 resamples that selected the modal
configuration still left SD 3.58 pp. Hyperparameter choice therefore accounts for only a
small part of the spread.

Two control conditions bound this: with the threshold re-estimated on the same 50
splits, the 3σ RMS detector produced zero false alarms in every split, whereas the
untuned default Isolation Forest showed essentially the same spread as the tuned one
(SD 3.34 pp).

### 3.4 Nominal sample size versus effective information

The central result comes from contrasting two ways of increasing the nominal training
size, both evaluated on the same fixed 24-recording test set.

| Nominal n | Resampled (same 20 recordings) | Distinct new recordings |
| ---: | ---: | ---: |
| 10 | SD 23.4 pp | SD 7.2 pp |
| 20 | SD 16.6 pp | SD 4.7 pp |
| 40 | SD 16.1 pp | SD 2.1 pp |
| 60 | SD 18.2 pp | SD 0.99 pp |
| 80 | SD 17.9 pp | SD 0.48 pp |
| 96 | **SD 18.0 pp** | **SD 0.00 pp** |

Resampling the same twenty recordings up to ninety-six times left the reported
false-alarm rate essentially as uncertain as it was at twenty; using ninety-six distinct
recordings reduced the spread to the quantisation floor. Expressed as effective sample
size (n_eff = q(1−q)/SD²), the resampling arm stayed between 0.18 and 0.38 while the
distinct-recording arm grew past 430. Across four operating conditions the direction
held in 3 of 4, and reaching SD ≤ 1 pp required 80–96 recordings rather than 60.
The classical 1/√n law was wrong in both directions: too optimistic on the resampling
arm (observed/ideal 4–13×) and too conservative on the distinct-recording arm
(efficiency above 1).

### 3.5 Simple versus modern detectors

On held-out healthy IMS recordings the 3σ RMS threshold produced a false-alarm rate of
2.38% in all three batches, while the fixed-hyperparameter one-class SVM produced 27–50%.
With hyperparameters selected inside the training data, Isolation Forest met a pre-set
5% target in 3/3 batches but required roughly 10⁵ times the search cost and selected the
same configuration in only 33% of folds; the one-class SVM met the target in 0/3.

## 4. Related Work

*(to be written — see `CLAIM_EVIDENCE_MAP.md` §5 for the required positioning)*

## 5. Discussion and reporting checklist

*(to be written)*

## 6. Limitations

*(to be written — mirror `CLAIM_EVIDENCE_MAP.md` §4)*