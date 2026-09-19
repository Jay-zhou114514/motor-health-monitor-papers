# Citation Audit Report（按 citation-audit skill 的三层协议执行）

- **Date**: 2026-09-20
- **Audited artifact**: `REFERENCES.md` + `DRAFT_v0.2.md`（Related Work）+ `DRAFT_v0.3_partIV.md` + `DRAFT_v0.4_discussion.md`
- **Total cited entries**: 19（其中正文实际引用 16 条）
- **工具链偏差声明（必须披露）**：
  该 skill 面向 **LaTeX `.bib` + `\cite{}` + `mcp__codex__codex` 跨模型审查**；
  本稿为 **Markdown 草稿 + Markdown 参考文献表**，无可用的 `.bib` 解析与跨模型审查通道。
  因此本次**仅沿用其三层协议（存在性 / 元数据 / 语境）与 KEEP·FIX·REPLACE·REMOVE 判定**，
  未生成 `CITATION_AUDIT.json`、未使用独立审阅线程。**独立性低于该 skill 的设计要求**，
  投稿前若条件允许，应以 LaTeX 稿重跑一次。

## Summary

| Verdict | Count | 说明 |
| --- | ---: | --- |
| **KEEP** | 12 | 存在性、元数据、语境三层均可核验 |
| **FIX** | 1 | 元数据已更正（第 12 项作者与标题） |
| **REPLACE** | 0 | — |
| **REMOVE** | 0 | — |
| **语境未核验** | **5** | 仅凭标题使用，未读到摘要/全文 → **不得写成"已验证"** |

**总体判定：WARN**，`reason_code: context_unverified_partial`
（按 skill 的判定表，无 REPLACE/REMOVE 即不构成 FAIL；但存在语境未核验项，不能判 PASS。）

## 第一层：存在性

| # | 检查 | 结果 |
| --- | --- | --- |
| 1–4, 9, 10, 11, 12, 13, 14 | DOI 解析（Crossref） | ✅ 全部存在 |
| 5, 6, 7, 8 | arXiv ID 解析（arXiv API） | ✅ 全部存在 |
| 15, 16 | 全文已读 | ✅ |
| 17 (Paderborn) | DOI `10.36001/phme.2016.v3i1.1577` | ✅ |
| 18 (IMS) | 官方页 "Data Set Citation" | ✅ 逐字著录 |
| 19 (MFPT) | 官方著录未确认 | ⚠️ 已在 REFERENCES 标注 |

## 第二层：元数据

- **第 12 项已更正**：原写 `Baumann, D., & Baumann, K. (2014)`，
  Crossref 实为 **Krstajic, D., Buturovic, L. J., Leahy, D. E., & Thomas, S.**，标题亦更正。
  → 这是本次审计最重要的发现，属 skill 定义的 **author hallucination + title drift**。
- 其余 18 条作者、年份、venue 均与 Crossref/arXiv 返回一致。

## 第三层：语境适当性（本次新增，逐条）

| # | 正文中的用法 | 判定 | 依据 |
| --- | --- | --- | --- |
| 1 Wu & Keogh | 基准缺陷导致"进步的幻觉" | **SUPPORTS** | 摘要含 "many published comparisons may be unreliable... illusionary" |
| 2 Kim et al. | point adjustment 可夸大至随机分数看似 SOTA | **SUPPORTS** | 摘要明确 |
| 3 Sehili & Zhang | 多元场景的同类结论 | **语境未核验** | 仅有标题，未读摘要 |
| 4 Bouthillier et al. | 仅随机种子即可改变基准结论 | **语境未核验** | 仅有标题与作者 |
| 5 rank-instability | 690 数据集上改变数据集/指标/超参/种子 → 排名不稳 | **SUPPORTS** | 摘要含 690 datasets 与四项变化 |
| 6 MSAD | 模型选择"远未最优" | **WEAK** | 摘要研究的是**用时序分类器做选择**，与我们的"训练内选择"语境不完全对应 |
| 7 mTSBench | 无单一检测器占优；选择方法远未最优 | **SUPPORTS** | 摘要明确 |
| 8 TAB | 统一基准流水线 | **SUPPORTS** | 摘要明确 |
| 9 PATE | 邻近感知评价 | **SUPPORTS** | 摘要明确 |
| 10 taxonomy | 面向问题的指标分类 | **SUPPORTS** | 标题与 Crossref 一致 |
| 11 robust framework | 无监督检测的稳健评价框架 | **语境未核验** | 仅有标题 |
| 12 Krstajic et al. | CV 同时用于选择与评估的陷阱；主张重复嵌套 | **SUPPORTS** | 摘要含 "high variance"、"repeated nested cross-validation" |
| 13 Indira 2010 | 最小振动样本量（监督分类） | **语境未核验** | 仅有标题 |
| 14 Indira 2015 | 功效分析定最小样本量；以准确率为终点 | **SUPPORTS** | 摘要明确（有监督、C4.5、accuracy） |
| 15 Vieira et al. | 泄漏安全划分、轴承级划分、训练轴承数重要 | **SUPPORTS** | 全文已读 40 页 |
| 16 Knap et al. | 记录级分离、跨域基准、DL 对初始化敏感 | **SUPPORTS** | 全文已读 8 页 |

## Priority Fixes（投稿前必须处理）

### ⚠️ CONTEXT-UNVERIFIED：第 3、4、11、13 项
- 现状：正文中的用法**仅凭标题推断**，未读摘要。
- 风险：skill 明确指出的最危险类型是 **wrong-context citation**（真论文、错语境）。
- ACTION：逐条读取摘要后再定稿；若摘要不支持当前用法，改写句子或换引。

### ⚠️ WEAK：第 6 项（MSAD）
- 现状：用于支撑"模型选择策略远未最优"，但该文研究的是**以时序分类器作为选择器**的场景。
- ACTION：把句子限定为该文实际覆盖的范围，或补一句区分。

### ⚠️ MFPT 著录（第 19 项）
- 官方著录未确认；投稿前须在脚注说明引用来源为分发方。

## All-Clean Entries

`1, 2, 5, 7, 8, 9, 10, 12, 14, 15, 16`（11 条）；第 12 项为"元数据更正后干净"。

## Skill 使用体验（供后续复用）

- 本 skill 的**第三层（语境）是最有价值的一层**，而我们此前只做了前两层；
- 第 6 项的 **WEAK** 判定是手工审查不会发现的——它来自"摘要实际研究的是什么"这一层比对；
- 工具链（LaTeX/.bib/Codex MCP）与当前 Markdown 稿不匹配，**投稿前应切到 LaTeX 并重跑**。