#!/usr/bin/env python3
"""Round-4 reviewer support: remaining recomputations (part B onwards).

Companion to REVIEW_round4_number_check.py, which aborted on a division by zero
in the saturated Mahalanobis cell. This part guards that case and covers §3.2
(all detectors), §3.4, §3.6 and §5.1.
"""

from __future__ import annotations

import csv
import math
import os
import statistics

EXP = r"<WORKDIR>\Documents\Codex\2026-09-06\github\motor-health-monitor\experiments"


def load(name):
    with open(os.path.join(EXP, name), newline="", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def num(value):
    if value is None or value == "" or value.lower() == "nan":
        return float("nan")
    return float(value)


def pct(value):
    return None if math.isnan(value) else round(value * 100, 2)


def head(title):
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


head("B. §3.2 unit effect, all three detectors (EXP-V2-05 / EXP-V2-06)")
v205 = load("EXP-V2-05-summary.csv")
v206 = load("EXP-V2-06-summary.csv")
print("  paper: 3sigma ratios 0.76,0.75,0.67,0.68,0.91,0.55 ; "
      "iForest ratios 0.32,0.57,0.34,0.58,0.86,0.52")
print("  paper: Mahalanobis k=1 mean FP 66.8-100%, one cell exactly 100%, SD 0.0-35.4pp")


def sweep(rows, filter_key, filter_value):
    conds = sorted({(r["dataset"], r["condition"]) for r in rows if r[filter_key] == filter_value})
    out = []
    for ds, cond in conds:
        ks = sorted(int(r["k_bearings"]) for r in rows
                    if r[filter_key] == filter_value and r["dataset"] == ds and r["condition"] == cond)
        by_k = {int(r["k_bearings"]): r for r in rows
                if r[filter_key] == filter_value and r["dataset"] == ds and r["condition"] == cond}
        sds = [num(by_k[k]["sd_fp"]) for k in ks]
        base = num(by_k[ks[0]]["sd_fp"])
        out.append({
            "cell": f"{ds}/{cond}",
            "k": ks,
            "k1_mean": num(by_k[ks[0]]["mean_fp"]),
            "k1_sd": base,
            "kmax_sd": sds[-1],
            "ratio": None if base == 0 else round(sds[-1] / base, 2),
            "km_lt_k1": sds[-1] < base,
            "monotone": all(b <= a for a, b in zip(sds, sds[1:])),
            "n": by_k[ks[0]]["n"],
            "folds": by_k[ks[0]]["folds"],
        })
    return out


for label, rows, key, value in (
    ("3sigma RMS", v206, "detector", "A_rms_3sigma"),
    ("Mahalanobis", v206, "detector", "B_mahalanobis"),
    ("IsolationForest", v205, "dataset", "PRONOSTIA"),
):
    if label == "IsolationForest":
        cells = []
        for ds in sorted({r["dataset"] for r in v205}):
            cells.extend(sweep(v205, "dataset", ds))
    else:
        cells = sweep(rows, key, value)
    print(f"  --- {label}  (n={cells[0]['n']}, folds={cells[0]['folds']})")
    for c in cells:
        print(f"      {c['cell']:<22} k={c['k']} k1: mean {pct(c['k1_mean'])}% SD {round(c['k1_sd'] * 100, 2)}pp"
              f" | kmax SD {round(c['kmax_sd'] * 100, 2)}pp ratio {c['ratio']}"
              f" | monotone={c['monotone']}")
    print(f"      ratios = {[c['ratio'] for c in cells]}")
    print(f"      k_max = {[max(c['k']) for c in cells]}")
    print(f"      count(kmax SD < k=1 SD) = {sum(1 for c in cells if c['km_lt_k1'])}/{len(cells)}"
          f"   strictly monotone = {sum(1 for c in cells if c['monotone'])}/{len(cells)}")
    print(f"      k=1 mean FP range {pct(min(c['k1_mean'] for c in cells))}-{pct(max(c['k1_mean'] for c in cells))}%"
          f"   k=1 SD range {round(min(c['k1_sd'] for c in cells) * 100, 2)}"
          f"-{round(max(c['k1_sd'] for c in cells) * 100, 2)}pp")

head("D. §3.4 reproduction count (EXP-V1-07-folds.csv)")
folds = load("EXP-V1-07-folds.csv")
print("  schemes:", sorted({r["scheme"] for r in folds}))
print("  feature groups:", sorted({r["feature_group"] for r in folds}))
sel = [r for r in folds if r["scheme"] == "empirical" and r["feature_group"].startswith("rms + centroid")]
by_ds = {}
for r in sel:
    by_ds.setdefault(r["dataset"], []).append(r)
for ds, rs in sorted(by_ds.items()):
    infl = [r for r in rs if num(r["inflation_ratio"]) > 1]
    print(f"  {ds:<16} folds={len(rs):<4} inflation>1: {len(infl)} "
          f"{[(r['held_out'], round(num(r['inflation_ratio']), 4)) for r in infl]}")
print(f"  TOTAL folds={len(sel)}  inflation>1={sum(1 for r in sel if num(r['inflation_ratio']) > 1)}")

head("E. §3.6 selection instability (EXP-V1-10-summary.csv)")
for r in load("EXP-V1-10-summary.csv"):
    print(f"  arm={r['arm'][:34]:<36} modal_share={r['modal_share']:<6} tie_share={r['tie_share']:<6} "
          f"test_fp mean={pct(num(r['test_fp_mean']))}% sd={round(num(r['test_fp_std']) * 100, 2)}pp "
          f"min={pct(num(r['test_fp_min']))}% max={pct(num(r['test_fp_max']))}% "
          f"n_distinct_cfg={r['n_distinct_cfg']} val_fp_mean={pct(num(r['val_fp_mean']))}%")
print("  paper: 92% tie at minimum; 86% had minimum validation FP exactly zero; "
      "test FP values 0.00/7.14/14.29%, mean 3.86%, SD 4.13pp")

head("E2. §3.6 variance decomposition (EXP-V1-10-variance-decomposition.csv)")
vd = load("EXP-V1-10-variance-decomposition.csv")
print("  columns:", list(vd[0].keys()))
for r in vd:
    print("   ", r)

head("E3. §3.6 resampling vs new recordings (EXP-V2-01-summary.csv)")
v201 = load("EXP-V2-01-summary.csv")
print("  columns:", list(v201[0].keys()))
for r in v201:
    print(f"  arm={r['arm']:<15} n={r['n_train']:<4} sd_fp={round(num(r['sd_fp']) * 100, 2)}pp "
          f"mean_fp={pct(num(r['mean_fp']))}% n_eff={r['n_eff']} eff={r['efficiency']}")
print("  paper: resampling 18.0pp at n=96 vs distinct 0.00pp; n_eff 0.18-0.38 vs >430")

head("E4. §3.6 search cost and stability (EXP-V1-09-summary, EXP-V1-08-summary)")
for name in ("EXP-V1-09-summary.csv", "EXP-V1-08-summary.csv"):
    print(f"  --- {name}")
    for r in load(name):
        print("   ", {k: v for k, v in r.items() if k not in ("", )})

head("F. §5.1 per-bearing RMS (EXP-V2-03-per-bearing-rms.csv)")
rms = load("EXP-V2-03-per-bearing-rms.csv")
vals = [num(r["mean"]) for r in rms]
print(f"  min={min(vals)} ({rms[vals.index(min(vals))]['bearing']}) "
      f"max={max(vals)} ({rms[vals.index(max(vals))]['bearing']})  paper: 0.171-0.403")
