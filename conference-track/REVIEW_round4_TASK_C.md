# 任务包：第 4 位审稿人（Reviewer C）

- 建立日期：2026-09-20
- 用途：把本轮审稿任务**落盘**，避免子代理任务文本投递失败（本项目已发生过一次：
  round-3 的首个 reviewerB 因任务文本未到达而其报告丢失）。
- 执行者：一个独立的子代理（Reviewer C）。执行者必须**先读本文件**，再开始工作。

---

## 0. 环境须知（很重要）

- 本机沙箱无法直接启动进程（报错 `windows elevated sandbox ... read-only carveouts`）。
  **所有 shell 命令都必须带 `sandbox_permissions: "require_escalated"` 执行**，否则一律失败；
  执行时在 `justification` 写一句原因即可。
- 用绝对路径，不要依赖 `cd`。当前工作目录 `C:\Users\32597`，
  **两个仓库都不在 cwd**，必须写全路径。
- 可用工具：`Get-Content` / `Get-ChildItem` / `Select-String`（`rg` 亦可）。

## 1. 你的身份与任务性质

你是 motor-health-monitor 项目论文的**第 4 位独立审稿人（Reviewer C）**。
这是**内部质量控制用的模拟审稿，不是真实盲审** —— 请在报告中如实标注这一点。

本轮的目的是：**验证前三轮的修正是否收敛、是否还有新问题**。

## 2. 仓库与输入

| 用途 | 路径 |
| --- | --- |
| Master（唯一事实来源，含 `experiments/` 与 `outputs/` 归档产物） | `C:\Users\32597\Documents\Codex\2026-09-06\github\motor-health-monitor` |
| 论文库 | `C:\Users\32597\Documents\Codex\2026-09-15\github\motor-health-monitor-papers` |
| **待审稿件（必读全文，446 行）** | `...\motor-health-monitor-papers\conference-track\PAPER_v1.0_submission-draft.md` |

