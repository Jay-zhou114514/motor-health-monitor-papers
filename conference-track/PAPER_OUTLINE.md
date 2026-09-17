# Conference Paper 骨架（2026-09-18 重写）

**工作标题**：*How Many Healthy Recordings Do You Need? Reporting Uncertainty in
Normal-Only Bearing Anomaly Detection*

**替代标题（更保守）**：*Nominal Sample Size Is Not Effective Information:
An Evaluation-Reliability Study of Healthy-Data-Only Bearing Anomaly Detection*

- 定位：**评价可靠性 / 应用方法学**，不是新算法
- 主张范围：两个公开试验台（IMS + Paderborn）；措辞限于 "consistent in two rigs"

## 章节结构

1. **Introduction**
   - 低成本状态监测的典型做法：只用健康数据训练 → 报警阈值取训练分数的分位数
   - 工程问题不是"哪个算法更准"，而是"**我报出的误报率能不能信**"
   - 本文问三个问题：①选择准则在小 n 下能否区分配置？②报告的误报率有多稳？
     ③多采数据能不能改善它？
2. **Related Work**（必须显式承认既有工作，见 `CLAIM_EVIDENCE_MAP.md` §5）
   - 轴承特征与阈值方法；单类方法在状态监测中的使用
   - 通用异常检测的评价批评（Wu & Keogh 2021；point adjustment；排名不稳定性）
   - 模型选择方差（CV pitfalls 2014；MSAD / mTSBench）
   - 故障诊断中的最小样本量（功效分析，2010 / 2015）——**有监督分类**，与本文不同
   - 泄漏安全划分（Vieira 2026；Knap 2026）——**已占**，本文不主张
3. **Protocol**（引用 Master `docs/FROZEN_PROTOCOL.md`）
   - 数据集：IMS 1st/2nd/4th（20 kHz）、Paderborn K001–K006（64 kHz，4 工况 × 20 条）、MFPT
   - 特征（4 个，冻结）、检测器（3σ RMS / 马氏 / OC-SVM / iForest）、阈值 q=0.99
   - 纪律：测试集不参与任何选择；证据等级 A–D
4. **Part I — What does not reproduce**（C1, C7）
   - 单折"协方差几何失效"在 27 折中仅 1 折复现
   - 简单方法 vs 现代单类方法：3σ RMS 2.38% vs OC-SVM 27–50%
5. **Part II — The selection criterion at small n**（C2）
   - 92% 的复制存在并列；86% 的最小验证误报恰为 0
   - 结论：该规模下"选择"常常是任意的
6. **Part III — The noise floor and its sources**（C3, C6）
   - 固定测试集下误报率 0–14.3%，SD 4.13 pp
   - 方差分解：划分 5.20 pp vs 种子 4.39 pp（超参只占很小一部分）
   - 经典 1/√n 律在两个方向都不适用
7. **Part IV — Nominal vs effective sample size**（C4, C5）★核心
   - S1（同一批记录重采样）vs S2（真实新增记录）：n=96 时 SD 18.0 pp vs 0.0 pp
   - 跨 4 个工况：方向 3/4 稳健，所需记录数 80–96 且条件依赖
8. **Reporting checklist**（本文的可操作产出）
   1. 报告阈值估计所用的**训练窗口数**，而不是"数据集大小"；
   2. 报告**重采样波动**（至少覆盖划分与随机种子两个来源）；
   3. 当验证集分辨率粗于目标误报水平时，报告**并列率**；
   4. 区分"新增记录"与"重复采样"，不要用后者声称数据充足；
   5. 给出**独立单元数**（轴承/记录），不要只给窗口数。
9. **Limitations**（逐条照 `CLAIM_EVIDENCE_MAP.md` §4）
10. **Conclusion**：在本场景下，报告的误报率比经典理论认为的更不可靠，
    且只能靠**新增不同的真实记录**改善，所需数量依工况而定。

## 核心图表

| 编号 | 内容 | 来源 |
| --- | --- | --- |
| Fig. 1 | 实验流程与两个"增长来源"的对照（S1 vs S2 概念图） | 新绘 |
| Fig. 2 | 小 n 下的噪声下限：测试误报率分布 + 并列率 | `exp_v1_10_selection_uncertainty.png` |
| Fig. 3 | 方差分解：划分 vs 种子 vs 超参 | `EXP-V1-10-variance-decomposition.csv` |
| **Fig. 4** | **S1 vs S2：名义 n 与有效信息（主图）** | `exp_v2_01_cross_dataset_scaling.png` |
| Fig. 5 | 跨 4 工况稳健性 | `exp_v2_02_cross_condition.png` |
| Table 1 | 数据集与独立单元 | 冻结协议 |
| Table 2 | 检测器误报率（IMS 3 批次 + Paderborn） | `EXP-V1-08/09-summary.csv` |
| Table 3 | 主张 → 证据 → 等级 | `CLAIM_EVIDENCE_MAP.md` |

## 会议版可以砍掉

- Layer 1 的全部细节（只在 Related Work 一句带过）
- MFPT 故障判别实验（AUROC 全 1.000，无信息量）
- 其余 3 个工况的完整表格（保留 Fig. 5 与一句结论）

## 待补（写作前）

1. Fig. 1 概念图（需新绘）；
2. 报告清单是否需要附一个最小示例（用 IMS 数据演示"错误报告 vs 正确报告"）。