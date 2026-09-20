# Layer 1 — humanizer / humanizer-zh 扫描（只检测，不改正文）

- 日期：2026-09-20
- 对象：`PAPER_v1.0_submission-draft.md`（收紧第二层主张之后的最新版）
- 依据：`humanizer` v3.0.0（Wikipedia "Signs of AI writing"）与 `humanizer-zh`
- 机器输出：`POLISH_L1_scan.py`、`POLISH_L1_scan.txt`
- **本文件未修改任何正文文字。** 所有条目仅为待办清单，交 Layer 2 处置。

## 0. 总体判断

词汇层面很干净：AI 高频词只命中 `key`(1)、`robust`(1)；连接词只命中 `therefore`(13)，
其余（however / moreover / furthermore / additionally / notably / in conclusion 类）**零命中**；
无 chatbot 残留、无表情符号、无"知识截止"免责声明、无弯引号。**论文不像 AI 生成的通用文本。**

真正的问题集中在**结构节奏**（同一句式连续四段）、**元话语密度**（每段都自称我们做了什么）
和**若干超长句**上；另有一条属于 claim 缺陷、需要尽快处置：

> **L293（§5.1）与 L404（§7）仍写着 "the defensible ratio is about 3.5-fold rather than
> an order of magnitude"。** 这正是第 3 轮 RB-M2 要求删除的"把下界当上界"表述，
> 上一轮只清理了 §5.5，漏了这两处。它**不只是风格问题**：§3.1 已明确该比值只是下界
> （"ratios larger than ten cannot be excluded"），两处残句与 §3.1 直接矛盾。

## 1. 疑似 AI 腔

| # | 位置 | 现象 | 说明 |
| --- | --- | --- | --- |
| 1 | L176 / L185 / L194 / L204 | **§3.6 四个段落全部以同一模板开场**：粗体断言短句 + 逗号后的展开（"**The selection criterion is often non-discriminative.**"…） | humanizer §19（bold as decoration）＋ §2（staged opener）。四段同构，是这个稿件里最像 AI 腔的地方 |
| 2 | L1 / 标题 | "Three Faces of Evaluation Uncertainty…" | 三段式框架是有意设计，保留；但需确认 Abstract / §1 / §3 / §7 里对 "three faces / three choices / three analyst choices" 的回指是否过密（现有 8 处） |
| 3 | L293 / L404 | "rather than an order of magnitude" | 见 §0 的警示；属 claim 缺陷，非风格 |
| 4 | 全文 | 元话语密度偏高："we state this plainly"、"we report it as such"、"we flag this as a remaining limitation"、"we make no claim"、"we do not claim"（约 8 处） | 每段都自我说明一次，读起来像作者在向审稿人解释，而非在陈述结果 |

## 2. 重复句式

| # | 位置 | 现象 |
| --- | --- | --- |
| 1 | L176–L206 | 四个同模板的粗体开场（见上） |
| 2 | 全文 | `rather than` 约 14 处，是全文最集中的对比句式（其中多数**不是** AI 套话，而是必要的范围限定，需逐条判断） |
| 3 | 全文 | 段落收尾惯用"我们没主张什么"式免责句：`not testable`(3)、`we do not claim`(2)、`cannot`(5) 集中在各节末尾 |
| 4 | L110 / L80（§3.2 / §3.1 引导句） | 两句都是"固定了 A、B 和 C，然后我们比较…"的长列举句，结构同型 |

## 3. 不自然的连接词

| 连接词 | 次数 | 备注 |
| --- | ---: | --- |
| `therefore` | 13 | **唯一高频连接词**，集中在 §3.6 与 §4；Layer 2 建议把其中一半改为句序或分号结构 |
| `however` / `moreover` / `furthermore` / `additionally` / `notably` / `importantly` / `in particular` | 0 | 无需处理 |

## 4. 过度概括

| # | 位置 | 现象 | 处理建议 |
| --- | --- | --- | --- |
| 1 | L345 附近（§5.4） | "a study that reports a single within-bearing number may present a detector with a 40% false-alarm rate as having none" — 由本文单数据集结果推向一般性建议 | Layer 2 加限定（例如限定到"本文所测的这类试验台"） |
| 2 | §4 末段 | "The remaining content of §3.1 and §3.2 should be read as quantification of phenomena that [15] and [16] already established" — 对他文覆盖范围做概括判断 | Layer 2 收窄为"与本工作的测量范围重叠" |
| 3 | Abstract 首句段 | "Using five public bearing sources under a pre-registered protocol" — 五个来源，但独立单元数很少（Paderborn 6 轴承） | Layer 2 决定是否在此处即给单元数量级 |
| 4 | 第二层主张 | 收紧后（Abstract / §3.2 / §7 已统一为"稳定性依赖于跨折变异的定义与估计；折间口径下 80% 准则未达到"）**无过度概括** | 无需处理 |

