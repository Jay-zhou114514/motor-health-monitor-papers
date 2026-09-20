#!/usr/bin/env python3
"""Record the venue decision (CSRSE 2026, Chinese track) and the schedule."""

from __future__ import annotations

import io
import os
import re

STATUS = os.path.join(
    r'C:\Users\32597\Documents\Codex\2026-09-15\github\motor-health-monitor-papers',
    'conference-track', 'STATUS.md',
)
BRIEF = os.path.join(
    r'C:\Users\32597\Documents\Codex\2026-09-06\github\motor-health-monitor',
    'docs', 'plans', 'NEXT_SESSION_BRIEF.md',
)

ADD = '''

---

## 2026-09-20 更新（第六次）：投稿目标定为 CSRSE 2026（中文轨）

**决定（用户，2026-09-20）**：走**中文稿**，目标会议为 **CSRSE 2026（第六届复杂系统可靠性科学与工程
国际会议，杭州，2026-12-12~13）**，投稿截止 **11-10**、录用 11-25、终稿 12-2；该会明确征集中文与
英文原创论文。备选 ISDMD 2026（温州，11-20~22，JPCS/EI）需先确认投稿系统是否仍开放；
AIIE 2026 已放弃（截止已过/时间过紧）。

**已完成的投稿形态改造**（脚本 `CSRSE_zh_apply_frontmatter.py`）：

- 中文新标题《有限健康数据下轴承一类异常检测的评价不确定性：评测口径、独立单元数与健康阶段边界》
  ＋对应英文标题；
- 摘要重写为中文会议长度（约 330 字），保留全部关键数字；
- 补投稿要素：关键词 6 个、中图分类号（TP277；TH133.3）、文献标志码、术语说明（误报率＝虚警率、
  pp 与 % 区分）、作者/单位/基金**占位待填**；
- 修两处事实性瑕疵：独立单元定义补「IMS 批次以批次为独立单元」；记录预算改为「20 条记录（k_max 时
  每颗轴承 5 条）」；
- 无归档列支撑的 86% 改为「多数重采样（86%）」的软措辞。

**数字守卫**：中英数字集合仅新增中图分类号（TH133.3、TP277）带来的两个记号，稿件数值未变。

**到 11-10 的排期**（详见会话记录）：W1 补归档产物与投稿要素；W2 补置信区间/置换检验并修英文残句；
W3 按新标题重写框架＋补图；W4 补中文文献、两版对齐；W5 模拟审稿＋Layer 2 润色；W6 排版与缓冲。

**待用户确认**：作者/单位/基金信息；CSRSE 论文集收录情况（EI/Scopus）与页数上限；
ISDMD 是否仍开放（若开放需二选一，禁止一稿两投）。
'''

with io.open(STATUS, 'r', encoding='utf-8', newline='') as fh:
    status = fh.read()
if '投稿目标定为 CSRSE 2026' in status:
    print('  skip STATUS')
else:
    with io.open(STATUS, 'w', encoding='utf-8', newline='') as fh:
        fh.write(status.rstrip('\n') + '\n' + ADD)
    print('  ok  STATUS.md')

with io.open(BRIEF, 'r', encoding='utf-8', newline='') as fh:
    brief = fh.read()

pattern = r'4\. \*\*投稿会议决定\*\*.*?(?=5\. \*\*待办\*\*|## 5\.)'
hits = len(re.findall(pattern, brief, re.DOTALL))
if hits != 1:
    raise SystemExit(f'FAIL: venue item matched {hits} times')

ITEM = '''4. **投稿会议已定：CSRSE 2026（中文轨）** —— 杭州 2026-12-12~13，投稿截止 **11-10**，
   录用 11-25，终稿 12-2；中英文均可。备选 ISDMD 2026（温州，11-20~22，JPCS/EI）需先确认系统是否
   仍开放；AIIE 2026 放弃。**中文投稿版**已具备会议形态：新标题、约 330 字中文摘要、关键词、
   中图分类号、术语说明（误报率＝虚警率）、作者/基金占位；稿件文件为 `PAPER_v1.0_中文版.md`。
   待用户提供作者/单位/基金，并确认会议页数与收录信息。**禁止一稿两投。**

'''
brief = re.sub(pattern, lambda _m: ITEM, brief, count=1, flags=re.DOTALL)
with io.open(BRIEF, 'w', encoding='utf-8', newline='') as fh:
    fh.write(brief)
print('  ok  brief venue item')
