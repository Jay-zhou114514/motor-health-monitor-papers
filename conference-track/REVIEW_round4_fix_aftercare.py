#!/usr/bin/env python3
"""Repair the anti-pattern list: the previous edit lost item 15 and inserted literal escapes."""

from __future__ import annotations

import io
import os

AFTERCARE = os.path.join(
    r"C:\Users\32597\Documents\Codex\2026-09-06\github\motor-health-monitor",
    "docs", "EXPERIMENT_AFTERCARE.md",
)

ITEM_15 = (
    "15. **启动子代理后未收取输出即结束回合 → 报告丢失**（首个 reviewerB 即如此丢失，不可取回）。\n"
    "   **规则：子代理任务必须要求把结果写入仓库文件，并在同一回合确认文件存在。**"
)

ITEM_16 = (
    "16. **子代理任务文本可能根本没送达**（2026-09-20 第 4 轮审稿实测：4 个子代理实例"
    "全部报告\"没有收到任务\"，短 ASCII 探针也未回执；该会话多代理消息通道整体不可用）"
    "→ 报告只能由主代理代写，**独立性未达成**。\n"
    "   **规则：启动子代理后必须先确认它收到了任务**（要求回执一个约定的 token 或一句话摘要）；"
    "收不到就中止这条路线，改由主代理执行，并在产物里**明确声明独立性未达成**，"
    "而不是把自检当作独立审稿。"
)

with io.open(AFTERCARE, "r", encoding="utf-8", newline="") as fh:
    text = fh.read()

marker = "\\1\\n16. "
if marker not in text:
    raise SystemExit("FAIL: mangled marker not found; nothing changed")

head, tail = text.split(marker, 1)
if "启动子代理后未收取输出即结束回合" in head:
    raise SystemExit("FAIL: item 15 still present; nothing changed")
if "16. **子代理任务文本可能根本没送达**" not in tail:
    raise SystemExit("FAIL: item 16 body not found; nothing changed")
collapsed = " ".join(tail.split())
item16_start = collapsed.index("16. **子代理任务文本可能根本没送达**")
item16_body = collapsed[item16_start:]
item16_body = item16_body.replace("。** 规则：", "。**\n   **规则：")

restored = head.rstrip("\n") + "\n" + ITEM_15 + "\n" + item16_body + "\n"

with io.open(AFTERCARE, "w", encoding="utf-8", newline="") as fh:
    fh.write(restored)
print("anti-pattern list repaired")