## 5. 过长句

209 句中 27 句超过 45 词（13%），均值 29.9 词。最长的六句：

| 行 | 词数 | 内容 | 备注 |
| --- | ---: | --- | --- |
| L110 | 144 | §3.2 表前的引导句 | **其中约 30 词是本次为补溯源（EXP-V2-05/06 与 CSV 名）加进去的**，Layer 2 应把溯源移到脚注或独立句 |
| L80 | 140 | §3.1 表前的引导句 | 同上（EXP-V2-03 溯源） |
| L142 | 125 | §3.3 规则定义句（含 `clip(max(20, 0.10·N), 20, 60)`） | 公式本身占位；建议拆成"规则 + 变体"两句 |
| L421 | 114 | Fig.1 图注 (b) | 图注可拆为两句 |
| L55 | 88 | §2 Datasets | 本次加入 IMS `2003.10.22*` 选取规则后续句变长 |
| L312 | 82 | §5.2 备择解释 | 建议拆分 |

## 6. claim 强度异常

| # | 位置 | 词 | 判断 |
| --- | --- | --- | --- |
| 1 | L293 / L404 | `order of magnitude` | **超标**：与 §3.1 的下界声明矛盾，需按 RB-M2 删除该从句 |
| 2 | L102 附近 | `unambiguous`（"The direction is unambiguous"） | 需核对：该方向来自单一试验台、单一检测器、单一工况，措辞可降为"consistent across the six held-out bearings" |
| 3 | §3.1 | `substantially`(1) | 抽象层使用，量级由数值支撑，可保留 |
| 4 | §3.4 | `proves`(1)（"If the boundary sensitivity proves negligible…"） | 无问题（条件句） |
| 5 | 全文 | `cannot`(5) / `never`(2) / `always`(1) / `must`(3) | 抽查方向正确：多用于范围限定而非主张扩张 |

## 7. 中英文术语不一致

### 7.1 英文内部

| 术语对 | 计数 | 问题 |
| --- | --- | --- |
| `false-alarm` / `false-positive` | 16 / 1 | Fig.1 图注 (b)（L421）用 false-positive，正文其余用 false-alarm；**统一为 false-alarm** |
| `recording(s)` / `record(s)` | 38 / 13 | 混用。§3.6 清单第 1 条恰恰要求区分"记录"与"窗口"，此处更需统一口径 |
| `scope` / `definition` | 11 / 8 | 与中文三层（口径 / 单元数 / 定义）对应正确，但英文 `scope` 同时承担"评估范围"与"口径"两义，需确认 §3.1 标题 "Scope: does the split keep physical units apart?" 不与 §2 的 "assessment scope" 混淆 |

### 7.2 论文（英文）↔ 项目文档（中文）

| 中文文档用语 | 论文英文 | 判断 |
| --- | --- | --- |
| 口径（C8）/ 单元数效应（C9）/ 定义效应（C10） | scope / units / definition | 一致 |
| 健康阶段规则（EXP-V2-04、FROZEN_PROTOCOL） | `healthy/degraded boundary`(4) 与 `healthy-phase rule`(2) **并存** | 不一致：需在 Layer 2 二选一（建议中文表"规则"、英文统一 `healthy-phase rule`，并在首次出现处给等价说明） |
| 池化 / 折间（本轮新增） | `pooled`(9) / `between-fold`(8) | 已在 §3.2 定义，一致 |
| 独立单元 / 记录 / 窗口 | independent unit(8) / recording / window | 与 FROZEN_PROTOCOL 的三层口径一致 |
| 单元数效应、定义效应（CLAIM_EVIDENCE_MAP 的 C9/C10 名称） | 论文中无对应固定短语（§3.2/§3.3 用疑问句标题） | Layer 2 决定是否加一个固定短语以便交叉引用 |

## 8. Layer 2 待办（等会议确定后执行）

执行前需要 venue 的四项参数：**page limit、paper type、abstract length、section structure、
reference style**。等这些确定后再动正文，届时按下列顺序处理：

1. 先修 L293 / L404 的 `order of magnitude`（属事实性措辞，不等 venue 也应修）；
2. 打散 §3.6 的四段同构开场，降低元话语密度；
3. 拆分 §5 表格前与图注中的超长句，把本轮补入的溯源信息移到脚注/独立句；
4. 统一 `false-alarm`、`recording`、`healthy-phase rule` 三个术语；
5. 按 venue 的篇幅与结构要求整体压缩。
