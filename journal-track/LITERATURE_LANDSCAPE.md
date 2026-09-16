# 文献地形与创新性定位（2026-09-16，Scopus 扫描）

- 完整报告：Master 仓库 `docs/literature/SCOPUS_LITERATURE_SCAN_2026-09-16.md`
- 原始计数：Master 仓库 `docs/literature/scopus_counts.csv`
- 方法：Scopus `TITLE-ABS-KEY` 检索；仅标题/摘要/关键词层，未做全文筛选

## 1. 拥挤区（不可作为创新点）

| 方向 | 命中 |
| --- | ---: |
| 轴承故障诊断 | 9,117 |
| Mahalanobis distance + fault diagnosis | 248 |
| Mahalanobis + bearing | 221 |
| 状态监测 + 误报 | 477 |
| 域偏移 + bearing | 280 |
| 数据泄漏 + 故障诊断 | 44 |
| 可复现性 + 故障诊断 | 119 |

**结论**：不能用"首次把马氏距离用于轴承诊断"或"首次关注数据泄漏"作为创新点。

## 2. 稀疏区（唯一可能站住的位置）

| 方向 | 命中 |
| --- | ---: |
| **Mahalanobis + shrinkage + bearing** | **1**（且属度量学习路线） |
| covariance + shrinkage + anomaly detection | 6（无一篇在工业振动领域） |
| evaluation pitfalls + machine learning | 6 |
| collinearity + anomaly detection | 9 |
| file-level / window-level + fault diagnosis | 12 / 14 |
| 功效分析 +（异常检测/状态监测） | 55 |
| 预注册 + machine learning | 28 |

## 3. 期刊线的贡献重新定位

EXP-V1-07 已经证伪"几何失效 + 收缩修复"的普遍性（膨胀未跨批次复现）。
结合本次文献扫描，期刊线应改为**评价方法学**方向：

> **贡献草案**：面向低成本状态监测，提出并示范一套"功效感知 + 批次级独立 + 多层级"
> 的检测器评价协议；给出一个"单数据集上看似显著、跨批次不复现"的实例，
> 并说明该实例如何改变结论（负结果同样是结果）。

该定位的依据：

- 领域内功效分析（55）与评价陷阱（6）相关工作极少；
- 数据泄漏/可复现性已有关注（44 / 119），但**尚未见到"功效不足 ≠ 被反驳"
  与批次级独立性结合**的工作；
- 负结果 + 方法学在 ML 领域有大量先例（1,891），但该细分在状态监测中稀疏。

## 4. 必须补齐的对比与引用

1. 经典 ML 基线：One-Class SVM / Isolation Forest（否则无法回应"简单 vs 现代方法"）；
2. 需精读并引用的近邻工作（6–55 篇区间）：功效分析与评价方法学文献；
3. 已有的数据泄漏/基准类工作（2026 MSSP 现实评估、PHM leakage-safe benchmark）
   必须作为相关工作引用，并说明我们的增量。

## 5. 下一步

1. 对稀疏区（6–55 篇）做全文精读，形成正式 Related Work 表；
2. 完成经典 ML 基线对比；
3. 据此发布期刊线 v1.4（评价方法学定位）。
