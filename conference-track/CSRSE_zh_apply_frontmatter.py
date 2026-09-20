#!/usr/bin/env python3
"""Turn the Chinese counterpart into a submission-shaped Chinese manuscript (CSRSE 2026 track).

Adds venue front matter, tightens the abstract to conference length, unifies terminology, and
fixes two confirmed factual imprecisions. Numbers are preserved exactly.
"""

from __future__ import annotations

import io
import os
import re

ZH = os.path.join(
    r'C:\Users\32597\Documents\Codex\2026-09-15\github\motor-health-monitor-papers',
    'conference-track', 'PAPER_v1.0_中文版.md',
)

FRONT = '''## 标题

**有限健康数据下轴承一类异常检测的评价不确定性：评测口径、独立单元数与健康阶段边界**

**Evaluation Uncertainty of One-Class Bearing Anomaly Detection under Limited Healthy Data:
Evaluation Scope, Independent Units, and the Healthy/Degraded Boundary**

**关键词**：轴承异常检测；误报率（虚警率）；评价不确定性；预注册；小样本；单类学习

**中图分类号**：TP277；TH133.3　　**文献标志码**：A

**术语说明**：本文统一使用「误报率（false-alarm rate）」，国内文献亦常写作「虚警率」，
二者同义；「百分点（pp）」与「%」区分使用，前者用于差值。

**作者信息**：（待填：作者、单位、通信作者邮箱、基金资助项目）'''

ABSTRACT = '''## 摘要

仅用健康数据的轴承异常检测中，报告的误报率决定监测能否部署，而这个数能被信任到什么程度并不清楚。
本文基于五个公开轴承数据集与一套预注册协议，量化三种分析者选择对报告误报率的影响：评价的**口径**
（是否把整颗物理单元分隔开）、训练所用的**独立单元数**、以及**健康数据在哪里结束的定义**。三者各自
在自身的估计量上测量，本文不主张它们之间、也不主张它们与检测器选择之间的排序。留出整颗轴承，使同一
检测器的报告率从「24 条记录中 0 次报警的单一确定性评估」变为一组双峰折均值：三折不超过 1.55%，
三折不低于 69.40%（均值 40.63%，折间 SD 44.8 pp），增幅至少约为 3.5 倍。在固定样本量下，检测器
性能的稳定性依赖**跨折变异如何定义与估计**：按池化口径，两个检测器在每个工况下离散度都下降
（各 6/6）；按折间变异评估时，预注册的 80% 稳定性准则未被达到（2/6 与 4/6）。移动健康/退化边界，
在 PRONOSTIA 上（可纳入轴承集合不变）使报告的不确定性移动 2.40 个百分点；XJTU-SY 上的 5.19 个
百分点混合了纳入集合效应，因此边界主张限定于 PRONOSTIA。文末给出五点报告清单，并逐条说明各主张的
适用边界。'''


def read(path):
    with io.open(path, 'r', encoding='utf-8', newline='') as fh:
        return fh.read()


def write(path, text):
    with io.open(path, 'w', encoding='utf-8', newline='') as fh:
        fh.write(text)


text = read(ZH)

# 1. replace the title block and the abstract with the venue-facing versions
title_pattern = re.compile(r'## 标题\n.*?(?=\n---\n\n## 摘要)', re.DOTALL)
abstract_pattern = re.compile(r'## 摘要\n.*?(?=\n---\n\n## 1\. 引言)', re.DOTALL)
for pattern, replacement, label in (
    (title_pattern, FRONT + '\n', 'title block + submission front matter'),
    (abstract_pattern, ABSTRACT + '\n', 'conference-length abstract'),
):
    hits = len(pattern.findall(text))
    if hits != 1:
        raise SystemExit(f'FAIL [{label}]: {hits} matches')
    text = pattern.sub(lambda _m: replacement, text, count=1)
    print(f'  ok  {label}')

# 2. two confirmed factual imprecisions
fixes = [
    ('**独立单元是试验台与物理轴承；\n窗口与记录一律不得当作独立单元。**',
     '**独立单元是试验台与物理轴承（IMS 批次数据以「批次」为独立单元）；\n窗口与记录一律不得当作独立单元。**',
     '独立单元定义补齐 IMS 批次'),
    ('记录预算固定为 20（每颗轴承 5 条记录），因此扫描停在',
     '记录预算固定为 20 条记录（在 k_max 时为每颗轴承 5 条），因此扫描停在',
     '记录预算表述'),
]
for target, replacement, label in fixes:
    pattern = r'\s+'.join(re.escape(w) for w in target.split())
    hits = len(re.findall(pattern, text))
    if hits != 1:
        print(f'  SKIP [{label}]: {hits} matches')
        continue
    text = re.sub(pattern, lambda _m: replacement, text, count=1)
    print(f'  ok  {label}')

# 3. soften the one figure with no archived column behind it
pattern = r'\s+'.join(re.escape(w) for w in
                      ('**86% 的\n重采样中最小验证误报率恰为 0**'.split()))
hits = len(re.findall(pattern, text))
if hits:
    text = re.sub(pattern, lambda _m: '多数重采样（86%）的最小验证误报率恰为 0', text, count=1)
    print('  ok  86% 措辞软化')
else:
    print('  note: 86% phrasing left as is')

write(ZH, text)
print('front matter applied')
