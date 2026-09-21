#!/usr/bin/env python3
"""Update the master repo's session brief and anti-pattern list after round 4.

Both repositories live under a path where the file-writing tool cannot update existing files,
so the edits are exact-match, asserted substitutions executed here instead.
"""

from __future__ import annotations

import io
import os
import re

MASTER = r"<WORKDIR>\Documents\Codex\2026-09-06\github\motor-health-monitor"
BRIEF = os.path.join(MASTER, "docs", "plans", "NEXT_SESSION_BRIEF.md")
AFTERCARE = os.path.join(MASTER, "docs", "EXPERIMENT_AFTERCARE.md")


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


# ------------------------------------------------------------------ the brief
brief = read(BRIEF)

brief = sub_once(
    brief,
    r"论文 v1\.0 稿\*\*已完成并经过三轮模拟审稿的修正\*\*",
    "论文 v1.0 稿**已完成并经过四轮模拟审稿的修正**（第 4 轮于 2026-09-20 完成，"
    "但**未取得独立性**，见 §4）",
    "brief section 0 status line",
)

brief = sub_once(
    brief,
    r"现在处在\"\*\*投稿前收尾\*\*\"阶段，剩三件事（见 §4）。",
    "现在处在\"**投稿前收尾**\"阶段：第 4 轮审稿已完成，剩两件需人工决定的事（见 §4）。",
    "brief section 0 remaining count",
)

new_section = """## 4. 下一步（按优先级）

1. ~~跑第 4 位审稿人~~ **已完成（2026-09-20），但独立性未达成**。
   - 报告：`conference-track/REVIEW_round4_reviewerC.md`（侧重报告完整性 + 读者可复现性），
     复算脚本与输出：`REVIEW_round4_number_check{,2,3,4}.py/.txt`，任务包：
     `REVIEW_round4_TASK_C.md`，修正脚本：`REVIEW_round4_apply_fixes{,6}.py`。
   - **过程事故**：为这一轮启动了 4 个子代理实例，**全部没有收到任务文本**（含 ASCII 探针），
     本会话多代理消息通道不可用 → 报告由主会话代理写成，**独立性未达成**，只能读作自检。
     若要真正的独立第 4 轮，需在通道可用的会话里重跑，或由用户另开一个任务。
   - **结论**：逐项复算 §3.1–§3.6、§5.1 与 Fig.1 图注，**零算术不一致**；
     第 3 轮 3 条 Major 全部已解决；问题集中在"数字→来源"的可追溯链（3 Major + 6 Minor），
     修正已应用到 v1.0 稿并提交。
2. **补两处归档产物**（第 4 轮 RC-M3 / RC-m2 的残留，需要写代码或补列）：
   - 把五条健康阶段规则的 SD(k_max) 以**带规则标签的 CSV** 落盘（当前只有散文表格）；
   - 在 `EXP-V1-10` 臂级汇总里补 zero-minimum 占比列，并给复制文件加 arm 列
     （现在 R=50 与 R=200 两臂无法被第三方分离）。
3. **语言润色**——注意：brief 原先引用的 `nature-polishing` skill **在本机并不存在**
   （`~/.codex/skills` 下无该目录）。可选替代：① 新安装的 `humanizer` / `humanizer-zh`
   （去 AI 写作痕迹，偏通用散文）；② `nature-writing`、`research-paper-writing`
   （偏学术结构，非纯语言）；③ 先安装 `nature-polishing` 再润色。**需人工选定后再动手**。
4. **投稿会议决定**——PHM Europe / PHM Conference / ICPHM；并决定是否等 V2 跨体系补齐。
   这会决定篇幅上限与润色力度，建议先定这个再润色。
5. **待办**：本地已提交 2 个 commit（`ce1e81a` 审稿记录、`80e1f5e` 稿件修正），
   2026-09-20 两次 `git push` 均因 GitHub 连接被重置而失败，需稍后重推。

"""

brief = sub_once(
    brief,
    r"## 4\. 下一步（按优先级，三件事）.*?(?=\n## 5\. )",
    new_section,
    "brief section 4 rewritten",
    flags=re.DOTALL,
)

write(BRIEF, brief)

# ------------------------------------------------------- anti-pattern addition
aftercare = read(AFTERCARE)

aftercare = sub_once(
    aftercare,
    r"(15\. \*\*启动子代理后未收取输出即结束回合 → 报告丢失\*\*"
    r"（首个 reviewerB 即如此丢失，不可取回）。\s*"
    r"\*\*规则：子代理任务必须要求把结果写入仓库文件，并在同一回合确认文件存在。\*\*)",
    r"\1\n16. **子代理任务文本可能根本没送达**（2026-09-20 第 4 轮审稿实测："
    r"4 个子代理实例全部报告\"没有收到任务\"，短 ASCII 探针亦未回执；"
    r"本会话多代理消息通道整体不可用）→ 报告只能由主代理代写，"
    r"**独立性未达成**。\n"
    r"    **规则：启动子代理后必须先确认它收到了任务**（要求回执一个约定 token 或一句话摘要）；"
    r"收不到就中止该路线，改由主代理执行，并在产物里**明确声明独立性未达成**，"
    r"而不是把自检当成独立审稿。",
    "anti-pattern 16",
    flags=re.DOTALL,
)

write(AFTERCARE, aftercare)
print("brief and aftercare updated")