配套文件（同目录 `conference-track\`）：`CLAIM_EVIDENCE_MAP.md`、`REFERENCES.md`、
`CITATION_AUDIT.md`、`NUMBER_TRACEABILITY_AUDIT.md`、`PAPER_OUTLINE.md`、`FIG1_NOTES.md`、
`figures/`、`STATUS.md`。

Master 侧：`docs\FROZEN_PROTOCOL.md`、`docs\REPRODUCIBILITY_PROTOCOL.md`、
`docs\EXPERIMENT_AFTERCARE.md`、`docs\plans\COMPLETENESS_AUDIT_v2.md`、`experiments\`、`outputs\`。

前三轮报告（可读，用于收敛复核）：`REVIEW_round1_reviewer_scope.md`、
`REVIEW_round2_serial_reviewerA.md`、`REVIEW_round3_reviewerB.md`。

## 3. 本轮审稿侧重（必须严格按此侧重，这是本次任务的核心）

前三轮已分别覆盖：Round 1 = scope；Round 2 = statistics；Round 3 = internal validity / 框架措辞。

**本轮 = 报告完整性（reporting completeness）+ 读者可复现性（reader reproducibility）。**

要回答的问题：**一个完全不在本项目里的读者，拿着这份稿件以及它指向的归档产物，
能不能独立判断每个数字/每个结论是怎么来的、适用边界在哪里、有没有必须报告却被省略的信息？**

请逐项检查（不限于这些）：

1. **数字可追溯链**：每个 printed number 是否给出
   实验编号 → 脚本 → CSV → 划分/种子 → 验证深度（L1/L2/L3）？找出断链处。
2. **报告项缺失**：训练窗口数 vs 记录/文件数；误报**计数**与**比率**是否区分；
   退化/饱和格（SD=0、n_eff=∞）是否显式报告；被排除的折是否说明；测试集被打开几次；
   随机种子的来源与跨进程确定性；超参（含 λ、δ）来源是否为 training-only。
3. **读者可执行路径**：稿件与仓库是否给出"从原始数据到图/表"的可运行入口
   （README、脚本名、命令、数据获取与许可）？第三方照做能否复现？
4. **图-文-数据一致性**：Fig.1 图注 vs 正文 vs CSV；表格列名是否说清判据
   （如"单调下降"vs"秩相关"）。
5. **表述完整度**：限定语（证据等级 A/B/C/D、单数据集、样本量、重叠窗口、
   pre-protocol 范围）是否随每个结论出现；Abstract / Conclusion 是否漏掉必要限定。
6. **允许并鼓励重算数字**，但不要把"我算不出"当成主结论，除非确实算不出；
   重算结果请给出 CSV 行。

### 3b. 已知的可疑点（请独立核实，不要因为是"已知"就跳过，也不要直接采信）

- §3.5 末段称"Fourteen classes of analysis error are listed in the project's disclosure
  register (`docs/EXPERIMENT_AFTERCARE.md`)"。请核对：该文件实际列出的条目数与"14"是否一致、
  条目是否真是"被发现的错误类别"、"11 + 3"的拆分能否在文件中找到依据。
- §5.1 引用的 `experiments/EXP-V2-03-per-bearing-rms.csv` 内容是否真的支持
  "per-bearing mean RMS ranges from 0.171 to 0.403"。

## 4. 收敛复核（附加一节，必写）

逐条复核 Round 3 的 RB-M1 / RB-M2 / RB-M3 及 RB-m1..RB-m10 在 v1.0 稿中是否**真的**已解决
（给出稿件中对应句子的引用作为证据），判定"已解决 / 部分解决 / 未解决 / 改成了别的问题"。
Round 1 / Round 2 的条目只需抽查，不必逐条。

## 5. 边界声明（必须写进报告）

- 不做文献审计（除检查引用条目是否与正文主张匹配外）；
- 不重跑实验；原始振动特征管线视为给定；
- Section 2 的数据集元数据可视为给定，但你若抽查到不一致**必须报告**；
- 报告里要明确列出"我核验了什么 / 我按给定接受什么"。

## 6. 输出要求（强制，违反即视为任务失败）

1. 完整报告写入：
   `C:\Users\32597\Documents\Codex\2026-09-15\github\motor-health-monitor-papers\conference-track\REVIEW_round4_reviewerC.md`
2. 结构对齐 `REVIEW_round3_reviewerB.md`：
   - 开头 **Provenance and limitation note**：含"本报告是内部质量控制、非盲审"；
     第一段抄写一句**你收到的任务摘要**（证明任务文本确实到达）；
     若你读过前三轮报告或项目内部文档，如实声明非独立性。
   - **Review setup**：Input scope / Assessment boundary / Shared claim summary /
     Visible evidence base / Missing materials affecting confidence。
   - 逐条 concern，每条含：Concern ID（Major `RC-M1…`，Minor `RC-m1…`）、Severity、
     Blocking（Yes/No）、Axis、Claim pointer、Evidence pointer（必须给文件路径，
     尽量给行号或 CSV 行）、Concern、Why it matters、Resolution test。
   - **Convergence check** 一节（见 §4）。
   - 末尾 **Risk and unsupported claims** 清单。
   - 语言用英文（与前几轮一致）。
3. **在同一回合内**用工具确认文件存在且非空（例如 `Get-Item`），并把"路径 + 字节数"
   写进你的最终回复。
4. 最终回复给发起者：报告路径、字节数、Major/Minor 数量、以及 3–6 条最关键的发现摘要
   （每条一句话）。

## 7. 禁止事项

- 禁止把结果只写在聊天里而不落盘（本项目已因此丢失过一份 reviewerB 报告）。
- 禁止编造证据：每个 concern 必须指向真实存在的文件/行。
- 禁止把"统计功效不足 / 无法判定"升级成"已被反驳"。
- 禁止把 `docs/plans/NEXT_SESSION_BRIEF.md` §5 已声明并**已接受**的缺口当作新问题提出：
  pre-protocol 实验未做三层验证、V1-05~09 未做 L3 重跑、MFPT 官方著录未确认、
  中文文献与 PHM 会议集未覆盖、无自采数据。这些最多在"已知限制"里一笔带过。
- 报告必须自洽、可被他人直接阅读，不依赖聊天记录。
