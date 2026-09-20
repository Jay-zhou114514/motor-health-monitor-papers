# Reviewer B report (single independent reviewer)

## Provenance and limitation note

- **Single reviewer, as instructed.** No three-reviewer blind triplication was attempted, so this report does not claim mutual blindness.
- **Task delivery failure.** The task text for this subagent did not reach its context. The assignment was reconstructed from the parent session log, which specified the packet and the emphasis used here.
- **Partial non-independence, stated rather than hidden.** During the same run this agent also carried out the parent A1 number audit, and its corrections are already in the manuscript being reviewed. While doing that work it also read `docs/plans/COMPLETENESS_AUDIT_v2.md`, which registers the findings of the earlier review rounds. Concerns below that overlap earlier rounds are therefore echoes rather than independent discoveries, and I mark them as such. This is a review artifact for internal quality control, not a blind peer review.

## Review setup

- **Input scope** `conference-track/PAPER_v1.0_submission-draft.md` (as revised, working copy with commit `3fa18a7` applied), `conference-track/CLAIM_EVIDENCE_MAP.md`, and the archived products under `motor-health-monitor/experiments/` and `motor-health-monitor/outputs/`.
- **Assessment boundary** bounded to what the archive can support. I recomputed every printed number in Sections 3.1 to 3.6 and in Section 5.1 from the archived CSV files. I did not re-derive the underlying vibration feature pipeline, did not re-run any experiment, did not audit the literature corpus, and took the dataset metadata of Section 2 as given. Figure 1 was checked only through the numbers in its caption.
- **Shared manuscript claim summary** in healthy-data-only bearing anomaly detection, the reported false-alarm rate is claimed to be moved substantially by three analyst choices (whether whole physical units are held apart, how many independent units enter training, and where healthy data end), with the practical reliability of the number described as set less by the detector than by those three choices, and with a five-point reporting checklist as the practical output.
- **Visible evidence base** 11 experiment folders with preregistrations, amendments, run logs, summary CSVs, per-fold CSVs and reproducibility records, four of which record hash-for-hash re-runs. I independently recomputed the published values from those files.
- **Missing materials affecting confidence** no archive pointer exists for the count of analysis-error classes, no archived product underlies the Paderborn per-bearing RMS range quoted in Section 5.1, no archived window count underlies the phrase about twenty windows in Section 5.2, and none of the three dataset-level numbers in Section 2 was re-derived.

## Reviewer 1

- **Overall assessment** the three quantified effects are real and, unusually for this literature, each number I checked reproduces from the archive. In this round every printed value in Sections 3.1 to 3.6 and Section 5.1 recomputed exactly, including the six holdout fold means, the between-fold SD and SE, the eleven per-cell ratios, the five-rule SD ranges for both run-to-failure datasets, the reproduction counts, the selection-stability shares and the variance decomposition. Six inconsistencies that were present at the start of this run have since been corrected in the working copy. What remains is not arithmetic. It is framing and scope. The manuscript still asserts, in the abstract and in the conclusion, a comparison between analyst choices and detector choice that the study never measures on a common estimand, and one such comparison is contradicted by material in the same archive. Two further concerns are interpretive, and both concern the reading of Section 3.1 rather than its computation.

- **Who would be interested in the results, and why** practitioners and methodologists who deploy healthy-only monitoring and report a false-alarm rate, and reviewers of PHM and condition-monitoring papers, because the paper quantifies how far that single number moves under three reporting decisions and supplies a checklist. Readers of the general anomaly-detection literature would find the same message in Wu and Keogh, in the 2026 rank-instability study, and in mTSBench, so the audience here is domain rather than general.

- **Major strengths**
  1. Every headline number I recomputed from the archive reproduces, including values that would be easy to overstate, such as the 44.8 pp between-fold SD that exceeds the 40.63 percent mean it is attached to.
  2. The preregistered criteria that failed are disclosed next to the results they affect, in Section 3.1 for the failed scope criterion and in Section 3.2 for the failed unit criterion, and the saturation of the resampling arm is reported as a failure mode rather than as support.
  3. The unit effect is measured at a fixed record budget inside a single operating condition, which separates the number of independent units from operating-condition diversity. The archive supports this. `EXP-V2-05-summary.csv` shows the sweep continuing to k equal to 4 in only three of six cells, and the paper's own boundary note now says so.
  4. The negative result in Section 3.4 is reported as underpowered and undetermined rather than refuted, and the power figure supporting that reading is archived in `docs/plans/power_analysis.csv` at 0.087.
  5. Scope statements are attached to most numbers, and the two confounded claims, the XJTU-SY boundary sweep and the cross-condition unit comparison, are marked as confounded rather than smoothed over.

- **Major Concerns** RB-M1, RB-M2, RB-M3.

