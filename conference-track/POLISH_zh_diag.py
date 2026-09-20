#!/usr/bin/env python3
"""Print exact characters around the anchors whose edits did not apply."""

from __future__ import annotations

import io
import os

ZH = os.path.join(
    r'C:\Users\32597\Documents\Codex\2026-09-15\github\motor-health-monitor-papers',
    'conference-track', 'PAPER_v1.0_中文版.md',
)

ANCHORS = ['2003.10.22', '0.86、0.52', '单次评估分辨率', '恰为 100%', '以该数据集为准',
           '检测器最准', '饱和规则', '前瞻性的自采研究', '干净的边界效应']

with io.open(ZH, 'r', encoding='utf-8', newline='') as fh:
    text = fh.read()

for anchor in ANCHORS:
    idx = text.find(anchor)
    print(f'\n=== {anchor} ===')
    if idx < 0:
        print('  NOT FOUND')
        continue
    start = max(0, idx - 90)
    end = min(len(text), idx + 130)
    print(repr(text[start:end]))
