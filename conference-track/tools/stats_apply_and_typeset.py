#!/usr/bin/env python3
"""Record the statistics, add them to both drafts, and rebuild the submission docx as v5."""

from __future__ import annotations

import io
import os
import re

EXP = r'<WORKDIR>\Documents\Codex\2026-09-06\github\motor-health-monitor\experiments'
TRACK = r'<WORKDIR>\Documents\Codex\2026-09-15\github\motor-health-monitor-papers\conference-track'
EN = os.path.join(TRACK, 'PAPER_v1.0_submission-draft.md')
ZH = os.path.join(TRACK, 'PAPER_v1.0_中文版.md')

NOTE = '''# Bootstrap and permutation statistics (derived product)

`EXP-STATS-bootstrap-permutation.csv` was produced by `conference-track/tools/stats_upgrade.py`
from the archived products below. Fixed seed 20260921; 10,000 bootstrap resamples and 10,000
permutations. Units are fold-level means, i.e. the between-fold definition.

Sources: `EXP-V2-03-summary.csv` (scope, six folds), `EXP-V2-05-raw.csv` and `EXP-V2-06-raw.csv`
(unit effect, fold-level rates per cell), `EXP-V1-10-variance-decomposition.csv` (noise floor).

Headline readings:

* six-fold holdout mean 40.63%, bootstrap 95% interval **12.0 to 72.7 pp** (the interval is wide
  because the fold distribution is bimodal, which is the point of the scope result);
* permutation test on the between-fold spread, k = 1 versus k_max: Isolation Forest p = 0.18,
  3σ RMS p = 0.51 (neither separates), Mahalanobis p < 0.001 in the opposite direction
  (its spread grows, consistent with saturation);
* noise-floor components 5.20 pp [3.60, 6.61], 4.39 pp [3.53, 5.12], 5.18 pp [3.60, 6.58].

Consequence for the text: the second face cannot be stated as a significant unit effect under the
between-fold definition; it is reported as definition-dependent, which is the tightened claim.
'''

with io.open(os.path.join(EXP, 'EXP-STATS-bootstrap-permutation.md'), 'w', encoding='utf-8',
             newline='') as fh:
    fh.write(NOTE)
print('wrote EXP-STATS-bootstrap-permutation.md')


def read(p):
    with io.open(p, 'r', encoding='utf-8', newline='') as fh:
        return fh.read()


def write(p, t):
    with io.open(p, 'w', encoding='utf-8', newline='') as fh:
        fh.write(t)


def sub(text, target, replacement, label):
    pattern = r'\s+'.join(re.escape(w) for w in target.split())
    hits = len(re.findall(pattern, text))
    if hits != 1:
        print(f'  SKIP [{label}] ({hits})')
        return text
    print(f'  ok  [{label}]')
    return re.sub(pattern, lambda _m: replacement, text, count=1)


en = read(EN)
en = sub(en,
         'The holdout arm is replicated over six physical units, and its between-fold spread is '
         'large (SD 44.8 pp).',
         'The holdout arm is replicated over six physical units, and its between-fold spread is '
         'large (SD 44.8 pp). A bootstrap 95% interval for the mean of the six fold rates spans '
         '12.0 to 72.7 percentage points (10,000 resamples over folds, fixed seed; '
         '`experiments/EXP-STATS-bootstrap-permutation.csv`).',
         'EN 3.1 bootstrap CI')
en = sub(en,
         'The pooled reading is reported as a sensitivity, not as the result.',
         'The pooled reading is reported as a sensitivity, not as the result. A permutation test on '
         'the between-fold spread (10,000 permutations over fold-level rates) does not separate '
         'k = 1 from k_max for either non-saturated detector (Isolation Forest p = 0.18, '
         '3σ RMS p = 0.51) and separates the saturated detector in the opposite direction '
         '(p < 0.001); the same file carries these tests.',
         'EN 3.2 permutation test')
write(EN, en)

zh = read(ZH)
zh = sub(zh,
         '留出臂在六个物理单元上重复，其折间离散度很大（SD 44.8 pp）。',
         '留出臂在六个物理单元上重复，其折间离散度很大（SD 44.8 pp）。六个折均值的 bootstrap '
         '95% 区间为 12.0 到 72.7 个百分点（对折做 10,000 次重采样，固定种子；见 '
         '`experiments/EXP-STATS-bootstrap-permutation.csv`）。',
         'ZH 3.1 bootstrap CI')
zh = sub(zh,
         '池化读数作为敏感性分析报告，\n不作为结果陈述。',
         '池化读数作为敏感性分析报告，不作为结果陈述。对折间离散度的置换检验（10,000 次，以折为单位）'
         '在两个未饱和检测器上都无法把 k=1 与 k_max 分开（Isolation Forest p = 0.18、3σ RMS p = 0.51），'
         '而饱和的马氏距离在相反方向上显著（p < 0.001）；这些检验同在该 CSV 中。',
         'ZH 3.2 permutation test')
write(ZH, zh)
print('drafts updated')

# ------------------------------------------------------------------ typeset v5
V4 = os.path.join(TRACK, 'tools', 'build_isdmd_v4.py')
with io.open(V4, 'r', encoding='utf-8') as fh:
    src = fh.read()
src = src.replace('PAPER_v1.0_ISDMD_v4.docx', 'PAPER_v1.0_ISDMD_v5.docx')
exec(compile(src, 'build_isdmd_v5', 'exec'))
