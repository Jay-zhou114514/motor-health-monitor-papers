#!/usr/bin/env python3
"""Pivot: the English draft is the submission; the Chinese file is a comprehension copy."""

from __future__ import annotations

import io
import os
import re

ZH = os.path.join(
    r'<WORKDIR>\Documents\Codex\2026-09-15\github\motor-health-monitor-papers',
    'conference-track', 'PAPER_v1.0_中文版.md',
)
STATUS = os.path.join(
    r'<WORKDIR>\Documents\Codex\2026-09-15\github\motor-health-monitor-papers',
    'conference-track', 'STATUS.md',
)
BRIEF = os.path.join(
    r'<WORKDIR>\Documents\Codex\2026-09-06\github\motor-health-monitor',
    'docs', 'plans', 'NEXT_SESSION_BRIEF.md',
)

NEW_FRONT = '''## 标题

**仅用健康数据的轴承异常检测中评价不确定性的三个侧面**

**Three Faces of Evaluation Uncertainty in Healthy-Data-Only Bearing Anomaly Detection**

> **本中文稿的用途**：供作者理解英文投稿稿（`PAPER_v1.0_submission-draft.md`）之用，
> **不作为投稿版本**；投稿走**英文稿**。术语上「误报率」与国内常用的「虚警率」同义，
> 「pp」表示百分点；正文数值与英文稿逐项一致。
'''


def read(path):
    with io.open(path, 'r', encoding='utf-8', newline='') as fh:
        return fh.read()


def write(path, text):
    with io.open(path, 'w', encoding='utf-8', newline='') as fh:
        fh.write(text)


text = read(ZH)
pattern = re.compile(r'## 标题\n.*?\*\*作者信息\*\*[^\n]*', re.DOTALL)
hits = len(pattern.findall(text))
if hits != 1:
    raise SystemExit(f'FAIL: front-matter block matched {hits} times')
text = pattern.sub(lambda _m: NEW_FRONT.rstrip('\n'), text, count=1)
write(ZH, text)
print('  ok  Chinese front matter returned to a comprehension-copy header')

ADD = '''

---

## 2026-09-20 更新（第六次）：投稿语言定为**英文稿**；中文稿降为自用理解稿

- **用户决定（2026-09-20）**：投稿走**英文稿** `PAPER_v1.0_submission-draft.md`；
  `PAPER_v1.0_中文版.md` 仅作作者阅读理解用，**不作为投稿版本**。
  此前一度决定走 CSRSE 中文轨，随后改回英文稿，故原计划中的中文投稿要素
  （会议标题、中文摘要定稿、关键词、中图分类号、作者占位）已从中文稿撤下。
- **中文稿保留的改动**：一次 humanizer-zh 去 AI 化（破折号 10→0、排比改直陈、删元话语、
  `因此` 减量、长句拆分），以及保持与英文稿逐项一致的数字。
- **英文稿当前状态**：投稿骨架完整（Abstract / Protocol / Results 3.1–3.6 / Related Work /
  Discussion 5.1–5.5 / Limitations 10 条 / 数据与代码可用性 / Conclusion / Fig.1 图注）。
  **投稿前必须处理**：① §5.1 与 §7 的 "rather than an order of magnitude" 残句（RB-M2）；
  ② 补两处归档产物（五条健康阶段规则的带标签 CSV；EXP-V1-10 的 zero-minimum 列与 arm 列）；
  ③ 关键比较补置信区间或置换检验；④ 按目标会议模板排版并核对页数（JPCS 类 6–8 页单栏）。
- **会议待定**：英文轨候选 ISDMD 2026（温州，11-20~22，JPCS/EI；官网 9-6 与平台 11-6 日期冲突，
  需进系统确认）与 CSRSE 2026（杭州，12-12~13，11-10 截止，接受英文）。
  **同一篇只能投一个，禁止一稿两投。**
'''

status = read(STATUS)
if '投稿语言定为**英文稿**' in status:
    print('  skip STATUS')
else:
    write(STATUS, status.rstrip('\n') + '\n' + ADD)
    print('  ok  STATUS.md')

brief = read(BRIEF)
pattern = r'4\. \*\*投稿会议决定\*\*.*?(?=5\. \*\*待办\*\*|## 5\.)'
hits = len(re.findall(pattern, brief, re.DOTALL))
if hits != 1:
    raise SystemExit(f'FAIL: venue item matched {hits} times')
ITEM = '''4. **投稿语言：英文稿**（2026-09-20 用户决定）；`PAPER_v1.0_中文版.md` 降为**自用理解稿**，
   不投稿。会议待定：ISDMD 2026（温州 11-20~22，JPCS/EI，日期信息冲突需确认）为首选匹配，
   CSRSE 2026（杭州 12-12~13，11-10 截止，接受英文）为稳妥备选；**禁止一稿两投**。
   英文稿投稿前必做：修 §5.1/§7 的 "rather than an order of magnitude" 残句；补两处归档产物；
   关键比较补置信区间或置换检验；按目标会议模板排版核对页数。

'''
brief = re.sub(pattern, lambda _m: ITEM, brief, count=1, flags=re.DOTALL)
write(BRIEF, brief)
print('  ok  brief venue item')
