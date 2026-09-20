#!/usr/bin/env python3
"""Fix the new CSV, add its provenance note, and propagate the two corrected facts to the paper."""

from __future__ import annotations

import csv
import io
import os
import re

EXP = r'C:\Users\32597\Documents\Codex\2026-09-06\github\motor-health-monitor\experiments'
TRACK = r'C:\Users\32597\Documents\Codex\2026-09-15\github\motor-health-monitor-papers\conference-track'
EN = os.path.join(TRACK, 'PAPER_v1.0_submission-draft.md')
ZH = os.path.join(TRACK, 'PAPER_v1.0_中文版.md')

# --- 1. fix the k_max column: on PRONOSTIA the admissible set is unchanged, so k_max = 16
path = os.path.join(EXP, 'EXP-V2-04-boundary-sweep.csv')
with io.open(path, 'r', encoding='utf-8', newline='') as fh:
    rows = list(csv.DictReader(fh))
for r in rows:
    if r['dataset'] == 'PRONOSTIA':
        r['k_max'] = '16'
    r['rule'] = r['rule'].replace('（主）', ' (main)')
with io.open(path, 'w', encoding='utf-8', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=['dataset', 'rule', 'sd_kmax_pp', 'k_max'])
    w.writeheader()
    w.writerows(rows)
print('fixed', os.path.basename(path))

note = '''# EXP-V2-04 boundary sweep (derived product)

`EXP-V2-04-boundary-sweep.csv` is **derived**, not recomputed: the five healthy-phase rules and
their per-rule SD(k_max) are transcribed by script from the table in
`EXP-V2-04-xjtu-pronostia.md` Section 3, which is the only archived product that carries the rule
labels. The archived CSVs (`EXP-V2-04-summary.csv`, `-main_raw.csv`, `-sensitivity_raw.csv`) do not
have a rule column, so a reader cannot recompute these values from them.

Consequences for the paper: Section 3.3's 2.40 pp (PRONOSTIA) and 5.19 pp (XJTU-SY) should be cited
as deriving from this table; a future re-run should write the rule label into the summary CSV so
that the sweep becomes recomputable end to end.
'''
with io.open(os.path.join(EXP, 'EXP-V2-04-boundary-sweep.md'), 'w', encoding='utf-8',
             newline='') as fh:
    fh.write(note)
print('wrote EXP-V2-04-boundary-sweep.md')


def read(p):
    with io.open(p, 'r', encoding='utf-8', newline='') as fh:
        return fh.read()


def write(p, t):
    with io.open(p, 'w', encoding='utf-8', newline='') as fh:
        fh.write(t)


def sub(text, target, replacement, label, required=True):
    pattern = r'\s+'.join(re.escape(w) for w in target.split())
    hits = len(re.findall(pattern, text))
    if hits != 1:
        if required:
            raise SystemExit(f'FAIL [{label}]: {hits} matches')
        print(f'  skip [{label}] ({hits})')
        return text
    print(f'  ok  [{label}]')
    return re.sub(pattern, lambda _m: replacement, text, count=1)


en = read(EN)
en = sub(en,
         'the minimum validation false-alarm rate was exactly zero in 86% of resamples and at '
         'least two candidate configurations tied at that minimum in 92%.',
         'the minimum validation false-alarm rate was exactly zero in 84% of the archived design-A '
         'Isolation Forest replicates, and at least two candidate configurations tied at that '
         'minimum in 92% (`experiments/EXP-V1-10-arm-extras.csv`; the per-replicate file carries '
         'no arm label, so the R = 50 and R = 200 arms are pooled).',
         'EN 86% -> 84%')
en = sub(en, 'yields mean false-positive rates of 16.9–57.6% for',
         'yields mean false-alarm rates of 16.9–57.6% for',
         'EN caption terminology')
en = sub(en,
         'The project\'s protocol grades evidence A–D;',
         'Two variability definitions appear below and are kept apart throughout: the pooled SD over '
         'all fold × repeat evaluations stored in the summary CSVs, and the between-fold SD of '
         'per-fold mean rates. Section 3.1 uses the between-fold definition; Section 3.2 reports '
         'both and says which verdict depends on which. The project\'s protocol grades evidence A–D;',
         'EN SD definitions upfront')
write(EN, en)

zh = read(ZH)
zh = sub(zh, '多数重采样（86%）的最小验证误报率恰为 0',
         '归档的设计 A 森林复制中，最小验证误报率恰为 0 的占 84%（池化统计，见 '
         '`experiments/EXP-V1-10-arm-extras.csv`）',
         'ZH 86% -> 84%')
zh = sub(zh, '**术语说明**', '**术语说明**', 'ZH check term note', required=False)
write(ZH, zh)
print('paper updated')
