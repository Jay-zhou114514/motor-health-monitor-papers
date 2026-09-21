#!/usr/bin/env python3
"""Record the Chinese-variant de-AI pass in STATUS.md."""

from __future__ import annotations

import io
import os

STATUS = os.path.join(
    r'<WORKDIR>\Documents\Codex\2026-09-15\github\motor-health-monitor-papers',
    'conference-track', 'STATUS.md',
)

ADD = '''

---

## 2026-09-20 更新（第五次）：**中文版**执行一次 humanizer-zh 去 AI 化（英文稿未动）

- **对象**：`PAPER_v1.0_中文版.md`。英文稿 `PAPER_v1.0_submission-draft.md` **一字未改**，
  仍是投稿与事实来源。
- **改写前扫描**（`POLISH_L1zh_scan.py/.txt`）：破折号 `——` 10 处、否定式排比 7 处、
  元话语 3 处、`因此` 出现在 26 行、粗体强调 111 次、长句（>60 字）85 条（其中多数其实是表格行）。
- **已应用的改写**（`POLISH_zh_apply_deAI2.py` 15 处 + `POLISH_zh_apply_deAI3.py` 两条类别规则）：
  破折号 **10 → 0**；装饰性加粗 −4（否定词不再加粗）；否定式排比改为直陈（如"这是退化的稳定，
  不能算好结果"）；删去"我们如实说明""我们如实报告为"等元话语；`因此` 减量 6 处；拆分 §3.2 口径段长句。
- **数字守卫**：`POLISH_zh_translation_check.txt` —— 中英两侧数字多重集**仍完全一致**
  （144 个不同数字、434 次出现），改写未触碰任何数值。
- **留给 Layer 2（venue 确定后）**：约 106 处粗体（多数是表格内数值强调，属学术惯例）、
  少量 `因此`、以及按 venue 篇幅要求的整体压缩。
- **说明**：`POLISH_L1_apply_deAI.py` 与 `POLISH_zh_mark_stale.py` 是为"英文稿路径"准备的，
  **从未执行**；因删除被驳回而保留在目录中，仅作记录。
'''

with io.open(STATUS, 'r', encoding='utf-8', newline='') as fh:
    text = fh.read()

if '中文版**执行一次 humanizer-zh 去 AI 化' in text:
    print('skip: already recorded')
else:
    with io.open(STATUS, 'w', encoding='utf-8', newline='') as fh:
        fh.write(text.rstrip('\n') + '\n' + ADD)
    print('STATUS.md updated')
