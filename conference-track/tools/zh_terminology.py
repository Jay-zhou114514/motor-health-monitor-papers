#!/usr/bin/env python3
"""Chinese copy: add the terminology note (误报率=虚警率, pp) and the SD-definition note upfront."""

from __future__ import annotations

import io
import os
import re

ZH = os.path.join(
    r'C:\Users\32597\Documents\Codex\2026-09-15\github\motor-health-monitor-papers',
    'conference-track', 'PAPER_v1.0_中文版.md',
)

TERM = ('\n**术语说明**：本文统一使用「误报率」，国内文献亦常写作「虚警率」，二者同义；'
        '「百分点（pp）」用于差值，「%」用于比率本身。变异性有两个口径：汇总 CSV 中跨「折 × 重复」'
        '的**池化 SD**，以及各折均值的**折间 SD**；§3.1 用折间，§3.2 同时报告两种并说明判定依赖哪一种。\n')

with io.open(ZH, 'r', encoding='utf-8', newline='') as fh:
    text = fh.read()

if '术语说明' in text and '虚警率' in text:
    print('skip: terminology note already present')
else:
    anchor = '> **本中文稿的用途**'
    start = text.index(anchor)
    end = text.index('\n', text.index('正文数值与英文稿逐项一致。', start)) + 1
    text = text[:end] + TERM + text[end:]
    with io.open(ZH, 'w', encoding='utf-8', newline='') as fh:
        fh.write(text)
    print('本中文稿：已插入术语说明')

# also make sure the Chinese 纪律 paragraph carries the definition pointer
pattern = r'\s+'.join(re.escape(w) for w in
                      ('探索性检查均已标注。'.split()))
hits = len(re.findall(pattern, text))
print(f'纪律段锚点命中: {hits}')
