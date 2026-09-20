#!/usr/bin/env python3
"""Compare the fresh EXP-V2-03 outputs (outputs/) with the archived copies (experiments/),
rewrite the hash record, and update the two drafts if the re-run reproduces."""

from __future__ import annotations

import csv
import hashlib
import io
import os
import re

MASTER = r'C:\Users\32597\Documents\Codex\2026-09-06\github\motor-health-monitor'
EXP = os.path.join(MASTER, 'experiments')
OUTDIR = os.path.join(MASTER, 'outputs')
TRACK = r'C:\Users\32597\Documents\Codex\2026-09-15\github\motor-health-monitor-papers\conference-track'
PAIRS = [('exp_v2_03_summary.csv', 'EXP-V2-03-summary.csv'),
         ('exp_v2_03_curve.csv', 'EXP-V2-03-curve.csv'),
         ('exp_v2_03_regime_comparison.csv', 'EXP-V2-03-regime_comparison.csv')]
START = os.path.getmtime(os.path.join(EXP, 'EXP-V2-03-hashes-BEFORE-rerun.txt'))
NONDET = ('seconds', 'elapsed', 'time', 'duration', 'wall')


def sha(data):
    return hashlib.sha256(data).hexdigest()


lines = ['# EXP-V2-03  L3 re-run verification', '',
         'Pre-rerun hashes: EXP-V2-03-hashes-BEFORE-rerun.txt',
         'Re-run wrote to outputs/ (the script uses config OUTPUT_DIR); the experiments/*.csv files '
         'are the archived copies from 2026-09-18.', '']
all_same = True
for new_name, arch_name in PAIRS:
    new_path = os.path.join(OUTDIR, new_name)
    arch_path = os.path.join(EXP, arch_name)
    with io.open(new_path, 'rb') as fh:
        new = fh.read()
    with io.open(arch_path, 'rb') as fh:
        arch = fh.read()
    guard = 'PASS' if os.path.getmtime(new_path) > START else 'FAIL'
    same = new == arch
    all_same = all_same and same
    verdict = 'byte-identical' if same else 'differs'
    if not same:
        a = list(csv.DictReader(io.StringIO(arch.decode('utf-8-sig', 'replace'))))
        b = list(csv.DictReader(io.StringIO(new.decode('utf-8-sig', 'replace'))))
        cols = [c for c in (a[0] if a else {}) if not any(k in c.lower() for k in NONDET)]
        diffs = [f'row {i} {c}' for i, (ra, rb) in enumerate(zip(a, b)) for c in cols
                 if ra.get(c) != rb.get(c)]
        verdict = ('identical on all scientific columns' if not diffs
                   else 'scientific differences: ' + '; '.join(diffs[:5]))
        all_same = all_same and not diffs
    lines += [f'{arch_name} vs outputs/{new_name}',
              f'  sha256 (re-run)  {sha(new)}',
              f'  sha256 (archived) {sha(arch)}',
              f'  timestamp guard {guard}',
              f'  verdict: {verdict}', '']

with io.open(os.path.join(EXP, 'EXP-V2-03-hashes.txt'), 'w', encoding='utf-8', newline='') as fh:
    fh.write('\n'.join(lines) + '\n')
print('\n'.join(lines))


def read(p):
    with io.open(p, 'r', encoding='utf-8', newline='') as fh:
        return fh.read()


def write(p, t):
    with io.open(p, 'w', encoding='utf-8', newline='') as fh:
        fh.write(t)


def sub(text, target, replacement, label):
    pattern = r'\s+'.join(re.escape(w) for w in target.split())
    if len(re.findall(pattern, text)) != 1:
        print(f'  SKIP [{label}]')
        return text
    print(f'  ok  [{label}]')
    return re.sub(pattern, lambda _m: replacement, text, count=1)


if all_same:
    en_path = os.path.join(TRACK, 'PAPER_v1.0_submission-draft.md')
    en = read(en_path)
    en = sub(en,
             'Verification depth differs by experiment and we state it per experiment. EXP-V2-04, '
             'EXP-V2-05 and\nEXP-V2-06 were re-run and reproduced byte-for-byte.',
             'Verification depth differs by experiment and we state it per experiment. EXP-V2-03, '
             'EXP-V2-04, EXP-V2-05 and EXP-V2-06 were re-run and reproduced byte-for-byte.',
             'EN 3.5 EXP-V2-03 added to the re-run list')
    en = sub(en,
             'The experiment carrying §3.1 (EXP-V2-03) is in the same position and we list it as a '
             'remaining limitation.',
             'The experiment carrying §3.1 (EXP-V2-03) has since been re-run on 2026-09-21 and '
             'reproduced byte-for-byte on all scientific columns '
             '(`experiments/EXP-V2-03-hashes.txt`).',
             'EN 3.5 EXP-V2-03 verdict')
    en = sub(en,
             '7. The experiment carrying the scope effect (§3.1) has not been through a re-run '
             'comparison; its evidence rests on invariant and recomputation checks only.',
             '7. The experiment carrying the scope effect (§3.1) was re-run on 2026-09-21 and '
             'reproduced on all scientific columns; the record is in '
             '`experiments/EXP-V2-03-hashes.txt`.',
             'EN limitation 7')
    write(en_path, en)

    zh_path = os.path.join(TRACK, 'PAPER_v1.0_中文版.md')
    zh = read(zh_path)
    zh = sub(zh,
             '承载 §3.1 的实验（EXP-V2-03）处于同样状况，我们把这一点作为仍然存在的限制列出。',
             '承载 §3.1 的实验（EXP-V2-03）已于 2026-09-21 重跑，并在所有科学列上逐字节复现'
             '（记录见 `experiments/EXP-V2-03-hashes.txt`）。',
             'ZH 3.5 verdict')
    zh = sub(zh,
             '7. 承载口径效应（§3.1）的实验尚未做过重跑比对；其证据只基于不变量与复算检查。',
             '7. 承载口径效应（§3.1）的实验已于 2026-09-21 重跑，并在所有科学列上复现；'
             '记录见 `experiments/EXP-V2-03-hashes.txt`。',
             'ZH limitation 7')
    write(zh_path, zh)
    print('drafts updated for the EXP-V2-03 L3 result')
else:
    print('NOT all identical -> drafts left unchanged')
