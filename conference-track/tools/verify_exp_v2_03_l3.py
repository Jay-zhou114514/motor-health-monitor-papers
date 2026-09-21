#!/usr/bin/env python3
"""EXP-V2-03 L3 check: timestamp guard, byte comparison, and column-wise comparison against the
pre-rerun content recovered from git (non-deterministic columns excluded)."""

from __future__ import annotations

import csv
import hashlib
import io
import os
import subprocess

MASTER = r'<WORKDIR>\Documents\Codex\2026-09-06\github\motor-health-monitor'
EXP = os.path.join(MASTER, 'experiments')
START_MARKER = os.path.join(EXP, 'EXP-V2-03-hashes-BEFORE-rerun.txt')
FILES = ['EXP-V2-03-summary.csv', 'EXP-V2-03-curve.csv', 'EXP-V2-03-regime_comparison.csv',
         'EXP-V2-03-per-bearing-rms.csv']
NONDET = ('seconds', 'elapsed', 'time', 'duration', 'wall')

start_time = os.path.getmtime(START_MARKER)
lines_out = ['# EXP-V2-03  L3 re-run verification', '']
lines_out.append(f'guard: output files must be newer than {os.path.basename(START_MARKER)} '
                 f'({START_MARKER}, mtime {start_time:.0f})')
lines_out.append('')

for name in FILES:
    path = os.path.join(EXP, name)
    if not os.path.isfile(path):
        lines_out.append(f'{name}: MISSING')
        continue
    with io.open(path, 'rb') as fh:
        now = fh.read()
    sha = hashlib.sha256(now).hexdigest()
    mtime = os.path.getmtime(path)
    guard = 'PASS' if mtime > start_time else 'FAIL (file not rewritten)'

    old = subprocess.run(['git', '-C', MASTER, 'show', f'HEAD:experiments/{name}'],
                         capture_output=True)
    if old.returncode != 0:
        lines_out.append(f'{name}: no git baseline ({old.stderr.decode()[:60].strip()})')
        continue
    old_bytes = old.stdout
    byte_same = old_bytes == now

    verdict = 'byte-identical' if byte_same else 'differs byte-wise'
    if not byte_same:
        def rows(data):
            text = data.decode('utf-8-sig', 'replace')
            return list(csv.DictReader(io.StringIO(text)))
        a, b = rows(old_bytes), rows(now)
        if a and b and list(a[0]) == list(b[0]):
            cols = [c for c in a[0] if not any(k in c.lower() for k in NONDET)]
            diffs = []
            if len(a) != len(b):
                diffs.append(f'row count {len(a)} -> {len(b)}')
            for i, (ra, rb) in enumerate(zip(a, b)):
                for c in cols:
                    if ra.get(c) != rb.get(c):
                        diffs.append(f'row {i} col {c}: {ra.get(c)} -> {rb.get(c)}')
            verdict = ('identical on all scientific columns'
                       if not diffs else 'scientific differences: ' + '; '.join(diffs[:5]))
        else:
            verdict = 'differs and the header changed'

    lines_out.append(f'{name}')
    lines_out.append(f'  sha256 {sha}')
    lines_out.append(f'  timestamp guard {guard}')
    lines_out.append(f'  vs pre-rerun: {verdict}')
    lines_out.append('')

out = os.path.join(EXP, 'EXP-V2-03-hashes.txt')
with io.open(out, 'w', encoding='utf-8', newline='') as fh:
    fh.write('\n'.join(lines_out) + '\n')
print('\n'.join(lines_out))
print('wrote', os.path.basename(out))
