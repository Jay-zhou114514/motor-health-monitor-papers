#!/usr/bin/env python3
"""Summary of the pooled-vs-between-fold SD comparison for every detector in Section 3.2."""

from __future__ import annotations

import csv
import os
import statistics as st

EXP = r"<WORKDIR>\Documents\Codex\2026-09-06\github\motor-health-monitor\experiments"
CLAIMED = {
    "EXP-V2-05-raw.csv": {"Isolation Forest": "6/6 (pooled SD)"},
    "EXP-V2-06-raw.csv": {"A_rms_3sigma": "6/6 (pooled SD)",
                          "B_mahalanobis": "2/6 (pooled SD)"},
}


def load(name):
    with open(os.path.join(EXP, name), newline="", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


for name in ("EXP-V2-05-raw.csv", "EXP-V2-06-raw.csv"):
    rows = load(name)
    by_detector = {}
    for r in rows:
        detector = r.get("detector") or "Isolation Forest"
        cell = (r["dataset"], r["condition"])
        by_detector.setdefault(detector, {}).setdefault(cell, {}).setdefault(
            int(r["k_bearings"]), {}).setdefault(r["held_out"], []).append(float(r["test_fp"]))
    print("=" * 78)
    print(f"{name}: between-fold SD (SD of per-fold mean rates)")
    print("=" * 78)
    for detector, cells in sorted(by_detector.items()):
        flags = []
        for cell, by_k in sorted(cells.items()):
            sd = {}
            for k, folds in by_k.items():
                means = [sum(v) / len(v) for v in folds.values()]
                sd[k] = st.stdev(means) * 100 if len(means) > 1 else float("nan")
            k1, kmax = min(sd), max(sd)
            ok = sd[kmax] < sd[k1]
            flags.append(ok)
            print(f"  {detector:<16} {cell[0]:<10} {cell[1]:<14} "
                  f"k=1 {sd[k1]:6.2f} pp -> k={kmax} {sd[kmax]:6.2f} pp   "
                  f"{'drops' if ok else 'DOES NOT DROP'}")
        print(f"  ==> {detector}: {sum(flags)}/{len(flags)} cells drop "
              f"| paper/figure claim: {CLAIMED[name].get(detector, '?')}")
        print()