- **Minor Comments** RB-m1 to RB-m10.

- **Technical failings that need to be addressed before the case is established** RB-M1 and RB-M2. Both are confidence and framing failures rather than data failures, so the empirical core survives them. No concern in this report is blocking in the sense defined by the review protocol, because the three quantified effects can each be established without the disputed sentences.

- **Assessment against Nature-style criteria** originality is low and the manuscript says so, positioning itself as quantification and a reporting protocol rather than as discovery. Scientific importance is moderate and is highest for the condition-monitoring community rather than for a general readership. Interdisciplinary reach is limited, since the contribution is a domain instantiation of a general observation. Technical soundness is good on the computational side and weaker on the framing side, in the two places noted above. Readability for nonspecialists is good, and the checklist is the most transferable part of the paper.

- **Recommendation posture** major revision. The measurements are sound and the checklist is worth publishing. Two framing defects should be repaired first, the unsupported detector comparison in the abstract and conclusion, and the lower-bound argument in Section 3.1 that is currently written as if it bounded the ratio from above. I would expect the paper to be acceptable after those changes, with the minor items as a single editing pass.

### RB-M1

- **Concern ID** RB-M1
- **Severity** Major
- **Blocking** No
- **Axis** internal validity and claim strength
- **Claim pointer** Abstract, the sentence reporting that three analyst choices each move the reported false-alarm rate by amounts comparable to, or larger than, changing the detector. Also Section 7, first paragraph, which states that the practical reliability of the rate is set less by the detector than by the three choices the analyst makes.
- **Evidence pointer** the three faces are all computed with the same detector. The preregistrations `experiments/EXP-V2-03-preregistration.md`, `experiments/EXP-V2-04-preregistration.md` and `experiments/EXP-V2-05-preregistration.md` each fix Isolation Forest with 200 trees, max_samples 0.5 and the 0.99 training-score quantile. The only detector spread in the archive is `experiments/EXP-V1-08-summary.csv`, on a different dataset and a different protocol, where the mean false-alarm rate on IMS 4th_test runs from 0.0238 for 3-sigma RMS to 0.50 for a one-class SVM, and `experiments/EXP-V1-09-summary.csv` shows the tuned Isolation Forest meeting a 5 percent cut in three of three batches.
- **Concern** the comparison is stated twice and measured nowhere. No experiment varies the detector and an analyst choice on one estimand. The archive does contain a detector comparison, and on that measurement the detector effect is larger than the definition effect reported in Section 3.3 by more than an order of magnitude when hyperparameters are left untuned, while it becomes small when they are tuned. The manuscript's own Section 3.6 shows that tuning status is itself an analyst decision, which makes the unqualified ranking in Section 7 difficult to defend.
- **Why it matters** the sentence tells a reader how to spend effort. A reader who takes it at face value would spend it on reporting discipline rather than on detector choice, and the archive does not support that ordering. The overlap with an earlier round's concern is acknowledged in the provenance note.
- **Resolution test** either remove the comparability clause and the Section 7 ranking sentence, or add a detector sweep at the same estimand as one of the three faces, in which case the IMS material in `EXP-V1-08` and `EXP-V1-09` already exists and only needs to be reported with its tuning status.

### RB-M2

- **Concern ID** RB-M2
- **Severity** Major
- **Blocking** No
- **Axis** statistical validity of a derived quantity
- **Claim pointer** Section 3.1, the sentence stating that the defensible increase is therefore about 3.5-fold, not an order of magnitude. The same phrase is repeated in Section 5.1 and in Section 7.
- **Evidence pointer** `experiments/EXP-V2-03-summary.csv`, within-bearing arm at n_train equal to 96, where the mean and SD are both 0.0 over 100 replicates, and the holdout arm at the same nominal size, where the six fold means are 0.00, 0.40, 1.55, 69.40, 75.35 and 97.10 percent. The one-sided bound quoted in the paper follows from 24 test recordings with 0 alarms, giving 1 minus 0.05 to the power 1 over 24, which is 11.73 percent.
- **Concern** the ratio is formed from a fold mean in the numerator and an upper confidence bound in the denominator. That construction gives a lower confidence bound on the increase, about 3.5-fold, and it cannot bound the increase from above. With zero alarms in 24 recordings the within-bearing rate is consistent with values well below the bound, so ratios considerably larger than 10 are also consistent with these data. The clause about not being an order of magnitude is therefore unsupported by the calculation that precedes it.
- **Why it matters** the paper's whole treatment of this comparison is a study in careful bounding, and this one sentence converts a lower bound into an upper bound. In a paper whose selling point is disciplined quantification, that inversion is the kind of error a referee will notice and cite.
- **Resolution test** restate the claim as a lower bound, for instance that the increase is at least about 3.5-fold, and delete the clause about orders of magnitude. If a bounded ratio is wanted, the within-bearing arm needs a design that resolves the rate at a fixed number of alarms, since 24 test recordings at 0 alarms cannot bound it above.

