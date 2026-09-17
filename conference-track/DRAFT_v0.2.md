# Conference Draft v0.2（2026-09-18）
# §4–§7（Related Work / Discussion / Limitations / Conclusion）

> §1–§3（Abstract / Introduction / Protocol / Results）见 `DRAFT_v0.1.md`，合并留到投稿整理阶段。
> 引用编号对应 `REFERENCES.md`；未列入该文件的文献不得出现在本稿中。

---

## 4. Related Work

### 4.1 Healthy-data-only monitoring with quantile thresholds

A common and pragmatic design for low-cost condition monitoring is to train only on
healthy-machine data, score each window with a one-class model or a simple statistic, and
place the alarm threshold at a high quantile of the training score distribution. The
attractiveness of the design is that no fault data are needed; the cost is that the
reported false-alarm rate is the *only* performance number an operator can act on. This
paper takes that reported number as its object of study.

### 4.2 The evaluation of anomaly detection is already known to be problematic

Several lines of work have established that anomaly-detection evaluation is unreliable in
general, and our contribution is not that observation.

Wu and Keogh [1] showed that the majority of exemplars in widely used time-series
anomaly-detection benchmarks suffer from identifiable flaws, that many published
comparisons may therefore be unreliable, and that much of the apparent progress may be
illusory. Kim et al. [2] showed that the widely used *point-adjustment* protocol can
inflate results to the point where even a random score can appear state-of-the-art.
Sehili and Zhang [3] reached a similar conclusion for multivariate settings, arguing that
evaluation methodology rather than algorithmic novelty often drives reported differences.
Subsequent work has proposed better-targeted evaluation instruments: proximity-aware
scoring [9], a problem-oriented taxonomy of metrics [10], robust evaluation frameworks
for unsupervised detection [11], and unified benchmarking pipelines [8].

### 4.3 Variance, model selection, and the instability of rankings

A second line of work quantifies how much of a reported result is an artefact of choices
unrelated to the method. Bouthillier et al. [4] demonstrated that random-seed variance
alone can change benchmark conclusions. In chemoinformatics, Baumann and Baumann [12]
documented the pitfalls of using cross-validation both to select and to assess models,
and argued for repeated, nested procedures to control the resulting variance. For
time-series anomaly detection specifically, MSAD [6] and mTSBench [7] evaluated model
selection directly and found that current selection strategies remain far from optimal —
mTSBench reports that no single detector dominates across datasets, motivating selection
in the first place. Most recently, the rank-instability study of [5] varied dataset
selection, metrics, hyperparameters and random seeds across 690 datasets and found that
algorithm rankings in anomaly detection are highly unstable.

That literature is general-purpose. It operates on datasets and benchmark suites. It does
not address the setting in which the number that matters is a false-alarm rate measured
on a handful of physical healthy recordings.

### 4.4 Sample size and evaluation protocol in fault diagnosis

Within bearing and machine fault diagnosis, two threads are directly relevant.

The first is sample-size determination. Power-analysis-based procedures have been
proposed to determine the minimum number of vibration samples needed for a classifier to
be trained with statistical stability [13], and applied, for example, to automotive
hydraulic brake diagnosis [14]. Both target **supervised classification** with accuracy as
the endpoint. Our setting is different in kind: training uses healthy data only, and the
endpoint is a false-alarm rate estimated from a quantile-based threshold.

The second is evaluation protocol. Vieira et al. [15] systematically demonstrated that
segment-wise and condition-wise splitting inflate reported performance, proposed
bearing-wise splitting so that one physical bearing appears in either training or test,
reframed the task as multi-label classification with prevalence-independent metrics, and
identified the number of training bearings as a key factor for generalisation. Knap et al.
[16] proposed a leakage-safe, recording-level cross-domain benchmark over CWRU and
Paderborn, and reported that deep models are sensitive to initialisation and require
repeated seeds. These works occupy the "leakage-safe splitting" and "recording-level
evaluation" space, and we do not claim them.

### 4.5 What this paper adds

The prior work above establishes four things: anomaly-detection benchmarks can be flawed
[1, 2, 3]; evaluation instruments can be improved [8, 9, 10, 11]; reported results carry
variance from seeds and selection procedures [4, 12], including unstable rankings [5, 6, 7];
and leakage-safe, unit-aware splitting is both necessary and achievable [15, 16].

What is missing is a quantified account, for the healthy-data-only setting, of **how much
a reported false-alarm rate can be trusted and what it would take to improve it**. This
paper contributes:

1. a measurement of the *noise floor* of the reported false-alarm rate at realistic
   sample sizes, with the test set held fixed so that test-set sampling contributes no
   variance;
2. a decomposition of that floor into split composition and detector random seed, showing
   the two are comparable in magnitude while hyperparameter choice contributes little;
3. a two-arm experiment separating **resampling the same recordings** from **adding
   distinct recordings**, showing that the former does not reduce the uncertainty while
   the latter does;
4. a demonstration that the required number of recordings is operating-condition
   dependent even within a single rig; and
5. a five-point reporting checklist derived from the above.

We explicitly do not claim that evaluation unreliability is a new discovery, nor that our
findings generalise beyond the two rigs studied.

## 5. Discussion

*(to be completed: mechanism, i.e. why threshold-quantile estimation error exceeds the
spacing of test scores near the threshold; relation to the 1/√n law in both directions;
and the five-point checklist below.)*

### Reporting checklist (draft)

1. **Report the training-window count behind the threshold**, not the dataset size.
2. **Report resampling variability from at least two sources** — split composition and
   random seed — rather than a single point estimate.
3. **Report the tie rate** at the minimum validation criterion when the validation
   resolution is coarser than the false-alarm level of interest.
4. **Distinguish new recordings from repeated sampling**; do not use the latter to claim
   sufficient data.
5. **State the number of independent units** (bearings, recordings), not the number of
   windows.

## 6. Limitations

*(to be completed; must mirror `CLAIM_EVIDENCE_MAP.md` §4 item by item:)*

1. very few independent units (IMS: 12 healthy recordings; Paderborn: 6 physical
   bearings, 120 recordings per condition);
2. all evidence derives from public datasets; no self-collected data;
3. three representative detectors only, with the threshold fixed at the 0.99 quantile;
4. limited test-set resolution (24 recordings → 4.17 pp; 14 → 7.14 pp), causing
   quantisation floors;
5. the two rigs differ in sampling rate and record length, so cross-rig comparison is
   limited to efficiency and trend;
6. the "new recordings" arm draws distinct recordings from the same dataset rather than
   prospectively collected data.

## 7. Conclusion

*(to be completed)*