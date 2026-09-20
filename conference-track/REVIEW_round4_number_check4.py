#!/usr/bin/env python3
"""Round-4 reviewer support, part 4: EXP-V1-10 selection-criterion claims
(86% zero-minimum, 92% tie) recomputed from the per-replicate archive."""

from __future__ import annotations

import csv
import os

EXP = r"C:\Users\32597\Documents\Codex\2026-09-06\github\motor-health-monitor\experiments"


def load(name):
    with open(os.path.join(EXP, name), newline="", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


rows = load("EXP-V1-10-replicates.csv")
print("columns:", list(rows[0].keys()))
print("designs:", sorted({r["design"] for r in rows}),
      "methods:", sorted({r["method"] for r in rows}))
print("rows:", len(rows))

for design in sorted({r["design"] for r in rows}):
    for method in sorted({r["method"] for r in rows}):
        sel = [r for r in rows if r["design"] == design and r["method"] == method]
        if not sel:
            continue
        reps = sorted({r["replicate"] for r in sel})
        zero = tie = 0
        for rep in reps:
            cell = [r for r in sel if r["replicate"] == rep]
            # the selection rule picks the smallest validation FP; the archive stores
            # the selected configuration per replicate together with n_tied_at_min
            best = min(float(r["val_fp"]) for r in cell)
            if best == 0.0:
                zero += 1
            chosen = cell[0]
            if int(chosen["n_tied_at_min"]) >= 2:
                tie += 1
        print(f"  design={design} method={method:<8} replicates={len(reps)} "
              f"zero-minimum share={round(zero / len(reps), 3)} tie share={round(tie / len(reps), 3)}")

print()
print("paper §3.6: 'the minimum validation false-alarm rate was exactly zero in 86% of")
print("resamples and at least two candidate configurations tied at that minimum in 92%'")
print("EXP-V1-10-summary.csv carries tie_share=0.92 and modal_share=0.88 for design A (forest).")
