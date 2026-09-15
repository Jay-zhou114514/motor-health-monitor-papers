# Conference Paper 骨架（初稿）

## 章节结构

1. **Introduction**
   - 小型工厂的低成本电机健康监测需求
   - 简单方法（阈值法 / 马氏距离）在文献中常被报告为"有效"
   - 本文问题：在严格评估与小样本条件下，这些方法会出现什么系统性失败？
2. **Related Work**
   - 轴承振动特征与经典阈值方法
   - 马氏距离用于状态监测
   - 数据划分、数据泄漏与评价偏差
3. **Method**
   - 特征提取（时域 + 频域）
   - 方法 A：3σ RMS 阈值；方法 B：马氏距离
   - 评价协议：window / file / leave-one-file-out
   - 统计工具：bootstrap 置信区间、条件数
4. **Experimental Setup**
   - 数据集与许可
   - train/test 划分（按文件，避免泄漏）
   - 参数：窗口 1 s / 步长 0.5 s / 分位数 0.99
5. **Results**
   - 基线性能与多层评价
   - 特征消融与依赖结构分析
   - 受控条件数实验（EXP-V1-04）
6. **Discussion**
   - 机制解释与证据强度（明确区分已证明 / 支持 / 推测）
   - 为什么"更多特征"反而更差
7. **Limitations**
   - 样本量、单文件、重叠窗口、非独立特征集
8. **Conclusion**

## 核心图表清单

| 编号 | 内容 | 来源 |
| --- | --- | --- |
| Fig. 1 | 系统与实验流程 | Master `docs/figures/` |
| Fig. 2 | 正常/外圈/内圈原始波形 | `waveforms.png` |
| Fig. 3 | 窗口级 vs 文件级指标对比 | `method_comparison.png` |
| Fig. 4 | 误报时间定位 | `error_localization.png` |
| Fig. 5 | 条件数 vs 误报 | `conditioning_control.png` |
| Table 1 | 特征集 / 条件数 / FP / F1 / 膨胀比 | EXP-V1-04 CSV |
| Table 2 | 多层评价指标（含 FPR / FNR） | EXP-V1-00 CSV |

## 可以砍掉的内容（会议版）

- 大量重复的稳健性扫描
- 跨数据集与真实设备实验（留给期刊版）
- 与深度学习的对比（除非成为核心论点）
