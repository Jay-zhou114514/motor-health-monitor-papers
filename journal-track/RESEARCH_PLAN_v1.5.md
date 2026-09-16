# Journal Track 研究计划 v1.5

- Version：v1.5
- Update basis：EXP-V1-09 + 文献审计（selection uncertainty / hyperparameter instability）
- Current stage：Evaluation-Reliability（三层框架 + 五维评价）
- Next experiment：EXP-V1-10（选择过程不确定性量化）

## 1. 期刊贡献定位（最终形态草案）

> **在状态监测领域应用并检验成熟的不确定性方法学**：
> 我们给出一个可复现的案例研究，说明在小样本、仅健康数据的轴承异常检测中，
> 数据划分、模型选择与结果报告三个层面都可能成为结论不确定性的来源，
> 并据此提出包含 **selection stability / cost / sensitivity** 的报告建议。

明确声明（防止创新性越界）：

- 概念层面**非原创**：stability selection（463）、nested CV（2,064）、
  hyperparameter variance（369）、model-selection uncertainty（599）已有成熟工作；
- 我们的增量是**领域应用 + 量化案例 + 报告规范**，以及一个公开的"不复现"实例。

## 2. 五维评价框架（期刊版核心）

| 维度 | 指标 | 现状 |
| --- | --- | --- |
| Performance | 记录级 FP / Recall / F1 | 已实现 |
| Selection stability | 模态占比、不同配置数、归一化熵 | EXP-V1-10 |
| Selection cost | 拟合次数、总耗时 | 已实现（EXP-V1-09） |
| Selection sensitivity | 重采样后配置是否改变 | EXP-V1-10 |
| Generalization | 选出的配置到新批次是否有效 | EXP-V1-10 / EXP-V1-11 |

## 3. 扩展实验路线

| 编号 | 实验 | 状态 |
| --- | --- | --- |
| EXP-V1-10 | 选择过程不确定性（固定测试集 + 50 次重采样） | **下一实验（已预注册）** |
| EXP-V1-11 | Paderborn 独立物理轴承（6 个独立单元） | 候选（需要时下载，~1 GB） |
| EXP-V2-01 | 跨数据集机制一致性 | 与 V1-11 合并考虑 |
| EXP-V2-02 | 真实自采数据 | 暂缓 |

## 4. 风险

1. 测试集分辨率约 7.1%（2 文件 × 7 窗口）→ P2 阈值可能无法可靠观测；
2. 独立单元数量少，不做显著性声称；
3. 概念非原创，写作必须严格区分"应用贡献"与"方法学发现"。
