#!/usr/bin/env python3
"""Add the two missing archive products requested by round-4 review.

1. EXP-V2-04-boundary-sweep.csv  - the five healthy-phase rules with their per-rule SD(k_max),
   parsed out of the experiment record (the record is the only place that carries rule labels).
2. EXP-V1-10-arm-extras.csv      - zero-minimum share per design/method, computed from
   EXP-V1-10-replicates.csv, with an explicit note that the archived file has no arm label.
Both are written into the master repo's experiments/ directory.
"""

from __future__ import annotations

import csv
import io
import os
import re

EXP = r'<WORKDIR>\Documents\Codex\2026-09-06\github\motor-health-monitor\experiments'
RECORD = os.path.join(EXP, 'EXP-V2-04-xjtu-pronostia.md')

# ---------------------------------------------------------------- product 1
with io.open(RECORD, 'r', encoding='utf-8', newline='') as fh:
    md = fh.read()

rows = []
for line in md.split('\n'):
    if not line.strip().startswith('|'):
        continue
    cells = [c.strip() for c in line.strip().strip('|').split('|')]
    if len(cells) != 3 or cells[0].startswith('---'):
        continue
    rule = cells[0].replace('**', '').strip()
    if not re.match(r'^(f\d+_lo\d+|\*\*极差\*\*|极差)', cells[0]):
        continue
    def num(cell: str):
        m = re.search(r'(\d+\.\d+)\s*pp', cell)
        return float(m.group(1)) if m else None
    k = re.findall(r'k=(\d+)', cells[1]) + re.findall(r'k=(\d+)', cells[2])
    rows.append({
        'dataset': 'PRONOSTIA',
        'rule': rule,
        'sd_kmax_pp': num(cells[1]),
        'k_max': k[0] if k else 16,
    })
    rows.append({
        'dataset': 'XJTU-SY',
        'rule': rule,
        'sd_kmax_pp': num(cells[2]),
        'k_max': k[-1] if k else '',
    })

out1 = os.path.join(EXP, 'EXP-V2-04-boundary-sweep.csv')
with io.open(out1, 'w', encoding='utf-8', newline='') as fh:
    writer = csv.DictWriter(fh, fieldnames=['dataset', 'rule', 'sd_kmax_pp', 'k_max'])
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
print(f'wrote {os.path.basename(out1)}: {len(rows)} rows')

# ---------------------------------------------------------------- product 2
with io.open(os.path.join(EXP, 'EXP-V1-10-replicates.csv'), 'r', encoding='utf-8-sig',
             newline='') as fh:
    reps = list(csv.DictReader(fh))

groups = {}
for r in reps:
    groups.setdefault((r['design'], r['method']), []).append(r)

out2 = os.path.join(EXP, 'EXP-V1-10-arm-extras.csv')
with io.open(out2, 'w', encoding='utf-8', newline='') as fh:
    writer = csv.writer(fh)
    writer.writerow(['design', 'method', 'n_rows', 'zero_min_share', 'tie_share',
                     'distinct_replicate_ids', 'note'])
    for (design, method), rs in sorted(groups.items()):
        n = len(rs)
        zero = sum(1 for r in rs if float(r['val_fp']) == 0.0) / n
        tie = sum(1 for r in rs if int(r['n_tied_at_min']) >= 2) / n
        ids = len({r['replicate'] for r in rs})
        writer.writerow([design, method, n, round(zero, 3), round(tie, 3), ids,
                         'pooled over all rows of this design/method; the archived per-replicate '
                         'file carries no arm label, so the R=50 and R=200 design-A arms cannot be '
                         'separated ({} distinct replicate ids for {} rows)'.format(ids, n)])
print(f'wrote {os.path.basename(out2)}: {len(groups)} groups')

# ---------------------------------------------------------------- feasibility probe
print('\n--- EXP-V2-03 re-run feasibility ---')
for probe in (r'E:\\MotorHealthMonitorData',
              r'<WORKDIR>\Documents\Codex\2026-09-06\github\motor-health-monitor\data\raw'):
    print(f'data root {probe}: {"present" if os.path.isdir(probe) else "missing"}')
for name in ('EXP-V2-03-run.log', 'EXP-V2-03-bearing-level-holdout.md'):
    path = os.path.join(EXP, name)
    if os.path.isfile(path):
        with io.open(path, 'r', encoding='utf-8', errors='replace') as fh:
            txt = fh.read()
        times = re.findall(r'([\d.]+)\s*(s|sec|seconds|分钟|min)', txt)
        print(f'{name}: {len(txt)} chars, timing hints: {times[:6]}')
