#!/usr/bin/env python3
"""Remove the two stale sentences that still described EXP-V2-03 as unverified, then typeset v8."""

from __future__ import annotations

import io
import os
import re

TRACK = r'C:\Users\32597\Documents\Codex\2026-09-15\github\motor-health-monitor-papers\conference-track'
EN = os.path.join(TRACK, 'PAPER_v1.0_submission-draft.md')
ZH = os.path.join(TRACK, 'PAPER_v1.0_中文版.md')


def read(p):
    with io.open(p, 'r', encoding='utf-8', newline='') as fh:
        return fh.read()


def write(p, t):
    with io.open(p, 'w', encoding='utf-8', newline='') as fh:
        fh.write(t)


en = read(EN)
print('EN lines mentioning EXP-V2-03:')
for line in en.split('\n'):
    if 'EXP-V2-03' in line:
        print('   ', line.strip()[:120])

pattern_en = re.compile(r'The experiment carrying §3\.1 \(EXP-V2-03\)[^.]*\.', re.DOTALL)
text_en_new = ('The experiment carrying §3.1 (EXP-V2-03) has since been re-run and reproduced '
               'byte-for-byte on all scientific columns (`experiments/EXP-V2-03-hashes.txt`).')
en2, n_en = pattern_en.subn(text_en_new, en, count=1)
print(f'EN stale sentence replaced: {n_en}')
if n_en:
    write(EN, en2)

zh = read(ZH)
pattern_zh = re.compile(r'承载 §3\.1 的实验（EXP-V2-03）[^。]*。')
text_zh_new = ('承载 §3.1 的实验（EXP-V2-03）已于 2026-09-21 重跑，在所有科学列上逐字节复现'
               '（`experiments/EXP-V2-03-hashes.txt`）。')
zh2, n_zh = pattern_zh.subn(text_zh_new, zh, count=1)
print(f'ZH stale sentence replaced: {n_zh}')
if n_zh:
    write(ZH, zh2)

# ----------------------------------------------------------------- typeset v8
V7 = os.path.join(TRACK, 'tools', 'build_isdmd_v7.py')
with io.open(V7, 'r', encoding='utf-8') as fh:
    src = fh.read()
src = src.replace('PAPER_v1.0_ISDMD_v7.docx', 'PAPER_v1.0_ISDMD_v8.docx')
exec(compile(src, 'build_isdmd_v8', 'exec'))
