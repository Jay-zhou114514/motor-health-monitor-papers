#!/usr/bin/env python3
"""Statistical upgrade for the three main results: bootstrap 95% CIs and permutation tests.

Deterministic (fixed seed 20260921). Reads only archived products; writes
experiments/EXP-STATS-bootstrap-permutation.csv plus a short markdown summary.
"""

from __future__ import annotations

import csv
import io
import os
import statistics as st

import numpy as np

EXP = r'<WORKDIR>\Documents\Codex\2026-09-06\github\motor-health-monitor\experiments'
RNG = np.random.default_rng(20260921)
B = 10000


def load(name, enc='utf-8-sig'):
    with io.open(os.path.join(EXP, name), 'r', encoding=enc, newline='') as fh:
        return list(csv.DictReader(fh))


def boot_ci(values, stat=np.mean, level=95):
    values = np.asarray(values, dtype=float)
    if len(values) < 2:
        return float('nan'), float('nan')
    idx = RNG.integers(0, len(values), size=(B, len(values)))
    stats = stat(values[idx], axis=1)
    lo, hi = np.percentile(stats, [(100 - level) / 2, 100 - (100 - level) / 2])
    return float(lo), float(hi)


def perm_test(a, b, stat=lambda x: np.std(x, ddof=1)):
    a, b = np.asarray(a, float), np.asarray(b, float)
    obs = abs(stat(a) - stat(b))
    pool = np.concatenate([a, b])
    na = len(a)
    count = 0
    for _ in range(B):
        RNG.shuffle(pool)
        if abs(stat(pool[:na]) - stat(pool[na:])) >= obs:
            count += 1
    return obs, (count + 1) / (B + 1)


rows = []

# ---------------------------------------------------------------- 3.1 scope
summ = load('EXP-V2-03-summary.csv')
holdout = [float(r['mean_fp']) * 100 for r in summ
           if r['regime'] == 'R2_bearing_holdout' and r['arm'] == 'S2_new_records'
           and float(r['n_train']) == 96]
lo, hi = boot_ci(holdout)
rows.append(dict(analysis='3.1 holdout fold means', dataset='Paderborn', detector='iForest',
                 n=len(holdout), observed=round(st.mean(holdout), 2),
                 ci_low=round(lo, 2), ci_high=round(hi, 2), p_value='',
                 note=f'mean of six fold means (median {round(st.median(holdout), 2)}); '
                      f'values {[round(v, 2) for v in sorted(holdout)]}'))

# ---------------------------------------------------------------- 3.2 units
def fold_means(rows, detector, dataset, condition, k, key='test_fp'):
    cells = {}
    for r in rows:
        if r.get('detector', 'Isolation Forest') != detector:
            continue
        if r['dataset'] != dataset or r['condition'] != condition:
            continue
        if int(r['k_bearings']) != k:
            continue
        cells.setdefault(r['held_out'], []).append(float(r[key]))
    return [float(np.mean(v)) for v in cells.values()]


for name, detectors in (('EXP-V2-05-raw.csv', ['Isolation Forest']),
                        ('EXP-V2-06-raw.csv', ['A_rms_3sigma', 'B_mahalanobis'])):
    raw = load(name)
    cells = sorted({(r['dataset'], r['condition']) for r in raw})
    for det in detectors:
        k1_all, kmax_all, ratios = [], [], []
        for dataset, condition in cells:
            ks = sorted({int(r['k_bearings']) for r in raw
                         if r['dataset'] == dataset and r['condition'] == condition
                         and r.get('detector', 'Isolation Forest') == det})
            if not ks:
                continue
            a = fold_means(raw, det, dataset, condition, ks[0])
            b = fold_means(raw, det, dataset, condition, ks[-1])
            k1_all += a
            kmax_all += b
            sa, sb = np.std(a, ddof=1), np.std(b, ddof=1)
            if sa > 0:
                ratios.append(sb / sa)
        obs, p = perm_test(k1_all, kmax_all)
        rows.append(dict(analysis='3.2 k=1 vs k_max spread (between-fold)', dataset='both',
                         detector=det, n=f'{len(k1_all)}/{len(kmax_all)}',
                         observed=round(float(obs), 2), ci_low='', ci_high='',
                         p_value=round(p, 4),
                         note=f'permutation test on the SD difference; per-cell ratios '
                              f'{ [round(r,2) for r in ratios] }'))

# ---------------------------------------------------------------- 3.6 components
vd = load('EXP-V1-10-variance-decomposition.csv')
for comp in ('A_fit_composition', 'B_random_seed', 'C_both'):
    vals = [float(r['test_pct_mean']) * 100 for r in vd if r['component'] == comp]
    lo, hi = boot_ci(vals, stat=lambda x, axis: np.std(x, ddof=1, axis=axis))
    rows.append(dict(analysis='3.6 variance component', dataset='IMS 1st_test',
                     detector='iForest', n=len(vals),
                     observed=round(st.stdev(vals), 2),
                     ci_low=round(lo, 2), ci_high=round(hi, 2), p_value='',
                     note='bootstrap CI of the SD of the reported rate'))

out = os.path.join(EXP, 'EXP-STATS-bootstrap-permutation.csv')
with io.open(out, 'w', encoding='utf-8', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=['analysis', 'dataset', 'detector', 'n', 'observed',
                                       'ci_low', 'ci_high', 'p_value', 'note'])
    w.writeheader()
    w.writerows(rows)
print('wrote', os.path.basename(out), f'({len(rows)} rows)')
for r in rows:
    print(' ', r['analysis'], '|', r['detector'], '| obs', r['observed'],
          '| CI', r['ci_low'], r['ci_high'], '| p', r['p_value'])
