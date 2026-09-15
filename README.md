# Motor Health Monitor · 双线论文计划仓库

Conference-first + Journal-extension，共享同一个 Master Research Project。

## 三条内容线

| 线 | 位置 | 职责 |
| --- | --- | --- |
| Master Project | [Jay-zhou114514/motor-health-monitor](https://github.com/Jay-zhou114514/motor-health-monitor) | 全部实验、代码、原始结果、失败结果、图表、实验日志与版本记录（唯一事实来源） |
| Conference Track | `conference-track/` | 从 Master 抽取一个已闭环的核心研究故事，最小完整闭环 |
| Journal Track | `journal-track/` | 在会议核心发现上扩展机制验证、稳健性、跨数据集与真实实验 |

原则：**研究优先，发表第二**。任何版本都不为了投稿而维持既定故事。

## 仓库结构

```text
motor-health-monitor-papers/
├── README.md                  # 本文件
├── WORKFLOW.md                # 固定工作流（结果审查 → 假说判定 → 风险审查 → 更新路线 → 版本）
├── CHANGELOG.md               # 双线计划版本变更记录
├── shared/                    # 两条线共享的规则、决策门、伦理与模板
├── conference-track/          # 会议线：计划、状态、论文骨架、投稿门槛
└── journal-track/             # 期刊线：计划、状态、论文骨架、扩展政策、实验协议
```

## 固定工作流

```text
实验完成 → 结果审查 → 假说判定 → 风险审查 → 更新研究路线 → 发布新版本（Vx.y）
```

每个实验交付：**实验结果、脚本/日志、CSV、图、初步理解**。
版本号不预先决定内容——先看结果，再决定下一版写什么。

## 当前状态（2026-09-15）

- 共同决策门 EXP-V1-04（良态特征集受控对照）已完成。
- 初步判定：预测 1（条件数越高误报越多）**部分支持**；预测 2（条件数越高阈值越不稳定）**不支持**。
- 误报只出现在含 RMS + 谱质心的特征组合，其距离膨胀比 > 1（1.35~1.50），其余组合 < 0.8。
- 2026-09-15：结果审查与假说判定已完成（结论见 `shared/EXP-V1-04-DECISION-GATE.md`），V1-05 已锁定为 **Covariance Geometry & Regularization**；双线计划发布 V1.1。

详见 `shared/EXP-V1-04-DECISION-GATE.md`。

## 命名规范

| 对象 | 命名 |
| --- | --- |
| 实验 | `EXP-<阶段>-<两位序号>`（编号永不复用，注册表在 Master 仓库 `experiments/README.md`） |
| 计划版本 | `RESEARCH_PLAN_v<major>.<minor>.md`（每条线各自维护） |
| 版本变更 | `CHANGELOG.md`，分类：保留 / 删除 / 修改 / 新增 / 延后 / 因实验结果而改变 |

