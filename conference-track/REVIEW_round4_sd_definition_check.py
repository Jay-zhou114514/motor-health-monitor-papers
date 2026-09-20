#!/usr/bin/env python3
"""Check the round-4 claim that the Section 3.2 verdicts depend on an undefined SD pooling.

For every (detector, dataset, condition) cell this computes the between-fold SD of the
per-fold mean false-alarm rate and asks whether SD(k_max) < SD(k=1) still holds.
"""

from __future__ import annotations

import csv
import os
import statistics as st

EXP = r"C:\Users\32597\Documents\Codex\2026-09-06\github\motor-health-monitor\experiments"

KNOWN = {
    "EXP-V2-05-summary.csv": {"Isolation Forest": "6/6 under pooled SD"},
    "EXP-V2-06-summary.csv": {"A_rms_3sigma": "6/6 under pooled SD",
                              "B_mahalanobis": "2/6 under pooled SD"},
}


def load(name):
    with open(os.path.join(EXP, name), newline="", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def cells_for(rows):
    groups = {}
    for r in rows:
        detector = r.get("detector") or "Isolation Forest"
        key = (detector, r["dataset"], r["condition"])
        groups.setdefault(key, {}).setdefault(int(r["k_bearings"]), {}).setdefault(
            r["held_out"], []).append(float(r["test_fp"]))
    return groups


for name in ("EXP-V2-05-raw.csv", "EXP-V2-06-raw.csv"):
    print("=" * 78)
    print(name)
    print("=" * 78)
    verdict = {}
    for key, by_k in sorted(cells_for(load(name)).items()):
        detector, dataset, condition = key
        stats = []
        for k, folds in sorted(by_k.items()):
            fold_means = [sum(v) / len(v) for v in folds.values()]
            stats.append((k, round(st.stdev(fold_means) * 100, 2) if len(fold_means) > 1 else None,
                          len(fold_means)))
        k1 = next(s for s in stats if s[0] == 1)
        kmax = stats[-1]
        mono = all(b[1] is not None and a[1] is not None and b[1] <= a[1]
                   for a, b in zip(stats, stats[1:]))
        ok = kmax[1] is not None and k1[1] is not None and kmax[1] < k1[1]
        verdict.setdefault(detector, []).append(ok)
        print(f"  {detector:<16} {dataset:<10} {condition:<14} "
              f"k=1 between-fold SD {k1[1]} pp (folds={k1[2]}) -> "
              f"k={kmax[0]} {kmax[1]} pp | SD drops: {'yes' if ok else 'NO'} "
              f"| monotone: {'yes' if mono else 'no'}")
    for detector, flags in verdict.items():
        print(f"  ==> {detector}: {sum(flags)}/{len(flags)} cells satisfy "
              f"SD(k_max) < SD(k=1) under the between-fold definition "
              f"(paper claims {KNOWN[name].get(detector, '?')})")
