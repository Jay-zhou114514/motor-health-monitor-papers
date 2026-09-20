#!/usr/bin/env python3
"""Record the Layer-2 tightening and Layer-1 scan (fixed quoting)."""

from __future__ import annotations

import io
import os
import re

PAPERS = r"C:\Users\32597\Documents\Codex\2026-09-15\github\motor-health-monitor-papers"
MASTER = r"C:\Users\32597\Documents\Codex\2026-09-06\github\motor-health-monitor"
STATUS = os.path.join(PAPERS, "conference-track", "STATUS.md")
BRIEF = os.path.join(MASTER, "docs", "plans", "NEXT_SESSION_BRIEF.md")


def read(path):
    with io.open(path, "r", encoding="utf-8", newline="") as fh:
        return fh.read()


def write(path, text):
    with io.open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


def sub_once(text, pattern, replacement, label, flags=0):
    hits = len(re.findall(pattern, text, flags))
    if hits != 1:
        raise SystemExit(f"FAIL [{label}]: expected 1 match, found {hits}")
    print(f"  ok  {label}")
    return re.sub(pattern, lambda _m: replacement, text, count=1, flags=flags)


STATUS_ADD = """

---

## 2026-09-20 更新（第三次）：第二层主张按作者裁决收紧；Layer 1 扫描完成（未改正文）

**第二层（单元数）主张已收紧并落到四处**（Abstract / §3.2 / §7 / Fig.1 图注）以及
`CLAIM_EVIDENCE_MAP.md` 的 C9 与「禁止表述」表：

> 在有限健康数据下，检测器性能的稳定性依赖于**如何定义与估计跨折变异**；
> **按折间变异评估时，预注册的 80% 稳定性标准未被达到**（iForest 2/6、3σ RMS 4/6）。
> 池化口径下的 6/6 降级为 sensitivity，不再作为结果陈述。

**Layer 1（humanizer / humanizer-zh）扫描完成，只出清单、未改任何正文**：
`POLISH_L1_humanizer_scan.md`（脚本与原始输出 `POLISH_L1_scan.py/.txt`）。
结论：词汇层干净（AI 高频词 2 处、连接词只有 therefore 13 处）；问题集中在
§3.6 四段同构的粗体开场、元话语密度、rather than 句式、27 句超长句，
以及 false-alarm/false-positive、recording(s)/record(s)、healthy-phase rule/boundary 三组术语混用。

**扫描同时发现一条 claim 缺陷（需在 Layer 2 前修）**：L293（§5.1）与 L404（§7）
仍写「the defensible ratio is about 3.5-fold rather than an order of magnitude」——
第 3 轮 RB-M2 要求删除的「下界当上界」残句，上一轮只清了 §5.5。

**Layer 2（人工学术润色）待 venue 确定后执行**，需要 page limit / paper type /
abstract length / section structure / reference style 五项参数。
"""

status = read(STATUS)
if "第二层主张按作者裁决收紧" not in status:
    write(STATUS, status.rstrip("\n") + "\n" + STATUS_ADD)
    print("  ok  STATUS.md")
else:
    print("  skip STATUS.md")

brief = read(BRIEF)

RULE_ADD = """   - RC-M3 / RC-M4 与 §5.5 残句已按最小改法修正。
   - **作者已裁决第二层（单元数）主张的收紧**：改为「稳定性依赖于如何定义与估计跨折变异；
     按折间变异评估时预注册的 80% 稳定性标准未达到」（iForest 2/6、3σ RMS 4/6；池化口径的
     6/6 降为 sensitivity）。已落到 Abstract / §3.2 / §7 / Fig.1 图注与 CLAIM_EVIDENCE_MAP 的 C9。
"""

brief = sub_once(
    brief,
    r"   - RC-M3 / RC-M4 与 §5\.5 残句已按最小改法修正。",
    RULE_ADD.rstrip("\n"),
    "brief item 1 layer-2 tightening",
)

ITEM3 = """3. **语言润色分两层执行（2026-09-20 定）**：
   - **Layer 1 已完成**：`humanizer` / `humanizer-zh` 扫描，**只出清单、不改正文** →
     `conference-track/POLISH_L1_humanizer_scan.md`（脚本 `POLISH_L1_scan.py`、原始输出 `.txt`）。
     结论：词汇层干净；问题集中在 §3.6 四段同构开场、元话语密度、27 句超长句、
     三组术语混用（false-alarm/false-positive、recording(s)/record(s)、healthy-phase rule/boundary）。
   - **待修（不等 venue）**：L293（§5.1）与 L404（§7）的
     `3.5-fold rather than an order of magnitude` —— RB-M2 要求删除的「下界当上界」残句。
   - **Layer 2 待 venue 确定后执行**，需要 page limit / paper type / abstract length /
     section structure / reference style 五项。注意：brief 原引用的 `nature-polishing` skill
     在本机不存在。
"""

brief = sub_once(
    brief,
    r"3\. \*\*语言润色\*\*.*?(?=4\. \*\*投稿会议决定\*\*)",
    ITEM3,
    "brief item 3 polish layers",
    flags=re.DOTALL,
)

write(BRIEF, brief)
print("recorded")
