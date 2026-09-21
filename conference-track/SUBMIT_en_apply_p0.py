#!/usr/bin/env python3
"""P0 fixes for the English submission draft (venue-independent), mirrored into the Chinese copy.

1. §5.1 and §7: the remaining RB-M2 residue that presented a lower bound as an upper bound.
2. §3.2: one conclusion that holds under both SD definitions (k = 1 is unreliable).
3. Limitations 2: state the binding constraint as the count of available independent units.
"""

from __future__ import annotations

import io
import os
import re

TRACK = r'<WORKDIR>\Documents\Codex\2026-09-15\github\motor-health-monitor-papers\conference-track'
EN = os.path.join(TRACK, 'PAPER_v1.0_submission-draft.md')
ZH = os.path.join(TRACK, 'PAPER_v1.0_中文版.md')

EN_EDITS = [
    ('Because the within-bearing figure is a single deterministic evaluation with a resolution of '
     '4.17 percentage points, the defensible ratio is about 3.5-fold rather than an order of '
     'magnitude (§3.1).',
     'Because the within-bearing figure is a single deterministic evaluation with a resolution of '
     '4.17 percentage points, the increase is at least about 3.5-fold; zero alarms in 24 recordings '
     'does not bound it from above (§3.1).',
     '§5.1 lower bound restored'),

    ('because the within-bearing figure is a single deterministic evaluation with '
     '4.17-percentage-point resolution, the defensible ratio is about 3.5-fold rather than an order '
     'of magnitude.',
     'because the within-bearing figure is a single deterministic evaluation with '
     '4.17-percentage-point resolution, the increase is at least about 3.5-fold.',
     '§7 lower bound restored'),

    ('The pooled reading is reported as a sensitivity, not as the result.',
     'The pooled reading is reported as a sensitivity, not as the result. One conclusion survives '
     'both definitions: training on a single bearing is unreliable. At k = 1 the mean false-alarm '
     'rate on a different bearing is 16.9–57.6% for Isolation Forest and 23.7–49.5% for the 3σ RMS '
     'threshold, and those cells carry the largest per-cell spread of the sweep.',
     '§3.2 definition-independent conclusion'),

    ('2. Few independent units: 6 (Paderborn), 15 (XJTU-SY), 17 (PRONOSTIA); the unit effect is '
     'estimated from 3–4 bearings per cell within a condition.',
     '2. The binding constraint is the number of publicly available independent healthy units, not '
     'the volume of healthy data: Paderborn contributes 6 healthy bearings in total and 3–7 per '
     'operating condition after the healthy-phase rule, XJTU-SY 15 and PRONOSTIA 17, so the unit '
     'effect rests on 3–4 bearings per cell. Adding recordings to the same units does not help '
     '(§3.6); adding units would require pooling datasets with different acquisition chains or new '
     'hardware.',
     'Limitations 2 rewritten'),
]

ZH_EDITS = [
    ('池化读数作为敏感性分析报告，\n不作为结果陈述。',
     '池化读数作为敏感性分析报告，\n不作为结果陈述。有一种读法在两种口径下都成立：只用一颗轴承训练不可靠。k=1 时，在不同轴承上的\n平均误报率为 Isolation Forest 16.9–57.6%、3σ RMS 23.7–49.5%，且这两格是整轮扫描中逐格离散度\n最大的情形。',
     '中文：口径无关结论'),

    ('2. 独立单元很少：6（Paderborn）、15（XJTU-SY）、17（PRONOSTIA）；单元效应在每个工况内仅由 3–4 颗\n   轴承估计。',
     '2. 真正的约束是公开可用的独立健康单元数，而不是健康数据量：Paderborn 一共只有 6 颗健康轴承，按\n   健康阶段规则筛选后每个工况剩 3–7 颗；XJTU-SY 15 颗、PRONOSTIA 17 颗，因此单元效应在每个工况内\n   仅由 3–4 颗轴承估计。给同样的单元增加记录不起作用（§3.6）；要增加单元，只能合并采集链路不同的\n   数据集，或使用新硬件。',
     '中文：限制 2 改写'),
]


def read(path):
    with io.open(path, 'r', encoding='utf-8', newline='') as fh:
        return fh.read()


def write(path, text):
    with io.open(path, 'w', encoding='utf-8', newline='') as fh:
        fh.write(text)


for path, edits, label in ((EN, EN_EDITS, 'EN'), (ZH, ZH_EDITS, 'ZH')):
    text = read(path)
    for target, replacement, name in edits:
        pattern = r'\s+'.join(re.escape(w) for w in target.split())
        hits = len(re.findall(pattern, text))
        if hits != 1:
            raise SystemExit(f'FAIL [{label}/{name}]: {hits} matches')
        text = re.sub(pattern, lambda _m: replacement, text, count=1)
        print(f'  ok  [{label}] {name}')
    write(path, text)

print('\nP0 edits applied to both drafts')
