# Draft v0.6 — Related Work 引用语境修正（按 citation-audit Step 6）

- 日期：2026-09-20
- 触发：`CITATION_AUDIT.md` 提出 4 条"语境未核验" + 1 条 WEAK
- 依据：本轮补齐摘要后逐条判定

## 判定更新（摘要获取结果）

| # | 摘要获取 | 新判定 |
| --- | --- | --- |
| 3 Sehili & Zhang | ✅ arXiv 摘要已读 | **SUPPORTS**（原文即称"inappropriate or highly flawed protocols"） |
| 4 Bouthillier et al. | ✅ arXiv 摘要已读 | **FIX**——原文的方差来源是"data sampling, parameter initialization and hyperparameter choice"，**不是"仅随机种子"** |
| 11 Gungor et al. | ❌ Crossref 与 S2 均无摘要 | **仍不可核验** → 用词限制到标题层 |
| 13 Indira et al. 2010 | ❌ Crossref 与 S2 均无摘要 | **仍不可核验** → 用词限制到标题层 |
| 6 MSAD | ✅ 摘要已有 | **WEAK** → 限定到该文实际覆盖范围 |

## 需要应用的 4 处修改

### 修改 1 — 第 4 项（Bouthillier）：校准方差来源

- **原句**：`Bouthillier et al. [4] demonstrated that random-seed variance alone can change benchmark conclusions.`
- **改为**：
  `Bouthillier et al. [4] modelled the benchmarking process and showed that variance from data
  sampling, parameter initialisation and hyperparameter choice markedly affects the results.`
- **理由**：原文并未主张"仅种子即可"；原句把三条来源压缩成一条，属语境放大。

### 修改 2 — 第 6 项（MSAD）：限定范围

- **原句**：`For time-series anomaly detection specifically, MSAD [6] and mTSBench [7] evaluated
  model selection directly and found that current selection strategies remain far from optimal`
- **改为**：
  `For time-series anomaly detection specifically, MSAD [6] studies model selection *carried out by
  time-series classifiers* over a large configuration space and reports that the resulting choices
  are far from optimal, while mTSBench [7] benchmarks model selection across 344 series and finds
  that even the strongest selection methods remain far from optimal.`
- **理由**：MSAD 研究的是"用时序分类器做选择器"这一特定设定，与"训练内验证选择"不是同一件事；
  原句把两篇并列成同一主张，属语境合并。

### 修改 3 — 第 11 项（Gungor）：限制到标题层

- **原句**：`...robust evaluation frameworks for unsupervised detection [11]...`
- **保留原句，但加脚注**：`[11] 的摘要不可得，本引用仅依据其标题所述范围。`
- **理由**：标题即"a robust framework for evaluation of unsupervised time-series anomaly
  detection"，我们的用法与标题一致；但**不得**据此声称该文证明了任何具体结论。

### 修改 4 — 第 13 项（Indira 2010）：删去超出标题的措辞

- **原句**：`Power-analysis-based procedures have been proposed to determine the minimum number of
  vibration samples needed for a classifier to be trained with statistical stability [13]`
- **改为**：`Power-analysis-based procedures have been proposed to determine the minimum number of
  vibration samples needed for a classifier in vibration-based fault diagnosis [13]`
- **理由**："trained with statistical stability"来自**第 14 项**的摘要（我们读过），
  不属于第 13 项可核验的范围；原句把 14 的措辞挂到了 13 上。

## 结论

- 应用上述 4 处修改后，`CITATION_AUDIT` 的 4 条"语境未核验"降为 **2 条"标题层限定"**（已加脚注声明），
  WEAK 降为 **0**；
- **剩余风险（如实保留）**：第 11、13 项的摘要不可得，其引用强度只能到标题层。
  若定稿前能通过机构订阅取得摘要，应回补核对；
- 第 19 项（MFPT 著录）仍待处理。