# Conference Track 研究计划 v1.0

- Version：v1.0
- Update basis：EXP-V1-01 ~ EXP-V1-04
- Current stage：Failure Mechanism Investigation
- Next experiment：待 EXP-V1-04 完成结果审查与假说判定后决定
- Update principle：Experimental-result-driven iterative planning

## 1. 定位

从 Master 中抽取一个已经形成闭环的核心研究故事，追求"最小完整闭环"：
一个清晰的问题 + 一组关键实验 + 一个可解释的发现（允许是明确的负结果）。

## 2. 核心故事候选

**候选 A（若 EXP-V1-04 支持病态协方差假说）**

> 小样本、高相关特征条件下，基于马氏距离的轴承异常检测会出现系统性误报；
> 通过受控实验定位到协方差病态与特征方向的作用。

核心链条：Baseline → Feature Ablation → Error Localization → V1-04 受控实验 → 核心发现与讨论。

**候选 B（若 EXP-V1-04 不支持）**

会议故事必须跟随新证据调整，例如围绕 threshold sensitivity、distance distribution
或其它经验证的机制形成新的闭环。**不得为了保住原故事而追加实验。**

**当前状态**：EXP-V1-04 为"部分支持"（见 `shared/EXP-V1-04-DECISION-GATE.md`），
按规则处于分支 C——需要先完成正式审查，再决定会议故事取 A 还是调整。

## 3. 内容边界

保留：

- 核心研究问题与动机
- 关键实验（Baseline、Feature Ablation、Error Localization、V1-04）
- 主要失败案例与其解释
- 核心图表（见 `PAPER_OUTLINE.md`）

可以省略：大量重复性稳健性实验、更多数据集、完整真实实验。

**不得省略**：数据划分原则、关键实验条件、核心限制，以及影响结论可信度的信息。

## 4. 投稿前门槛

1. 核心研究问题明确。
2. 至少形成一个足够完整的核心实验闭环，或形成有价值的明确负结果。
3. 实验不只有 Accuracy 表格，而能解释现象或机制。
4. 代码与实验记录可复现。
5. 论文诚实区分"已证明""支持""推测"。

详见 `SUBMISSION_CHECKLIST.md`。

## 5. 版本更新触发条件

- 触发 1：EXP-V1-04 完成结果审查 → 判定 → 风险审查 → 发布 v1.1。
- 触发 2：任何新关键实验（如 EXP-V1-05）完成后，重新评估"是否达到投稿门槛"。

## 6. 当前最大风险

1. 样本量小（22 训练窗口 / 11 正常测试窗口 / 1 个正常测试文件）→ 机制结论的证据强度受限。
2. 特征集是嵌套结构，统计推断的独立性假设不成立。
3. 若机制无法在本数据集内被受控实验确认，会议故事可能要转向"负结果"叙事。
