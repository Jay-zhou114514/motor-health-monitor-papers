#!/usr/bin/env python3
"""Repair pass 2: the marker consumed the "16. " prefix, so rebuild it explicitly."""

from __future__ import annotations

import io
import os

AFTERCARE = os.path.join(
    r"<WORKDIR>\Documents\Codex\2026-09-06\github\motor-health-monitor",
    "docs", "EXPERIMENT_AFTERCARE.md",
)

ITEM_15 = (
    "15. **启动子代理后未收取输出即结束回合 → 报告丢失**（首个 reviewerB 即如此丢失，不可取回）。\n"
    "   **规则：子代理任务必须要求把结果写入仓库文件，并在同一回合确认文件存在。**"
)

with io.open(AFTERCARE, "r", encoding="utf-8", newline="") as fh:
    text = fh.read()

marker = "\\1\\n16. "
if marker not in text:
    raise SystemExit("FAIL: mangled marker not found; nothing changed")
if "启动子代理后未收取输出即结束回合" in text:
    raise SystemExit("FAIL: item 15 already present; nothing changed")

head, tail = text.split(marker, 1)
body = tail.replace("\\n", " ").replace('\\"', '"')
body = " ".join(body.split())
if not body.startswith("**子代理任务文本可能根本没送达**"):
    raise SystemExit(f"FAIL: unexpected item-16 body: {body[:60]!r}")

# put the rule sentence on its own indented line, as the rest of the list does
body = body.replace("。** 规则：", "。**\n   **规则：")

restored = head.rstrip("\n") + "\n" + ITEM_15 + "\n16. " + body + "\n"

with io.open(AFTERCARE, "w", encoding="utf-8", newline="") as fh:
    fh.write(restored)
print("anti-pattern list repaired (items 15 and 16)")
