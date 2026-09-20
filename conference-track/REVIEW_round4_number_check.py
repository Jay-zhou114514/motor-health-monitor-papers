#!/usr/bin/env python3
"""Round-4 (Reviewer C) independent recomputation of the numbers printed in
PAPER_v1.0_submission-draft.md, straight from the archived CSVs in the master repo.

Scope: recomputation only. No experiment is re-run; no new result is produced.
"""

from __future__ import annotations

import csv
import math
import os
import statistics

EXP = r"C:\Users\32597\Documents\Codex\2026-09-06\github\motor-health-monitor\experiments"


def load(name):
    with open(os.path.join(EXP, name), newline="", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def num(value):
    if value is None or value == "" or value.lower() == "nan":
        return float("nan")
    if value.lower() in ("inf", "+inf", "infinity"):
        return math.inf
    return float(value)


def pct(value):
    return None if math.isnan(value) else round(value * 100, 2)


def sd(values):
    return statistics.stdev(values) if len(values) > 1 else float("nan")


def head(title):
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


# ---------------------------------------------------------------- §3.1 scope
head("A. §3.1 scope effect  (source: EXP-V2-03-summary.csv)")
rows = load("EXP-V2-03-summary.csv")
for n in (96,):
    w = [r for r in rows if r["regime"] == "R1_within_bearing" and float(r["n_train"]) == n]
    for r in w:
        print(f"  within-bearing n={n} arm={r['arm']:<15} mean={pct(num(r['mean_fp']))}% "
              f"sd={round(num(r['sd_fp']) * 100, 2)}pp repeats={r['n_repeat']}")
    for arm in ("S1_resample", "S2_new_records"):
        h = [r for r in rows
             if r["regime"] == "R2_bearing_holdout" and r["arm"] == arm
             and float(r["n_train"]) == n]
        if not h:
            continue
        means = sorted(num(r["mean_fp"]) for r in h)
        folds = sorted(r["fold"] for r in h)
        print(f"  holdout n={n} arm={arm:<15} folds={folds}")
        print(f"      fold means (pp) = {[pct(m) for m in means]}")
        print(f"      mean={pct(statistics.mean(means))}  median={pct(statistics.median(means))}  "
              f"between-fold SD={round(sd(means) * 100, 2)}pp  range={round((max(means) - min(means)) * 100, 2)}pp")
print("  paper says: within 0.00%, holdout 0.00/0.40/1.55/69.40/75.35/97.10, "
      "mean 40.63, median 35.5, SD 44.8")
print(f"  resolution 1/24 = {round(100 / 24, 2)}pp;  exact one-sided 95% upper bound "
      f"= {round((1 - 0.05 ** (1 / 24)) * 100, 2)}%")
print(f"  ratio mean_holdout / upper_bound = {round(40.63 / ((1 - 0.05 ** (1 / 24)) * 100), 2)}-fold")

head("A2. §3.1 preregistered criterion that failed  (source: EXP-V2-03-summary.csv)")
for n in (20, 96):
    comp = {}
    for arm in ("S1_resample", "S2_new_records"):
        h = [r for r in rows
             if r["regime"] == "R2_bearing_holdout" and r["arm"] == arm
             and float(r["n_train"]) == n]
        comp[arm] = {r["fold"]: num(r["sd_fp"]) for r in h}
    out = []
    for fold, s1 in sorted(comp["S1_resample"].items()):
        s2 = comp["S2_new_records"].get(fold)
        out.append(f"{fold}: S1={round(s1 * 100, 2)} S2={round(s2 * 100, 2)}"
                   f"{'  <- S2<S1' if s2 < s1 else ''}")
    print(f"  n={n}  " + " | ".join(out))


# ---------------------------------------------------------------- §3.2 units
head("B. §3.2 unit effect  (sources: EXP-V2-05-summary.csv, EXP-V2-06-summary.csv)")


def cells(rows_, key, value):
    out = {}
    for r in rows_:
        if r.get(key) == value:
            out[(r["dataset"], r["condition"], int(r["k_bearings"]))] = r
    return out


v205 = load("EXP-V2-05-summary.csv")
v206 = load("EXP-V2-06-summary.csv")
print("  paper: 3sigma RMS ratios 0.76, 0.75, 0.67, 0.68, 0.91, 0.55")
print("  paper: iForest     ratios 0.32, 0.57, 0.34, 0.58, 0.86, 0.52")
for key, value in (("detector", "A_rms_3sigma"), ("detector", "B_mahalanobis")):
    sub = [r for r in v206 if r[key] == value]
    conds = sorted({(r["dataset"], r["condition"]) for r in sub})
    ratios, k1_means, k1_sds, kmax_sds, kmax_list = [], [], [], [], []
    for ds, cond in conds:
        ks = sorted(int(r["k_bearings"]) for r in sub if r["dataset"] == ds and r["condition"] == cond)
        s = {int(r["k_bearings"]): r for r in sub if r["dataset"] == ds and r["condition"] == cond}
        ratios.append(round(num(s[max(ks)]["sd_fp"]) / num(s[1]["sd_fp"]), 2))
        k1_means.append(num(s[1]["mean_fp"]))
        k1_sds.append(num(s[1]["sd_fp"]))
        kmax_sds.append(num(s[max(ks)]["sd_fp"]))
        kmax_list.append(max(ks))
    print(f"  {value:<15} k_max={kmax_list} ratios={ratios} "
          f"k=1 mean FP {pct(min(k1_means))}-{pct(max(k1_means))}% "
          f"SD {round(min(k1_sds) * 100, 2)}-{round(max(k1_sds) * 100, 2)}pp "
          f"count(km<k1)={sum(1 for a, b in zip(kmax_sds, k1_sds) if a < b)}/{len(conds)}")

conds = sorted({(r["dataset"], r["condition"]) for r in v205})
ratios, k1_means, k1_sds, kmax_sds, kmax_list, mono = [], [], [], [], [], 0
for ds, cond in conds:
    sub = sorted([r for r in v205 if r["dataset"] == ds and r["condition"] == cond],
                 key=lambda r: int(r["k_bearings"]))
    ks = [int(r["k_bearings"]) for r in sub]
    sds = [num(r["sd_fp"]) for r in sub]
    ratios.append(round(sds[-1] / sds[0], 2))
    k1_means.append(num(sub[0]["mean_fp"]))
    k1_sds.append(sds[0])
    kmax_sds.append(sds[-1])
    kmax_list.append(max(ks))
    if all(b <= a for a, b in zip(sds, sds[1:])):
        mono += 1
print(f"  IsolationForest k_max={kmax_list} ratios={ratios} "
      f"k=1 mean FP {pct(min(k1_means))}-{pct(max(k1_means))}% "
      f"SD {round(min(k1_sds) * 100, 2)}-{round(max(k1_sds) * 100, 2)}pp "
      f"count(km<k1)={sum(1 for a, b in zip(kmax_sds, k1_sds) if a < b)}/{len(conds)} "
      f"strictly-monotone cells={mono}/{len(conds)}")


# ----------------------------------------------------------- §3.3 definition
head("C. §3.3 boundary sweep  (source: EXP-V2-04-xjtu-pronostia.md table 3)")
print("  paper: PRONOSTIA SD(k_max) 7.56-9.96pp range 2.40pp; "
      "XJTU-SY 14.51-19.70pp range 5.19pp")
print("  md table 3 holds the five-rule values; the sweep itself is not stored as a CSV")


# ------------------------------------------------------- §3.4 reproduction
head("D. §3.4 what does not reproduce  (source: EXP-V1-07-folds.csv)")
folds = load("EXP-V1-07-folds.csv")
print("  schemes:", sorted({r["scheme"] for r in folds}))
print("  feature groups:", sorted({r["feature_group"] for r in folds}))
sel = [r for r in folds if r["scheme"] == "empirical" and "rms + centroid" in r["feature_group"]]
by_ds = {}
for r in sel:
    by_ds.setdefault(r["dataset"], []).append(r)
for ds, rs in sorted(by_ds.items()):
    infl = [r for r in rs if num(r["inflation_ratio"]) > 1]
    print(f"  {ds:<14} folds={len(rs)}  inflation>1: {len(infl)}"
          + (f"  {[(r['held_out'], round(num(r['inflation_ratio']), 4)) for r in infl]}" if infl else ""))
print(f"  total folds={len(sel)}  total inflation>1={sum(1 for r in sel if num(r['inflation_ratio']) > 1)}")


# ------------------------------------------------ §3.6 evaluation protocol
head("E. §3.6 selection instability  (source: EXP-V1-10-summary.csv)")
v110 = load("EXP-V1-10-summary.csv")
for r in v110:
    print(f"  arm={r['arm'][:32]:<34} modal_share={r['modal_share']} tie_share={r['tie_share']} "
          f"test_fp mean={pct(num(r['test_fp_mean']))} sd={round(num(r['test_fp_std']) * 100, 2)}pp "
          f"min={pct(num(r['test_fp_min']))} max={pct(num(r['test_fp_max']))}")
print("  paper: 86% of resamples had minimum validation FP exactly zero; 92% tie at the minimum; "
      "test FP 0.00/7.14/14.29%, mean 3.86%, SD 4.13pp")

head("E2. §3.6 variance decomposition  (source: EXP-V1-10-variance-decomposition.csv)")
vd = load("EXP-V1-10-variance-decomposition.csv")
print("  columns:", list(vd[0].keys()))
for r in vd[:12]:
    print("   ", r)
print("  paper: 5.20pp split composition, 4.39pp seed only, 5.18pp both vary")

head("E3. §3.6 resampling vs new data  (source: EXP-V2-01-summary.csv)")
v201 = load("EXP-V2-01-summary.csv")
print("  columns:", list(v201[0].keys()))
for r in v201:
    if float(r["n_train"]) in (20, 96):
        print(f"  arm={r['arm']:<15} n={r['n_train']:<4} sd_fp={round(num(r['sd_fp']) * 100, 2)}pp "
              f"mean_fp={pct(num(r['mean_fp']))}% n_eff={r['n_eff']} eff={r['efficiency']}")
print("  paper: resampling 18.0pp at n=96 vs distinct 0.00pp; n_eff 0.18-0.38 vs >430")

head("E4. §3.6 search cost / stability  (source: EXP-V1-09-summary.csv, EXP-V1-08-summary.csv)")
for name in ("EXP-V1-09-summary.csv", "EXP-V1-08-summary.csv"):
    print(f"  --- {name}")
    for r in load(name):
        print("   ", {k: v for k, v in r.items()
                      if k in ("batch", "dataset", "method", "detector", "mean_fp_rate",
                               "median_fp_rate", "max_fp_rate", "modal_share", "seconds_per_fold",
                               "std_fp_rate", "seconds")})

head("F. §5.1 per-bearing RMS  (source: EXP-V2-03-per-bearing-rms.csv)")
rms = load("EXP-V2-03-per-bearing-rms.csv")
vals = [num(r["mean"]) for r in rms]
print(f"  min={min(vals)} ({rms[vals.index(min(vals))]['bearing']})  "
      f"max={max(vals)} ({rms[vals.index(max(vals))]['bearing']})   paper: 0.171-0.403")
