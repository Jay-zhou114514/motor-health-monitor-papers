# Journal Track 研究计划 v1.2

- Version：v1.2
- Update basis：EXP-V1-05 + 项目负责人最终审查（判定 B）
- Current stage：Evidence Strengthening
- Next experiment：**EXP-V1-06（A + B）**
- Update principle：Experimental-result-driven iterative planning

## 1. 判定摘要

| 项目 | 判定 |
| --- | --- |
| H1 方向归因 | 部分支持，Level B |
| H2 正则化干预 | 部分支持，Level B |
| "标准化投影幅度" | 有价值的后验线索，尚未独立验证 |
| LW δ = 0.220 | 当前有效，但不是已证明最优 |
| LW δ = 1.000 | 重要警告信号（边界解） |
| FP 9 → 1 | 值得追踪，但受 11 窗口限制 |
| 机制是否被推翻 | 没有 |
| 是否进入修复叙事 | 暂不建议 |

## 2. EXP-V1-06 结构

### A：验证 H1（预注册）

- 冻结指标：标准化投影幅度 = |投影到最小特征值方向| / √λ_min
- 验证方式：三折 leave-one-normal-file-out 轮换；如获得更多公开正常数据则追加
- 判据：问题组是否稳定高于对照组，且与 inflation / FP 同向

### B：验证 H2 与 δ 选择

- 比较：δ=0 / LOO likelihood / LW 解析式 / 其他预定义 training-only 准则
- 核心问题：training-only 准则能否稳定选出合理 δ
- 规则：测试集最后打开一次

## 3. 可以现在做 / 不能声称什么

可以现在做：定义准则、训练集内部 CV、方法比较、敏感性分析、
leave-one-file-out（数据结构允许时）、准则稳定性检查。

不能强声称：最优 δ、普适 δ 选择方法、跨设备/跨工况泛化、
普遍解决 Mahalanobis 误报膨胀。

## 4. 其余实验状态

| 编号 | 实验 | 状态 |
| --- | --- | --- |
| EXP-V1-06 | A 验证 H1 + B 验证 H2/δ 选择 | **下一实验** |
| EXP-V1-07 | 特征稳定性 / 跨文件稳健性 | 暂缓（部分内容并入 V1.06-A） |
| EXP-V2-01 | 跨数据集验证 | 暂缓 |
| EXP-V2-02 | 独立真实实验 | 暂缓 |

## 5. 触发条件

EXP-V1-06 完成 → 审查 → 若 H1/H2 复现则升级为 A 并重启扩展实验；
若不成立则重新定位机制。
