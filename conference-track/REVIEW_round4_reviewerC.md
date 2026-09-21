# Reviewer C report (round 4, serial independent reviewer)

## Provenance and limitation note

- **This report is internal quality control, not blind peer review.** It was produced by a single
  reviewer commissioned by the project itself, on the project's own manuscript, with full access to
  the project's internal records. No measure of blinding was attempted and none should be inferred.
- **Task-text delivery failed again, and the on-disk packet is what saved the review.** The task text
  for this subagent did not reach its context: the incoming message was `Message Type: NEW_TASK /
  Task name: /root/reviewer_c2/reviewer_c_round4_v2 / Payload:` with an **empty payload**. The
  assignment was therefore reconstructed from the packet file
  `conference-track/REVIEW_round4_TASK_C.md`, which states, as the assignment actually worked to:
  *"本轮 = 报告完整性（reporting completeness）+ 读者可复现性（reader reproducibility）… 要回答的问题：
  一个完全不在本项目里的读者，拿着这份稿件以及它指向的归档产物，能不能独立判断每个数字/每个结论是怎么来的、
  适用边界在哪里、有没有必须报告却被省略的信息？"* The mitigation required by
  aftercare anti-pattern 15 (write the packet to disk) worked; the message channel did not. This is a
  recurrence of anti-pattern 15 in a new form and is reported as such in the project record, not as a
  defect of the manuscript.
- **Partial non-independence, declared.** While performing this review I read, besides the manuscript:
  `REVIEW_round3_reviewerB.md` (all of it), `docs/EXPERIMENT_AFTERCARE.md`,
  `docs/REPRODUCIBILITY_PROTOCOL.md`, `docs/plans/COMPLETENESS_AUDIT_v2.md`,
  `docs/plans/PRE_WRITING_COMPLETENESS_AUDIT.md`, `conference-track/NUMBER_TRACEABILITY_AUDIT.md`,
  `conference-track/CLAIM_EVIDENCE_MAP.md`, `conference-track/FIG1_NOTES.md`, the EXP-V2-04/05/06
  preregistrations and the frozen experiment scripts. Concerns that overlap earlier rounds are echoes
  rather than independent discoveries and are marked as such; the concerns I believe are new to this
  round are RC-M1, RC-M3, RC-M4, RC-m3, RC-m7 and RC-m8 (RC-m5 and RC-m10 echo a round-2 minor about missing window reporting, and RC-m7 is adjacent to round-2 R1-M6).