### RB-M3

- **Concern ID** RB-M3
- **Severity** Major
- **Blocking** No
- **Axis** interpretation of a reported central value
- **Claim pointer** Section 3.1, table row for the bearing-level holdout, reporting a mean of 40.63 percent, and the abstract, which contrasts 0.00 percent against 40.63 percent. Also Figure 1 panel (a).
- **Evidence pointer** `experiments/EXP-V2-03-summary.csv`, holdout arm at n_train equal to 96, where the six fold means are 0.00, 0.40, 1.55, 69.40, 75.35 and 97.10 percent.
- **Concern** the six folds fall into two groups, three at or below 1.55 percent and three above 69 percent, and no fold lies near the reported mean. The mean of 40.63 percent is therefore not a rate that any held-out bearing experiences, and the between-fold SD of 44.8 pp makes that plain, but the manuscript reports the mean as the headline value and reports the spread as a separate detail. The median is 35.5 percent, which is also not a value any fold takes.
- **Why it matters** the reader's natural question is what happens to the number when a whole bearing is held out, and the honest answer here is that it depends on which bearing, with the outcome falling into a low group or a high group. Reporting a single central value invites the reader to treat 40.63 percent as typical when it is between the two regimes.
- **Resolution test** report the fold-level distribution as the primary result, name the two groups, and present 40.63 percent explicitly as the mean of a bimodal set, or replace it with the fold values and the range. The same treatment should be reflected in the abstract and in Figure 1 panel (a).

### RB-m1

- **Concern ID** RB-m1
- **Severity** Minor
- **Axis** internal consistency
- **Affected element** Section 3.2, table column header SD decreases with number of bearings, for all three detector rows.
- **Evidence pointer** the same section's boundary note, which defines the criterion as the rank correlation between k and the SD, and `experiments/EXP-V2-05-summary.csv`, where XJTU-SY 40Hz10kN runs 39.61, 36.12, 20.02 and 20.69 pp and is therefore not strictly monotone.
- **Issue** under the header as written, Isolation Forest is 5 of 6 rather than 6 of 6. The value 6 of 6 holds only under the rank criterion.
- **Required correction** rename the column so the criterion is in the header, for example negative rank correlation between k and SD, or add a footnote to the column.

### RB-m2

- **Concern ID** RB-m2
- **Severity** Minor
- **Axis** traceability
- **Affected element** Section 3.2, the three-detector table.
- **Evidence pointer** `experiments/EXP-V2-05-summary.csv` for the Isolation Forest row and `experiments/EXP-V2-06-summary.csv` for the 3-sigma RMS and Mahalanobis rows.
- **Issue** the three rows are presented as one comparison but come from two experiments. The design is the same, with seven folds and n equal to 350 in the PRONOSTIA cells I checked, so the presentation is defensible, but a reader cannot recover the provenance from the paper.
- **Required correction** add a note naming the experiment behind each row, or state that the Isolation Forest row is the main arm and the other two are the multi-detector replication.

### RB-m3

- **Concern ID** RB-m3
- **Severity** Minor
- **Axis** scope statement
- **Affected element** Section 3.4, the claim of 0 of 26 independent folds and the breakdown into 0 of 24 for IMS and 0 of 2 for MFPT.
- **Evidence pointer** `experiments/EXP-V1-07-folds.csv`, filtered to scheme empirical and feature group RMS plus centroid, where the totals are 24 IMS folds and 3 MFPT folds with exactly one inflation ratio above 1, that one being 1.5756 for the MFPT fold holding out baseline_3.
- **Issue** the counts reproduce exactly, but the paper does not say which scheme and which feature group define the 26 folds. Under other schemes the archive holds a different number of folds, so the scope is needed for the count to be checkable.
- **Required correction** state the scheme and feature group next to the count.

### RB-m4

- **Concern ID** RB-m4
- **Severity** Minor
- **Axis** reproducibility disclosure
- **Affected element** Section 3.6, the resampling claim of 18.0 pp against 0.00 pp, which comes from EXP-V2-01.
- **Evidence pointer** `experiments/EXP-V2-01-summary.csv`, S1_resample at n_train equal to 96 with sd_fp 0.18037, and S2_new_records at n_train equal to 96 with sd_fp 0.0. Section 3.5 names the verification depth for EXP-V2-04 to V2-06 and for EXP-V1-10, and for V1-05 to V1-09, but not for V2-01.
- **Issue** the paper's own discipline is to state verification depth per experiment, and the experiment carrying a key Section 3.6 claim is not covered by that statement.
- **Required correction** extend the Section 3.5 sentence to name the verification depth for EXP-V1-11, EXP-V2-01 and EXP-V2-02.

