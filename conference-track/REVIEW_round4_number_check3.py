#!/usr/bin/env python3
"""Round-4 reviewer support, part 3: §3.4 fold counts, §3.6 variance decomposition,
the 86% zero-minimum claim, and the window/recording bookkeeping."""

from __future__ import annotations

import csv
import os
import statistics

EXP = r"<WORKDIR>\Documents\Codex\2026-09-06\github\motor-health-monitor\experiments"


def load(name):
    with open(os.path.join(EXP, name), newline="", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def head(title):
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


head("D. §3.4 reproduction count (EXP-V1-07-folds.csv)")
folds = load("EXP-V1-07-folds.csv")
sel = [r for r in folds
       if r["scheme"] == "empirical"
       and "RMS" in r["feature_group"] and "centroid" in r["feature_group"]]
print("  selected feature_group values:", sorted({r["feature_group"] for r in sel}))
by_ds = {}
for r in sel:
    by_ds.setdefault(r["dataset"], []).append(r)
for ds, rs in sorted(by_ds.items()):
    infl = [r for r in rs if float(r["inflation_ratio"]) > 1]
    print(f"  {ds:<16} folds={len(rs):<4} inflation>1: {len(infl)} "
          f"{[(r['held_out'], round(float(r['inflation_ratio']), 4)) for r in infl]}")
print(f"  TOTAL folds={len(sel)}  inflation>1={sum(1 for r in sel if float(r['inflation_ratio']) > 1)}")
print("  paper: 0 of 26 (IMS 0 of 24, MFPT 0 of 2 further), the 1.576 MFPT fold is the original case")
print("  all-scheme totals:", {ds: sum(1 for r in folds if r["dataset"] == ds) for ds in sorted({r["dataset"] for r in folds})})

head("E2. §3.6 variance decomposition, recomputed (EXP-V1-10-variance-decomposition.csv)")
vd = load("EXP-V1-10-variance-decomposition.csv")
groups = {}
for r in vd:
    groups.setdefault(r["component"], []).append(float(r["test_pct_mean"]))
for comp, values in groups.items():
    print(f"  {comp:<20} n={len(values):<4} mean={round(statistics.mean(values) * 100, 2)}% "
          f"SD={round(statistics.stdev(values) * 100, 2)}pp")
print("  paper: 5.20pp split composition, 4.39pp seed only, 5.18pp both vary")

head("E5. §3.6 '86% had minimum validation FP exactly zero' - where does it live?")
for name in ("EXP-V1-10-null.csv", "EXP-V1-10-extra-checks.csv", "EXP-V1-10-controls.csv",
             "EXP-V1-10-summary.csv"):
    rows = load(name)
    print(f"  {name}: columns={list(rows[0].keys())} rows={len(rows)}")
for name in ("EXP-V1-10-null.csv", "EXP-V1-10-extra-checks.csv", "EXP-V1-10-controls.csv"):
    for r in load(name):
        flat = " ".join(str(v) for v in r.values())
        if "0.86" in flat or "86" == str(r.get("share", "")).strip():
            print(f"    {name}: {r}")

head("G. window/recording bookkeeping")
for name in ("EXP-V2-03-summary.csv", "EXP-V2-05-summary.csv", "EXP-V2-06-summary.csv",
             "EXP-V2-01-summary.csv"):
    rows = load(name)
    ns = sorted({r.get("n") for r in rows if r.get("n")})
    print(f"  {name}: n values = {ns[:8]}{'...' if len(ns) > 8 else ''}"
          f"   (n_train values = {sorted({r['n_train'] for r in rows if 'n_train' in r})[:8]})")
