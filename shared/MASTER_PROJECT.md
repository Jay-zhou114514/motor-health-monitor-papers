# Master Research Project 资料管理

## 唯一事实来源

Master 仓库：<https://github.com/Jay-zhou114514/motor-health-monitor>

所有内容都保存在 Master，论文仓库只做"抽取 + 组织"：

| 内容 | 存放位置 |
| --- | --- |
| 代码与检测器实现 | Master `src/` |
| 实验注册表 | Master `experiments/README.md` |
| 实验记录（契约/结果/Observation/Interpretation/Limitation） | Master `experiments/EXP-*.md` |
| 结果 CSV | Master `experiments/EXP-*.csv` |
| 运行日志 | Master `experiments/EXP-*-run-log.txt` |
| 图表 | Master `docs/figures/` |
| 工程路线图 | Master `docs/ROADMAP.md` |
| 研究计划版本 | Master `docs/plans/` |
| 单元测试 | Master `tests/` |

## 规则

1. **任何数字都必须能在 Master 里追溯到脚本 + 日志 + CSV。**
2. 论文只能引用**已冻结、可复现**的结果（结果冻结 = 脚本、参数、数据划分、CSV 都已入库）。
3. 失败实验必须保留，禁止删除不利结果。
4. 论文仓库中引用结果时，必须写明实验编号（如 EXP-V1-04）与 Master 提交哈希。
5. 任何"最新结果"在完成结果审查前，不得写进论文正文。

## 命名

- 实验：`EXP-<阶段>-<两位序号>`（永不复用）
- 计划版本：`RESEARCH_PLAN_v<major>.<minor>.md`
- 记录：`EXP-<编号>-<短名>.md` / `.csv`
