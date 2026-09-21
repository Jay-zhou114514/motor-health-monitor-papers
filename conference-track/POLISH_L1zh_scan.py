#!/usr/bin/env python3
"""humanizer-zh scan of the Chinese counterpart (detection only)."""

from __future__ import annotations

import io
import os
import re

TRACK = r"<WORKDIR>\Documents\Codex\2026-09-15\github\motor-health-monitor-papers\conference-track"
ZH = os.path.join(TRACK, "PAPER_v1.0_中文版.md")

with io.open(ZH, "r", encoding="utf-8", newline="") as fh:
    text = fh.read()
lines = text.split("\n")


def hits(label, pattern):
    found = [(n, l.strip()) for n, l in enumerate(lines, 1) if re.search(pattern, l)]
    print(f"\n### {label}: {len(found)} lines")
    for n, l in found[:25]:
        print(f"  L{n}: {l[:120]}")
    if len(found) > 25:
        print(f"  ... {len(found) - 25} more")


hits("破折号 —— （humanizer-zh §13）", "——")
hits("否定式排比 不是…而是 / 而非 / 不只是（§9）", r"不是[^。]{0,40}而是|而非|不只是|不仅仅")
hits("元话语 我们如实/我们报告/我们不作/我们不声称", r"我们(如实|报告|声明|主张|不声称|不主张|不把)")
hits("连接词 因此/值得注意的是/应当指出", r"因此|值得注意的是|应当指出|总而言之")
hits("夸张意义 标志着/彰显/凸显/至关重要/关键在于", r"标志着|彰显|凸显|至关重要|关键在于")
hits("通用积极结尾 前景/展望/未来", r"前景|展望|未来|下一步最自然")

bold = re.findall(r"\*\*[^*]{1,20}\*\*", text)
print(f"\n### 粗体强调次数: {len(bold)}；样例 {bold[:12]}")

print("\n### 长句（>60 字）")
sentences = [s for s in re.split(r"(?<=[。；])", text) if len(s) > 60]
print(f"  count={len(sentences)}")
for s in sorted(sentences, key=len, reverse=True)[:10]:
    print(f"  [{len(s)}] {s[:110]}")
print("\nscan complete")