- **Round-4 purpose served.** The question set by this round is whether a reader outside the project
  could reconstruct each number, its boundary, and the information omitted. My verdict is: the
  arithmetic core is in better shape than at any earlier round - every headline number I recomputed
  from the archive reproduces - while the *reader-facing* layer (what the numbers mean, how they were
  produced, and what the project's own records say about verification) is where the remaining defects
  sit. No defect found in this round touches the data or the fitting code.

## Review setup

- **Input scope.** `conference-track/PAPER_v1.0_submission-draft.md` (446 lines, the file as it stands
  at review time), `CLAIM_EVIDENCE_MAP.md`, `REFERENCES.md`, `CITATION_AUDIT.md`,
  `NUMBER_TRACEABILITY_AUDIT.md`, `PAPER_OUTLINE.md`, `FIG1_NOTES.md`, `figures/` and the three
  earlier review reports in the same directory; on the Master side `docs/FROZEN_PROTOCOL.md`,
  `docs/REPRODUCIBILITY_PROTOCOL.md`, `docs/EXPERIMENT_AFTERCARE.md`,
  `docs/plans/COMPLETENESS_AUDIT_v2.md`, `docs/plans/PRE_WRITING_COMPLETENESS_AUDIT.md`, all 17
  `experiments/` records with their CSV products and hash files, `outputs/`, and the frozen scripts in
  `src/`.
- **Assessment boundary - what I verified.** I recomputed, from the archived CSVs, every number in
  Section 3.1; the per-cell SD series, ratios and criterion counts behind Section 3.2; the five-rule
  SD values behind Section 3.3; the fold counts and the single inflation ratio behind Section 3.4; and
  every number in Section 3.6 and Section 5.1. I recomputed Section 3.2 and Section 3.3 under **two**
  definitions of SD (below). I recomputed the Section 5.1 per-bearing RMS values directly from the raw
  `.mat` records with my own RMS formula (120 records), and I recomputed the tie/zero-minimum shares
  for Section 3.6 from the replicate-level file. I checked the existence, content and coverage of
  every archived hash file and preregistration artifact, the anti-pattern register's actual length,
  the row-level training sizes in the two unit experiments, and which IMS recordings the frozen loader
  actually reads.
- **Assessment boundary - what I took as given.** The vibration-feature pipeline's internal formulas
  (I re-used the raw records but not a re-derivation of each feature); Section 2's dataset metadata
  other than the IMS recording counts; the literature corpus and the citation metadata (no literature
  audit, per the task packet); the dataset licences; and the correctness of the earlier rounds'
  reports. **I did not re-run any experiment**, so nothing in this report is L3 evidence of my own.
- **Shared manuscript claim summary.** In healthy-data-only bearing anomaly detection the reported
  false-alarm rate is claimed to be moved substantially by three analyst choices - whether whole
  physical units are held apart, how many independent units enter training, and where healthy data end
  - with each choice measured on its own estimand and no ordering claim between them or against
  detector choice, and with a five-point reporting checklist as the practical output.
- **Visible evidence base.** 17 numbered experiments with preregistrations (from EXP-V1-06 onward),
  run logs, summary CSVs, per-fold and replicate-level CSVs, four archived hash files, three figure QA
  reports, two number audits, and the three earlier review reports. The headline numbers of Sections
  3.1-3.6, 5.1 and both abstract/conclusion sentences all reproduce from this base.
- **Missing materials affecting confidence.** No archived verification record of any kind exists for
  EXP-V1-11, EXP-V2-01, EXP-V2-02 or EXP-V2-03 (no L1 output, no L2 output, no `*-hashes.txt`); no
  generating script or run log exists for `EXP-V2-03-per-bearing-rms.csv`; no figure source-data table
  exists for Figure 1; `conference-track/SUBMISSION_CHECKLIST.md` is unchecked and still states that the
  project has not reached the submission threshold, and `STATUS.md` stops at 2026-09-18, so the
  reader-facing repository state does not yet match the manuscript's state.

## Major concerns

### RC-M1

- **Concern ID** RC-M1
- **Severity** Major
- **Blocking** No
- **Axis** reporting completeness and reproducibility of a derived quantity (definition of the dispersion measure)
- **Claim pointer** Section 3.2, table header (line 116) `Negative rank correlation between k and SD` and `SD(k_max) < SD(k=1)`; Section 3.2 line 113 `Holding the sample size fixed at 20 recordings`; Section 3.3, table header (line 148) `SD(k_max) across five rules`; abstract lines 26-28 (`increasing the number of distinct training bearings reduced the spread ... (6 of 6 conditions each)`); Section 5.2; Figure 1 caption panel (b); Section 7 lines 401-403.
- **Evidence pointer** The manuscript labels the SD in Section 3.1 (`between-fold SD 44.8 pp`, line 88) but never labels the SD in Sections 3.2 and 3.3, where it is a **different quantity**. The frozen implementations compute a **pooled SD over replicate rows** (`src/exp_v2_05_within_condition.py:114-116`, `src/exp_v2_06_multi_detector.py:118-119`, `src/exp_v2_04_xjtu_pronostia.py:124-129`, all `agg(sd_fp=("test_fp","std"))` over fold x replicate rows), not an SD of fold means. I recomputed both definitions from `experiments/EXP-V2-05-raw.csv`, `EXP-V2-06-raw.csv` and `EXP-V2-04-sensitivity_raw.csv`:
  - Isolation Forest (6 cells): pooled 6/6 negative correlation and 6/6 SD(k_max) < SD(k=1), as printed; **between-fold 2/6 and 2/6**.
  - 3-sigma RMS (6 cells): pooled 6/6 and 6/6, as printed; **between-fold 4/6 and 4/6**.
  - Mahalanobis (6 cells): pooled 2/6 and 2/6, as printed; **between-fold 0/6 and 0/6**.
  - Boundary sweep, PRONOSTIA, SD(k_max) per rule: pooled `7.56, 7.80, 9.60, 9.96, 9.59` -> range **2.40 pp** (as printed); between-fold `4.66, 4.85, 5.90, 5.66, 6.38` -> range **1.72 pp**.
  - Boundary sweep, XJTU-SY: pooled `14.51, 15.69, 15.95, 16.31, 19.70` -> range 5.19 pp; between-fold `12.73, 13.30, 15.50, 11.05, 19.16` -> range 8.11 pp.
  That the printed values are the pooled ones is also visible inside the paper: the disclosed non-monotone cell `XJTU-SY 40Hz10kN rises from 20.02 pp at k=3 to 20.69 pp at k=4` (line 133) is exactly the pooled series (`39.61, 36.12, 20.02, 20.69`); the between-fold series for that cell is `14.16, 17.29, 10.38, 18.89`.
- **Concern** Every dispersion number in the second and third faces of the paper is a pooled replicate SD, while the only SD the manuscript defines is a between-fold SD. The two definitions do not merely differ in magnitude: they change the reported counts (6/6 vs 2/6 for Isolation Forest; 2/6 vs 0/6 for Mahalanobis) and they change whether the preregistered X1 criterion passes on PRONOSTIA (`EXP-V2-04-preregistration.md` Section 7 defines X1 as an SD range greater than 2 pp; pooled 2.40 pp passes, between-fold 1.72 pp would not). A reader who carries the Section 3.1 convention into Sections 3.2-3.3 - the natural reading - cannot reproduce the printed counts.
- **Why it matters** The unit effect and the boundary effect are two of the paper's three claims, and both are quantified with a dispersion measure whose definition is unstated and whose alternative gives different headline numbers, including a different pass/fail against the project's own preregistered threshold. Reporting discipline is the paper's selling point; an undefined dispersion measure in the central tables is the one gap a methods referee will look for first.
- **Resolution test** Name the measure once in Section 2 or at first use (for example, "SD denotes the standard deviation of the reported rate over all fold x replicate evaluations, pooled; where a between-fold quantity is meant it is stated"), then either re-state the counts and ranges under both definitions or add a one-sentence sensitivity note giving the between-fold counts (6/6 -> 2/6, 6/6 -> 4/6, 2/6 -> 0/6; 2.40 -> 1.72 pp on PRONOSTIA). Because the abstract, Section 3.2, Section 5.2, the Figure 1 caption and Section 7 all carry the affected counts, the fix must be applied at every occurrence, not only in Section 3.2.

### RC-M2

- **Concern ID** RC-M2
- **Severity** Major
- **Blocking** No
- **Axis** accuracy of the reproducibility claim (report completeness)
- **Claim pointer** Section 3.5, lines 174-177: `EXP-V1-11, EXP-V2-01 and EXP-V2-02 carry invariant and recomputation checks together with an archived hash baseline, but have not been re-run for comparison. The experiment carrying Section 3.1 (EXP-V2-03) is in the same category`; and Section 6, limitation 6-7 (`older experiments have invariant and recomputation checks plus a stored hash baseline only`).
- **Evidence pointer** The project's own verification records say the opposite.
  - `src/verify_paper_experiments.py` (header: `对象：EXP-V1-05/06/07/08/09/10`) checks exactly six experiments and writes exactly one baseline file, `experiments/EXP-V1-05_to_V1-10-hashes.txt` (17 entries, EXP-V1-05 to EXP-V1-10). No hash file covering EXP-V1-11, EXP-V2-01, EXP-V2-02 or EXP-V2-03 exists anywhere: the complete set of archived hash files is `EXP-V1-05_to_V1-10-hashes.txt`, `EXP-v2_04-hashes.txt`, `EXP-v2_04-hashes-BEFORE-rerun.txt`, `EXP-v2_05-hashes-BEFORE-rerun.txt`, `EXP-V2-04_05_06-hashes-FINAL.txt` (plus copies under `outputs/`).
  - `docs/plans/PRE_WRITING_COMPLETENESS_AUDIT.md:21` lists `EXP-V1-01 ~ V1-11、V2-01、V2-02、V2-03（共 14 个）` against three-layer verification as `未做（均早于规范）`; line 86 puts `EXP-V2-01~03` at `未做三层验证；结论按 Level B 使用并如实披露`; line 123 repeats `V1-00~04、V2-01~03 未做三层验证（已声明 pre-protocol）`; the core-experiment matrix at lines 98-104 covers only EXP-V1-10, EXP-V2-04, EXP-V2-05, EXP-V2-06 and `EXP-V1-05~09 | L1 | L2 | 哈希基线`.
  - `docs/plans/COMPLETENESS_AUDIT_v2.md:11` (D1) and `docs/plans/NEXT_SESSION_BRIEF.md:58` state the same status for the pre-protocol family.
- **Concern** The manuscript upgrades four experiments (EXP-V1-11, EXP-V2-01, EXP-V2-02, EXP-V2-03) from "no three-layer verification, disclosed as pre-protocol" to "invariant and recomputation checks with an archived hash baseline". No such checks or baselines exist in the archive. The upgrade matters most for EXP-V2-01, which carries the Section 3.6 claim *resampling is not a substitute for data* (SD 18.0 pp at n = 96 versus 0.00 pp), and for EXP-V2-03, which carries Section 3.1. The project's accepted gap (eight pre-protocol experiments disclosed as such) is also replaced by a stronger claim rather than disclosed. This is the same failure class as round 1's S-M4 (reproducibility statement not accurate), recurring in a new form.
- **Why it matters** Section 3.5 is the paragraph a reader uses to decide how much of the paper to trust, and Section 6 repeats it. A verification status that the archive contradicts is worse than an acknowledged gap, because it removes the flag that would otherwise tell the reader which results rest on checks and which do not.
- **Resolution test** Either perform and archive L1/L2 for EXP-V1-11, EXP-V2-01, EXP-V2-02 and EXP-V2-03 (the six-experiment script can be extended), or restore the record's wording: state that these experiments were run before the verification protocol existed, carry no L1/L2 and no hash baseline, and are used at Level B with the pre-protocol limitation disclosed. The accepted-gap list in the brief should then appear in the manuscript in that form.

### RC-M3

- **Concern ID** RC-M3
- **Severity** Major
- **Blocking** No
- **Axis** reader reproducibility (execution path)
- **Claim pointer** Section 2 entire (datasets, features, discipline); Sections 3.1-3.6 as instructions a reader would follow; Figure 1.
- **Evidence pointer** The manuscript contains **no** code-availability statement, repository reference, script name, command, environment description, seed policy, dataset download route or licence statement. Searching the draft: `code` 0 hits, `script` 0 hits, `open` 0 hits, `license/licence` 0 hits, `download` 0 hits; `seed` occurs 6 times, all describing variance components, never the seed derivation; the single `repositor` hit is inside the IMS data-set citation. The only pointers into the project are private-repo relative paths (`experiments/EXP-V2-03-per-bearing-rms.csv`, line 293; `docs/EXPERIMENT_AFTERCARE.md`, line 178), which a reader cannot resolve. Dataset sizes are given as **subsets**: `data/raw/ims/1st_test` holds 15 recordings and `src/exp_v1_08_baselines.py:45-49` keeps only the 12 whose names start `2003.10.22` (the three `2003.11.25` recordings are silently dropped), which is exactly the `12 healthy recordings` printed in Section 2 line 57 and used in Section 3.6 (7 fit + 3 validation + 2 test = 12); `PROJECT_STATUS.md:114` records the same 12 + 6 + 6 as a project choice. Window construction is never stated per dataset: the frozen code uses 0.25 s / 0.125 s for IMS (`src/exp_v1_08_baselines.py:66-67`), one window per record for the run-to-failure data (`src/runtofailure_data.py:48-53`), and a single whole-record window for Paderborn (`src/paderborn_data.py:63-65`). The 50 percent overlap, which appears in the project's own limitations list, appears nowhere in the manuscript.
- **Concern** The paper cannot be executed from the paper. A reader can read every number but cannot obtain the data subset, the code, the seeds, the window definitions or the licence terms, and the two inline archive pointers are unresolvable outside the private repository. The Protocol section asserts a discipline (pre-registration, training-only thresholds, hash-for-hash re-runs) that a reader can only take on faith.
- **Why it matters** This round's question is whether an outside reader can independently determine how each number was produced and where it applies. For the *data* layer the answer is currently no, even though the archive would support the answer with a few sentences. For a venue with a reproducibility or data-availability requirement, this is also a desk-reject risk independent of the science.
- **Resolution test** Add a short Data and Code availability paragraph (repository or supplementary location, entry-point script per experiment family, environment and versions), state the seeds and their derivation (`zlib.crc32`-based, per the project's anti-pattern 4, with the exact strings), state the dataset acquisition sources and licences, state the IMS subsetting rule and why the November recordings are excluded, and state the window length, step and overlap for each dataset. All of this exists in the Master repository; the work is transcription, not new measurement.

### RC-M4

- **Concern ID** RC-M4
- **Severity** Major
- **Blocking** No
- **Axis** claim strength / reporting completeness (evidence-level qualifiers)
- **Claim pointer** Section 2 lines 71-72 (`Evidence is graded A-D; exploratory analyses are labelled as such`); abstract lines 20-35; Section 7 lines 393-410.
- **Evidence pointer** The grade vocabulary appears **only** in that one Protocol sentence: searching the draft for `Level`, `graded`, `grade`, `A-D` returns line 71-72 and nothing else. No claim in Sections 3, 5 or 7 carries a grade, and the abstract and conclusion carry none. The project's own mapping (`CLAIM_EVIDENCE_MAP.md`) assigns Level B to C2-C10 and Level A only to the negative result C1, and the project's hard rule is that Level C/D claims must not appear in an abstract or conclusion - a rule a reader cannot check without the grades.
- **Concern** The manuscript claims a grading discipline it never applies. Readers cannot tell which of the three faces is Level A, B or C, and the one sentence in Section 3.3 that does qualify a subset of the boundary claim (`the cross-dataset claim is therefore partially supported`) is the only place where the paper's own confidence vocabulary surfaces.
- **Why it matters** The paper's positioning is that it quantifies what can and cannot be trusted in a single reported number. A reader who is not told which of the paper's own numbers are Level A and which are Level B has to re-derive the confidence structure from the boundary notes, which is exactly the burden the paper sets out to remove.
- **Resolution test** Attach the grade (or a compact qualifier of the same force) to each of the three faces at first statement, to the two cross-dataset statements, and to the abstract and conclusion sentences, or delete the Protocol sentence and rely on explicit per-claim qualifiers. If a grade is attached, the registry in `CLAIM_EVIDENCE_MAP.md` should be cited so the mapping is checkable.

## Minor concerns

### RC-m1

- **Concern ID** RC-m1
- **Severity** Minor
- **Blocking** No
- **Axis** traceability of the third face
- **Claim pointer** Section 3.3, lines 144-146 (`swept five variants (fraction 5/10/20%, floor 10/20/30)`) and the Section 3.3 table.
- **Evidence pointer** Six parameter values are listed for five rules; the five rules actually run are `(0.05, 20, 60), (0.10, 20, 60), (0.20, 20, 60), (0.10, 10, 60), (0.10, 30, 60)` (`src/exp_v2_04_xjtu_pronostia.py:31-32`), and only the raw CSV carries them: `experiments/EXP-V2-04-sensitivity_raw.csv` has a `rule` column, while `experiments/EXP-V2-04-sensitivity_summary.csv` **drops it** (`summarize()` groups by dataset/arm/n_train/k_bearings only, lines 124-130), so its PRONOSTIA row pools all five rules into one row with `n = 2550` and `sd_fp = 0.0896` - a value that appears nowhere in the paper. The five printed SDs are only recomputable from the raw file, grouped by `rule`; I reproduced them exactly that way (`7.56, 7.80, 9.60, 9.96, 9.59` and `14.51, 15.69, 15.95, 16.31, 19.70`). The project's own number audit names the wrong source: `NUMBER_TRACEABILITY_AUDIT.md` row `Section 3.3` cites `EXP-V2-04-sensitivity_summary.csv` (plus the record's prose table) for these five values.
- **Concern** The third face's numbers are traceable, but not along the path the paper and its audit imply, and the archived summary for that experiment both loses the rule key and pools rules - the failure modes the project registered as anti-patterns 2 and 3.
- **Why it matters** A reader who opens the summary file, as the audit invites, finds a different set of numbers and cannot recover the five rules.
- **Resolution test** Name the five rule triples in the paper, cite `EXP-V2-04-sensitivity_raw.csv` with its `rule` column (and the pooled-SD definition), regenerate the sensitivity summary with `rule` retained, and correct the audit's source row.

### RC-m2

- **Concern ID** RC-m2
- **Severity** Minor
- **Blocking** No
- **Axis** verifiability of a stated count
- **Claim pointer** Section 3.5, lines 177-180: `Fourteen classes of analysis error are listed in the project's disclosure register (docs/EXPERIMENT_AFTERCARE.md) ... Eleven lie in summary, verdict and verification logic, and three concern data handling such as seed derivation and file counting`.
- **Evidence pointer** `docs/EXPERIMENT_AFTERCARE.md` lines 46-75 contain **15** numbered entries under the heading `反模式清单（已实际发生过，禁止再犯）`. Of these, 13 concern analysis (items 1, 2, 3, 7, 8, 9, 10, 11, 12, 13 = ten summary/verdict/verification entries, plus items 4, 5, 6 = three data-handling entries matching the paper's own examples of seed derivation and file counting); item 14 is a citation-provenance error and item 15 is a sub-agent workflow error, neither an analysis error. `11 + 3 = 14` matches neither 15 (the register's length) nor 13 (the analysis-related subset).
- **Concern** The round-3 minor asked for the register to be cited or the number dropped; the register is now cited, and it contradicts the number.
- **Why it matters** The sentence is a self-audit claim; a reader who opens the cited file finds a different count, which weakens an otherwise strong passage.
- **Resolution test** Write the count that the register supports (fifteen entries, thirteen of them analysis errors, three of those data-handling), or drop the arithmetic and keep the qualitative statement.

### RC-m3

- **Concern ID** RC-m3
- **Severity** Minor
- **Blocking** No
- **Axis** accuracy of the stated design
- **Claim pointer** Section 3.2, line 113 (`Holding the sample size fixed at 20 recordings`) and lines 129-131 (`the record budget is fixed at 20 (five recordings per bearing)`).
- **Evidence pointer** In all five cells where k reaches 3 the actual training size is **18** recordings, because the budget is split by integer division (`per = max(1, BUDGET // k_use)`, `src/exp_v2_05_within_condition.py:107`; same code in `src/exp_v2_06_multi_detector.py`): `EXP-V2-05-raw.csv` and `EXP-V2-06-raw.csv` show `n_train = 20` at k = 1, 2, 4 and `n_train = 18` at k = 3 (XJTU-SY 35Hz12kN, 37.5Hz11kN, 40Hz10kN and PRONOSTIA C1, C2). "Five recordings per bearing" holds only in the k = 4 cells (per = 5); at k = 3 it is six per bearing, at k = 2 it is ten.
- **Concern** The stated design is not the executed design in five of six cells, and the difference is in the direction that matters for the claim (the k = 3 cells have fewer training records than k = 4, so part of the SD reduction attributed to bearings also comes with a nominal-size change).
- **Why it matters** This is the one place where the unit claim's "fixed budget" construction can be challenged, and the paper states it in a form a reader will find to be inaccurate on recomputation.
- **Resolution test** State the split rule (`20 // k` per bearing, hence 20 recordings at k = 1, 2, 4 and 18 at k = 3) and add the k = 3 cells' actual sizes to the boundary note.

### RC-m4

- **Concern ID** RC-m4
- **Severity** Minor
- **Blocking** No
- **Axis** figure-text-data consistency
- **Claim pointer** Figure 1 caption, panel (d), line 429: `Rendered with matplotlib; collision and typography audits passed (Section 3.5)`.
- **Evidence pointer** Section 3.5 contains no figure material (it is the experiment-verification subsection); the checklist is Section 3.6, and the QA reports are `figures/fig1.validate.txt` (19 pass / 2 warn / 0 fail), `figures/fig1.pdftext.txt` (PASS, minimum 6.5 pt) and `figures/fig1.collision.txt` (0 fail), summarised in `FIG1_NOTES.md` (which itself still maps panel (d) to `Section 3.5`). The figure's numbers are hard-coded text strings in `src/make_fig1_concept.py` (e.g. lines 87, 123-124) and no source-data table for the figure exists in the archive.
- **Concern** The cross-reference points at the wrong section, and the figure has no machine-readable source data; its numbers are traceable only through a plotting script the paper never cites.
- **Why it matters** Figure 1 carries the paper's three headline numbers; journals increasingly require source data for figures, and the caption currently sends the reader to a subsection that cannot answer the question asked.
- **Resolution test** Repoint the caption to the subsection that reports the numbers each panel shows (or to a new figure-QA sentence), cite the generating script, and ship a figure source-data CSV.

### RC-m5

- **Concern ID** RC-m5
- **Severity** Minor
- **Blocking** No
- **Axis** internal consistency of the checklist
- **Claim pointer** Section 3.6, checklist item 1 (`Report the number of training windows behind the threshold, not the dataset size`), against the same section's Paderborn claims (`20`/`96` recordings, line 206-209).
- **Evidence pointer** The two central Section 3.6 claims are stated in recordings; for Paderborn one recording contributes exactly one feature vector (`src/paderborn_data.py:59-65`, single-window mode), whereas for IMS one recording contributes seven windows of 0.25 s (`src/exp_v1_08_baselines.py:63-70`, as used in the 84-window and 14-window counts of Section 3.6 line 188). The manuscript never states either conversion, so recommendation 1 is not met by the section that makes it. Round 3's RB-m10 asked for exactly this note; it is absent.
- **Concern** The paper's recommendations outrun its own reporting, which is the most quotable criticism of a reporting-checklist paper.
- **Why it matters** A reader applying the checklist to this paper finds item 1 unanswered, and cannot convert the paper's own n values into windows.
- **Resolution test** Add one sentence per dataset family (Paderborn: one record = one 4 s feature vector, so 20/96 recordings are 20/96 training vectors; IMS: 0.25 s windows at 0.125 s step, seven per recording; run-to-failure: one record = one vector) and give the window count alongside each n.

### RC-m6

- **Concern ID** RC-m6
- **Severity** Minor
- **Blocking** No
- **Axis** artifact completeness
- **Claim pointer** Section 5.1, line 293: `per-bearing mean RMS ranges from 0.171 to 0.403 on the Paderborn healthy set (experiments/EXP-V2-03-per-bearing-rms.csv)`.
- **Evidence pointer** The cited file exists (`experiments/EXP-V2-03-per-bearing-rms.csv`, 161 bytes, written 2026-09-20 18:15:03, also copied to `outputs/paderborn_per_bearing_rms.csv`) and contains exactly the six values the sentence needs: K001 0.4028, K002 0.2301, K003 0.3622, K004 0.1706, K005 0.1987, K006 0.3812, each over count = 20. I verified them independently by recomputing RMS directly from the raw `.mat` records (first 256 000 samples of `vibration_1` of all 120 `N15_M07_F10_*` records) with my own formula: identical to four decimals. The file has **no generating script and no run log**, so the project's own five-artifact rule (record, script, CSV, log, figure) is not met for the only artifact backing Section 5.1.
- **Concern** The number is correct and reproducible from raw data, but the artifact itself cannot be regenerated from the archive without re-implementing it; its timestamps show it was produced during manuscript revision rather than by an experiment run.
- **Why it matters** Round 3 asked for a CSV or script that produces these values. The answer is now half-given: a values-only CSV. A reader can still reproduce it (as I did) but is not told how.
- **Resolution test** Add the short script that writes the file (record or per-bearing aggregation of the frozen feature table) and reference it from the caption of the sentence, or move the claim into the Section 3.1 results where the same data are already analysed.

### RC-m7

- **Concern ID** RC-m7
- **Severity** Minor
- **Blocking** No
- **Axis** label accuracy
- **Claim pointer** Section 3.2, table header line 116 (`Negative rank correlation between k and SD`) and line 131-132 (`The criterion for "decreases" is the rank correlation between k and the SD`).
- **Evidence pointer** The frozen criterion is a product-moment correlation, not a rank correlation: `src/exp_v2_05_within_condition.py:132` and `src/exp_v2_06_multi_detector.py:141` both call `np.corrcoef(k_bearings, sd_fp)`. For the one cell the paper singles out (XJTU-SY 40Hz10kN, pooled SD `39.61, 36.12, 20.02, 20.69`), Pearson is -0.921 and Spearman -0.800.
- **Concern** Round 3's RB-m1 asked for the criterion to be moved into the column header, and it was - with a name that does not match the implementation. The sign and therefore the count are unaffected in the six cells, but the label is wrong.
- **Why it matters** A reader who recomputes with a rank correlation gets slightly different coefficients and will query the difference; the paper should not force that.
- **Resolution test** Call it a negative correlation, or state that the frozen implementation uses the product-moment correlation (and give the rank version alongside if the distinction is wanted).

### RC-m8

- **Concern ID** RC-m8
- **Severity** Minor
- **Blocking** No
- **Axis** verifiability of a re-run claim
- **Claim pointer** Section 3.5, lines 171-172 (`EXP-V2-04, EXP-V2-05 and EXP-V2-06 were re-run and reproduced byte-for-byte`); Section 2 line 72-73 (four experiments compared hash-for-hash).
- **Evidence pointer** Pre-rerun baselines exist for two of the three: `outputs/exp_v2_04-hashes-BEFORE-rerun.txt`, `outputs/exp_v2_05-hashes-BEFORE-rerun.txt` (copied into `experiments/` for V2-04). For EXP-V2-06 the archive holds only the post-rerun values (`experiments/EXP-V2-04_05_06-hashes-FINAL.txt`: `0432bf4b... exp_v2_06_raw.csv`, `9fe28efd... exp_v2_06_summary.csv`) and the record's own statement (`EXP-V2-06-multi-detector.md:37`). No BEFORE file for V2-06 exists in either directory.
- **Concern** The byte-for-byte claim for EXP-V2-06 cannot be checked by a reader, because the value it is compared against was not archived. (The claim may well be true; the point is what the archive can support.)
- **Why it matters** The whole value of the hash discipline is that the comparison is external and checkable; one of the four re-run experiments is currently not.
- **Resolution test** Archive a BEFORE file for EXP-V2-06 (or state in the record where the pre-rerun hash was recorded and cite it), so that all four re-runs have both sides of the comparison on disk.

### RC-m9

- **Concern ID** RC-m9
- **Severity** Minor
- **Blocking** No
- **Axis** internal consistency / stale text
- **Claim pointer** Section 5.5, item 1, lines 355-357: `If the scope effect fails to reproduce on a rig whose bearings are more uniform, the order-of-magnitude framing would have to be restricted to rigs with strong between-bearing variation`.
- **Evidence pointer** After the round-3 fix the manuscript makes no order-of-magnitude claim: Section 3.1 line 96 says `at least about 3.5-fold`, Section 5.1 line 303-304 and Section 7 line 400-401 repeat the 3.5-fold formulation, and Section 2.5 of the round-3 report required the clause to be deleted. The phrase survives only here.
- **Concern** A falsification condition is attached to a framing the paper no longer uses, so Section 5.5 item 1 currently reads as if the paper claimed an order of magnitude.
- **Why it matters** Section 5.5 is the paper's own statement of what would overturn it; a stale referent there confuses exactly the reader who is checking claim strength. It is also direct evidence for the operational rule proposed in `NUMBER_TRACEABILITY_AUDIT.md` Section 3 (count every occurrence of a claim before declaring a fix complete).
- **Resolution test** Rewrite item 1 in terms of the 3.5-fold lower bound, or delete it.

### RC-m10

- **Concern ID** RC-m10
- **Severity** Minor
- **Blocking** No
- **Axis** claim accuracy (protocol)
- **Claim pointer** Section 2, line 70: `Every experiment was pre-registered before it was run`.
- **Evidence pointer** Preregistration artifacts exist only from EXP-V1-06 onward (`experiments/EXP-V1-06-preregistration.md`, `EXP-V1-07-preregistration.md` plus two amendments, `EXP-V1-08`, `EXP-V1-09`, `EXP-V1-10` plus two amendments, `EXP-V1-11`, `EXP-V2-01` plus three amendments, `EXP-V2-02` plus one, `EXP-V2-03` plus one, `EXP-V2-04` plus two, `EXP-V2-05`, `EXP-V2-06`). There is no preregistration artifact for EXP-V1-00 through EXP-V1-05, and EXP-V1-05 is cited by the paper (Section 3.4's original single-fold observation; Section 3.5). EXP-V1-05's record does contain a frozen contract table (`EXP-V1-05-covariance-geometry.md` Section 1) but no separate pre-run artifact and no amendment trail. The project's own records classify EXP-V1-00~04 (and V2-01~03) as pre-protocol.
- **Concern** The blanket sentence is not supported for at least six experiments, one of which the paper cites. The disclosure in Section 3.5 covers verification depth but not preregistration depth, so the reader has no way to know which experiments had contracts frozen in advance.
- **Why it matters** The pre-registration claim is part of the paper's credibility argument; a referee who asks for the preregistration of a cited experiment will not find one.
- **Resolution test** Restrict the sentence to the experiments that have archived preregistrations and state that earlier experiments were run before the protocol was introduced (the brief's pre-protocol disclosure), or add the missing artifacts.

## Convergence check (round 3 items, plus spot checks on rounds 1-2)

### Round 3 Major items

- **RB-M1 (unsupported detector-versus-analyst comparison) - RESOLVED.** The abstract now reads
  `We measure each on its own estimand, on overlapping but different data, and we make no ordering
  claim between them or against detector choice` (lines 21-23); Section 1 restates the question as
  `not which detector is most accurate` (lines 48-49); Section 5.4 no longer ranks analyst choices
  against detector choice; Section 7 contains no ranking sentence. The overlap with round 1's
  R1-M4 is acknowledged in the round-3 report itself.
- **RB-M2 (lower bound written as an upper bound) - RESOLVED, with one stale remnant.** Section 3.1
  now reads `the increase is therefore at least about 3.5-fold ... This is a lower bound only: zero
  alarms in 24 recordings is also consistent with true rates well below the 11.7% bound, so ratios
  larger than ten cannot be excluded` (lines 94-96); Section 5.1 (lines 302-304) and Section 7
  (lines 399-401) carry the same formulation, and the phrase `not an order of magnitude` survives only
  as `3.5-fold rather than an order of magnitude`, which is now the correct direction. The remnant is
  Section 5.5 item 1, which still says `the order-of-magnitude framing would have to be restricted`
  (line 356) although the manuscript makes no such claim - reported as RC-m9.
- **RB-M3 (bimodal fold distribution reported as a mean) - RESOLVED.** The abstract gives the
  distribution (`a bimodal set of fold means, three at or below 1.55% and three at or above 69.40%`,
  lines 24-28); the Section 3.1 table row labels the result `bimodal` and lists the six fold values
  with mean, median and between-fold SD (line 88); Figure 1 panel (a) states `folds 0.4-97.1%`.
  I recomputed the six fold means from `EXP-V2-03-summary.csv` (`R2_bearing_holdout`, `S2_new_records`,
  `n_train = 96`): `0.00, 0.40, 1.55, 69.40, 75.35, 97.10`, mean 40.63%, median 35.48%, SD 44.76 pp,
  SE 18.27 pp - all as printed.

### Round 3 Minor items

- **RB-m1 (criterion in the column header) - RESOLVED in form, new label defect.** The header now
  reads `Negative rank correlation between k and SD` (line 116) and the boundary note explains the
  criterion (lines 131-132), but the frozen code computes a product-moment correlation - see RC-m7.
- **RB-m2 (name the experiment behind each table row) - NOT RESOLVED.** Section 3.2's three-row table
  still carries no experiment provenance; the only experiment identifiers in the whole manuscript are
  in Section 3.5 (lines 171-176) and Section 5.1 (line 293). A reader cannot learn that the
  Isolation Forest row is EXP-V2-05 while the 3-sigma RMS and Mahalanobis rows are EXP-V2-06.
- **RB-m3 (scope of the fold count) - PARTIALLY RESOLVED.** Section 3.4 now states the scheme and the
  feature group (`the empirical-covariance scheme and the RMS plus spectral-centroid feature group`,
  lines 165-166) and I reproduced the counts exactly under that filter: 27 folds, 24 of them IMS and
  3 MFPT, with exactly one inflation ratio above 1 (`MFPT baseline_3.mat`, 1.575592, 22 training
  windows). What is still missing is the **window length**: those 24 IMS folds use 0.25 s windows while
  the 3 MFPT folds use 1.0 s, so the count pools two window conventions without saying so.
- **RB-m4 (verification depth named for EXP-V2-01) - NAMING RESOLVED, CONTENT CONTRADICTED.**
  Section 3.5 now names EXP-V1-11, EXP-V2-01 and EXP-V2-02 (lines 174-176) and Limitations 6-7 repeat
  the statement, but the verification these sentences claim does not exist for those experiments -
  see RC-M2. The naming gap is closed; the underlying claim is now both more specific and less
  accurate.
- **RB-m5 (twenty windows in Section 5.2) - RESOLVED.** Section 5.2 now says `with four features and a
  training budget of twenty recordings, each contributing a single feature vector` (lines 319-321).
  Verified against `EXP-V2-05-preregistration.md` Section 4 (`1 record = 1 feature vector ... does not
  cut multiple windows`) and `src/runtofailure_data.py:48-53` (`window_sec = step_sec = record
  length`), and against the raw files' `n_train` values.
- **RB-m6 (archived product for the per-bearing RMS range) - RESOLVED, with a residual.**
  `experiments/EXP-V2-03-per-bearing-rms.csv` now backs the sentence and its six values reproduce
  exactly from the raw records under an independent RMS implementation (my own recomputation). The
  residual is that the file has no script or log - see RC-m6.
- **RB-m7 (qualifier in the abstract) - RESOLVED.** The abstract now reads `from a single deterministic
  evaluation with zero alarms in 24 recordings to a bimodal set of fold means` (lines 24-26).
- **RB-m8 (the fourteen-class count) - NOT RESOLVED, now a checkable contradiction.** The count is now
  attributed to a register, and the register does not support it - see RC-m2.
- **RB-m9 (Figure 1 caption generalising to four bearings) - RESOLVED.** The caption now says `k_max
  between 2 and 4, depending on the condition` (lines 422-423), which matches the raw cells
  (4, 4, 2 for PRONOSTIA; 3, 3, 4 for XJTU-SY).
- **RB-m10 (checklist outruns the paper's own reporting) - NOT RESOLVED.** No window count and no
  record-to-window conversion appears for the Section 3.1 or Section 3.6 numbers - see RC-m5.

### Spot checks on rounds 1-2 (not exhaustive, per the packet)

- Round 1 **S-M2** (the checklist had no evidence in the manuscript): now largely addressed - Section
  3.6 carries its own measurements for checklist items 1-5, and Section 5.4 links them to the observed
  effect sizes. Remaining asymmetry is item 1 against the paper's own n values (RC-m5).
- Round 1 **S-M3** (overlap with references [15]/[16]): now addressed in Section 4 by the three
  explicit increments and the sentence `We claim no novelty for these observations`.
- Round 1 **S-M4** (reproducibility statement contradicted by the audit): fixed once for EXP-V2-03, and
  then re-broken in the opposite direction for EXP-V1-11/V2-01/V2-02/V2-03 (RC-M2). The failure class
  recurs; the fix did not generalise.
- Round 1 **S-M5** (`data fixed` too strong): now `the same dataset` (line 82).
- Round 1 **S-M7** (dataset count): now `five public bearing sources` (abstract line 20).
- Round 2 **R1-M4** (no hyperparameter component in the decomposition; `C_both` omitted; no same-scale
  ranking): now disclosed in Section 3.6 (lines 198-203), including `we therefore make no claim about
  the size of the hyperparameter contribution`, and the ranking sentence is gone.
- Round 2 **R1-M5** (EXP-V2-01 scope): now disclosed - `under the within-bearing scope identified in
  Section 3.1 as the optimistic one`, `The second figure is a quantisation floor`, `must be read
  together with Section 3.1` (lines 205-210).
- Round 2 **R1-M8** (failed preregistered criterion not disclosed): now disclosed in Section 3.1
  (lines 99-105, the P1 criterion and the saturating resampling arm) and in Section 3.2 (lines 135-138,
  Z1/Z2 and the Mahalanobis reclassification).
- Round 2 minor **checklist cross-reference Section 3.5 -> Section 3.6**: still unfixed in the Figure 1
  caption (RC-m4). Round 2 minor **window length and per-dataset window counts missing from Section 2**:
  still unfixed (RC-m5, RC-m10) - so RC-m5 and RC-m10 are echoes of round 2, as noted in the provenance
  note.
- Round 2 **R1-M6** (criterion, fold counts, Mahalanobis exclusion): the criterion, the non-monotone
  cell, the per-cell bearing counts and the reclassification are all now disclosed. One residual:
  Limitations item 2 says `the unit effect is estimated from 3-4 bearings per cell within a condition`,
  while the sweep's per-cell k_max is 2-4 (PRONOSTIA C3 reaches only k = 2) and the available training
  pools are 6, 6, 2 and 3, 3, 4. Minor wording, not re-reported as a separate concern.

### Convergence verdict

Seven of the ten round-3 minors and all three round-3 majors are genuinely fixed, and the fixes are
visible in the text rather than only in the changelog. Three minors were not fixed (RB-m2, RB-m8,
RB-m10) and one was fixed in a way that introduced a new inaccuracy (RB-m1 -> RC-m7). The
substantive new findings of this round are the undefined dispersion measure (RC-M1), the four
experiments whose verification status was upgraded beyond what the archive records (RC-M2), the
absent reader execution path (RC-M3), and the unapplied evidence-grade discipline (RC-M4). None of
them affects the underlying measurements; all of them affect whether a reader can tell how those
measurements were produced and how far they extend.

## Risk and unsupported claims

1. The SD in Sections 3.2 and 3.3 is not defined; under a between-fold definition the same archive
   gives 2/6 (Isolation Forest), 4/6 (3-sigma RMS) and 0/6 (Mahalanobis) instead of 6/6, 6/6, 2/6, and
   a PRONOSTIA boundary range of 1.72 pp instead of 2.40 pp - below the preregistered X1 threshold.
2. The verification status claimed in Section 3.5 for EXP-V1-11, EXP-V2-01, EXP-V2-02 and EXP-V2-03
   is contradicted by the project's own records: no L1 output, no L2 output and no hash baseline exist
   for those four experiments.
3. The manuscript provides no resolvable path from paper to data, code, seeds, subsetting rule or
   licence, so a third party cannot reproduce it; the two inline archive pointers are private-repo
   relative paths.
4. The evidence-grade vocabulary (A-D) is asserted in Section 2 and used nowhere, so the confidence
   level of each of the three faces cannot be checked by a reader.
5. `Fourteen classes of analysis error ... listed in ... docs/EXPERIMENT_AFTERCARE.md` is not supported
   by that file, which lists fifteen entries (thirteen of them analysis-related).
6. `Holding the sample size fixed at 20 recordings` and `five recordings per bearing` are inaccurate
   for the k = 3 cells, where the executed training size is 18.
7. The Section 3.4 fold count of 26 independent folds pools 0.25 s IMS windows with 1.0 s MFPT windows
   without stating the window length.
8. `Every experiment was pre-registered before it was run` is not supported for EXP-V1-00 to EXP-V1-05,
   one of which (EXP-V1-05) the manuscript cites.
9. The byte-for-byte re-run claim for EXP-V2-06 has no archived pre-rerun baseline.
10. Section 5.5 item 1 still refers to an order-of-magnitude framing the manuscript no longer uses.
11. Section 2's dataset sizes describe the project's subsets, not the datasets (IMS `1st_test` is
    represented by 12 recordings selected by a filename prefix out of 15 present, and no rule or
    reason is given).
12. Figure 1 has no source-data table and its numbers live only in an uncited plotting script; the
    caption's QA cross-reference points at Section 3.5.

## Closing statement

This is a fourth, non-blind, internal quality-control review. Taking the arithmetic as given - and it
holds up under independent recomputation for every number I checked, including a from-raw-data
recomputation of the Section 5.1 values - the manuscript's remaining weaknesses are those of a paper
whose internal record is richer than what it shows the reader: an unstated definition behind its
central dispersion numbers, a verification sentence that outruns its own archive, no reproducible
execution path, and a grading discipline that is claimed but never applied. The first two are
correctable without new experiments and should be corrected before submission; the third is a writing
task; the fourth is a decision about how much of the project's internal discipline to expose. Nothing
found in this round changes the direction of any of the three reported effects.