### RB-m5

- **Concern ID** RB-m5
- **Severity** Minor
- **Axis** traceability
- **Affected element** Section 5.2, the phrase about four features and about twenty windows.
- **Evidence pointer** `experiments/EXP-V2-05-preregistration.md` fixes the detector and the quantile but does not state a window count per record, and `experiments/EXP-V2-05-summary.csv` records n_train equal to 20 recordings. I could not verify that 20 recordings corresponds to about 20 windows.
- **Issue** the claim may well be correct, but it is unverifiable from the material in the archive, and Section 3.6 of the same manuscript asks authors to report training windows rather than dataset size.
- **Required correction** give the window construction and the resulting window count, or restate the sentence in recordings.

### RB-m6

- **Concern ID** RB-m6
- **Severity** Minor
- **Axis** traceability
- **Affected element** Section 5.1, the statement that per-bearing mean RMS ranges from 0.17 to 0.40 on the Paderborn healthy set.
- **Evidence pointer** the range appears in `docs/AUDIT_2026-09-18_self_check.md`, which cites K001 at 0.403 and K004 at 0.171. No summary CSV in the archive carries per-bearing Paderborn RMS.
- **Issue** the number is consistent with the audit note, but the audit note is not an archived result product, so a reviewer cannot recompute it.
- **Required correction** point to a CSV or script that produces the per-bearing RMS values.

### RB-m7

- **Concern ID** RB-m7
- **Severity** Minor
- **Axis** claim strength
- **Affected element** Abstract, the contrast between 0.00 percent and 40.63 percent.
- **Evidence pointer** Section 3.1, which states that the within-bearing figure is a single deterministic evaluation with 4.17 percentage point resolution.
- **Issue** the abstract states the pair without the qualifier that the lower value is one deterministic evaluation rather than a distribution.
- **Required correction** add a short qualifier to the abstract sentence, and keep the fuller treatment in Section 3.1.

### RB-m8

- **Concern ID** RB-m8
- **Severity** Minor
- **Axis** verifiability
- **Affected element** Section 3.5, the statement that fourteen classes of analysis error were found and corrected, split eleven and three.
- **Evidence pointer** none in the archive. The figure appears in the manuscript and in the audit document, and I found no register whose entries add to fourteen by those categories.
- **Issue** a count of this kind invites the reader to trust a bookkeeping total that cannot be checked.
- **Required correction** cite the register that lists the classes, or drop the number and keep the qualitative statement.

### RB-m9

- **Concern ID** RB-m9
- **Severity** Minor
- **Axis** claim strength in a figure caption
- **Affected element** Figure 1 caption, panel (b), which states that four bearings reduce the spread.
- **Evidence pointer** `experiments/EXP-V2-05-summary.csv` and `experiments/EXP-V2-06-summary.csv`, where the sweep reaches k equal to 4 in only three of the six cells, and stops at 3 for XJTU-SY 35Hz12kN and 37.5Hz11kN, and at 2 for PRONOSTIA C3.
- **Issue** the caption generalizes a value that half the cells never reach.
- **Required correction** replace four bearings with the number of bearings available in the cell, and state the range.

### RB-m10

- **Concern ID** RB-m10
- **Severity** Minor
- **Axis** internal consistency
- **Affected element** Section 3.6, the checklist item asking authors to report training windows, against the same section's own numbers, which are quoted as 20 and 96 recordings.
- **Evidence pointer** Section 3.6 paragraphs on the noise floor and on resampling, and `experiments/EXP-V2-01-summary.csv`, whose n_train column counts recordings.
- **Issue** the paper's recommendations outrun its own reporting for the two central Section 3.6 claims.
- **Required correction** give the window counts behind those two numbers, or add a sentence noting that in these datasets the record count and the window count coincide, with the reason.

## Risk and unsupported claims

- The count of fourteen analysis-error classes is not supported by any archived register.
- The per-bearing Paderborn RMS range of 0.17 to 0.40 has no archived data product.
- The phrase about twenty windows in Section 5.2 is unverifiable against the archive.
- The comparability clause in the abstract and the ranking sentence in Section 7 are not supported by any measurement on a common estimand, and the detector spread recorded in `EXP-V1-08-summary.csv` runs the other way on a different dataset.
- The claim that the scope increase is not an order of magnitude is not implied by the lower confidence bound that precedes it.
- The comparison of the 40.63 percent mean against a bimodal fold distribution is stated without the qualification the distribution requires.
- Section 2 dataset metadata, including sampling rates, record lengths and unit counts, was taken as given and is not independently verified here.
- Literature positioning was not audited in this review.