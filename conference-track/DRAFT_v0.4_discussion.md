# Draft v0.4 — Discussion

> 承接 `DRAFT_v0.3_partIV.md`（Results）。引用编号对应 `REFERENCES.md`。
> 纪律：只讨论已登记的 C1–C10；对既有工作的重叠必须主动声明。

---

## 5. Discussion

### 5.1 Why holding out a physical unit changes the number so much

The scope effect (§3.1) is large — 0.00% versus 40.63% — and it is not a subtle statistical
artefact. When the test recordings come from bearings the detector was fitted on, the
detector has effectively seen that bearing's baseline level; when the whole bearing is held
out, the threshold must generalise across bearings, and the healthy recordings of the new
bearing sit at a different operating point. In our data the between-bearing spread is
substantial: per-bearing mean RMS ranges from 0.17 to 0.40 on the Paderborn healthy set.
The reported false-alarm rate is therefore dominated by *which physical units* the split
keeps apart, well before any question of model choice arises.

This is consistent with prior work that identified leakage from segment- and
condition-wise splitting and proposed bearing-wise splitting [15], and with recording-level
separation in cross-domain benchmarking [16]. **We claim no novelty for the observation
that leakage inflates apparent performance.** Our contribution is that the same effect,
measured on the *false-alarm rate* under healthy-data-only training, moves the number by
an order of magnitude, and that it can be quantified in a single controlled comparison.

### 5.2 Why the unit effect disappears for some detectors

§3.2 shows the unit effect clearly for two detectors and not at all for the third, and the
reason is saturation rather than disagreement. With a single training bearing the
Mahalanobis detector alarms on 67–100% of the healthy recordings of a different bearing,
and in one cell on 100% exactly — the metric has no room left to vary, so its spread
collapses to zero and the test "does the spread decrease?" becomes undefined.

This matters beyond bookkeeping. **A detector that is saturated cannot be evaluated by
its false-alarm rate at all, because the rate has reached its ceiling.** Reporting a
false-alarm rate for such a configuration is not wrong so much as uninformative. We
therefore state the unit effect as holding *for non-saturated detectors*, and treat
saturation as a scope condition rather than a failure to report.

We also note an alternative reading of the Mahalanobis result: with four features and
about twenty windows, the empirical covariance is itself poorly estimated, so the
saturation may reflect estimator instability rather than a property of the detector
family. Both readings lead to the same practical conclusion for this configuration, and
we do not claim to separate them.

### 5.3 The healthy/degraded boundary is a free parameter

For run-to-failure data there is no onset label: the split between "healthy" and
"degraded" is chosen by the analyst, and whatever is chosen becomes the ground truth
against which false alarms are counted. §3.3 shows that this choice alone moves the
reported uncertainty by 2.4–5.2 percentage points, and that the same rule can be binding
on opposite sides in different datasets (a floor of 20 windows in one, a cap of 60 in the
other).

We emphasise what this is *not*: it is not a claim that any particular boundary is wrong,
and it is not a new method for finding degradation onset. Detecting the first prediction
time is an established problem with a substantial literature [B–series in REFERENCES].
Our claim is narrower and, we think, more immediately useful: **the boundary is a
reporting parameter, and its influence on the reported number should be measured and
disclosed, exactly as one would disclose a threshold or a split.**

### 5.4 A checklist rather than a method

The practical output of this study is the five-point checklist in §3.5. It requires no new
model and no additional data collection beyond what a careful practitioner would already
have; it changes only what is reported. Read against the observed effect sizes, the
consequences are concrete: a study that reports a single within-bearing number may
present a detector with a 40% false-alarm rate as having none; a study that reports a
single training size may present a number that is an artefact of its split; and a study
that does not disclose its healthy/degraded boundary may present a number that moves by
several percentage points under a defensible alternative.

### 5.5 What would change our conclusions

We state the falsifiers explicitly.

1. If the scope effect (§3.1) fails to reproduce on a rig whose bearings are more uniform,
   the "order of magnitude" framing would have to be restricted to rigs with strong
   between-bearing variation.
2. If the unit effect (§3.2) is shown to arise from the covariance estimator rather than
   from unit diversity, the recommendation would shift from "more bearings" toward
   "better-regularised estimators".
3. If the healthy-boundary sensitivity (§3.3) proves negligible for other rules and
   datasets, the boundary would remain a reporting detail rather than a first-order
   parameter.
4. If a prospective, self-collected dataset contradicts any of the above, that dataset
   takes precedence — none of our evidence is from our own hardware.

---

## 6. Limitations (draft)

1. **All evidence is from public datasets** (IMS, MFPT, Paderborn, XJTU-SY, PRONOSTIA);
   no self-collected data. Cross-rig generality is asserted only in the limited sense of
   "consistent across the rigs studied".
2. **Few independent units**: 6 physical bearings (Paderborn), 15 (XJTU-SY), 17
   (PRONOSTIA). The unit effect is estimated from 3–4 bearings per cell within a
   condition.
3. **One detector family**: all detectors use a quantile of the training score
   distribution. The Mahalanobis result is reported as not testable (saturation).
4. **The healthy-phase rule was chosen by us** (H = clip(max(20, 0.10N), 20, 60),
   H/N ≤ 0.25); it is defended by a sensitivity sweep, not by an external label.
5. **Confounds we disclose rather than remove**: within the XJTU-SY boundary sweep the
   rule also changes which bearings qualify; the cross-condition unit comparison is
   confounded with operating-condition diversity.
6. **Verification is not uniform across experiments**: four experiments were re-run and
   compared hash-for-hash; older experiments have invariant and recomputation checks plus
   a stored hash baseline, but no re-run comparison.
7. **Literature scope**: the search covered Scopus and arXiv; Chinese-language venues and
   PHM conference proceedings are not comprehensively covered.