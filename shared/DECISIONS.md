# 结构性决策记录

这里记录**长期生效的结构性决策**（不是实验结果）。实验结论在 Master 仓库的实验记录里。

格式：编号 / 日期 / 决策 / 理由 / 影响 / 状态。

---

## D-001 论文仓库结构

- 日期：2026-09-15
- 决策：采用「一个论文仓库 + 两条线目录」：
  `motor-health-monitor-papers` 下设 `conference-track/`、`journal-track/`、`shared/`；
  `motor-health-monitor` 保持**唯一事实来源（Master）**。
- 理由：实验数据不会因为会议线与期刊线分开而复制、分叉；论文层只做"抽取 + 组织"。
- 已否决的替代方案：为会议线与期刊线各建一个独立仓库（会导致数据分叉与重复维护）。
- 影响：论文层引用结果时必须写明实验编号（如 EXP-V1-05）与 Master 提交哈希。
- 状态：**已确认（项目负责人，2026-09-15）**

---

## D-002 CHANGELOG 只写触发条件，不预写版本内容

- 日期：2026-09-15
- 决策：新版本的内容不在 `CHANGELOG.md` 中预先填写；只写"触发条件"。
  版本真正发布时才填写实际变更，并按六分类记录
  （保留 / 删除 / 修改 / 新增 / 延后 / 因实验结果而改变）。
- 理由：EXP-V1-04 只**部分支持**原假设，路线因此从 condition number
  转向 covariance geometry / directional attribution 与正则化。
  若预先写死版本内容，就会迫使研究迁就计划。
- 影响：每个版本必须包含六要素报告；任何路线变化都要留下可追溯的记录。
- 状态：**已确认（项目负责人，2026-09-15）**

---

## D-003 证据等级与措辞纪律

- 日期：2026-09-15
- 决策：所有机制表述必须标注证据等级 A/B/C/D；
  Level C/D 的内容不得写入 Abstract 或 Conclusion；
  来自事后观察的解释必须显式注明"事后观察、尚未证实"。
- 理由：EXP-V1-03 的 bootstrap 置信区间全部重叠，说明"相关性反转"无法排除随机波动；
  EXP-V1-04 的"方向一致性"同样来自事后观察。
- 状态：**已确认（项目负责人，2026-09-15）**

---

## 新决策模板

```markdown
## D-XXX <决策标题>

- 日期：
- 决策：
- 理由：
- 已否决的替代方案：
- 影响：
- 状态：已确认 / 待确认 / 已废止（可能被 D-YYY 取代）
```

---

## D-004 研究 skill 安装范围

- 日期：2026-09-16
- 决策：只把 research_codex_skills_v3 中有实质内容的部分装成官方格式 skill：
  research-stack-router、research-state，并新增项目专用 skill
  motor-health-monitor-research（记录本项目的实验契约、证据等级、命名与工作流）。
- 已否决：整包安装约 78 个模板化 skill —— 正文逐字重复、缺少 YAML frontmatter、
  会稀释 skill 路由且违反"只保留能改变决策的信息"这一原则。
- 依据：skill-creator 规范；官方校验脚本对 3 个新 skill 全部返回 Skill is valid!。
- 影响：以后新增 skill 必须先有可区分的 name/description 与实质性内容，
  不得直接复制 V3 模板文件。
- 状态：已确认（2026-09-16）

---

## D-005 研究 skill 套件安装（GitHub 来源）

- 日期：2026-09-16
- 决策：按方向从 GitHub 安装 8 个套件中的**核心科研技能**（共 18 个 skill），
  不整包安装（ARIS 189 / scientific-agent-skills 166 / AI-Research 98 个）。
- 已安装映射（skill → 上游仓库）：
  - nature-experiment-log / nature-statistics / nature-figure / nature-writing / nature-reviewer → Yuan1z0825/nature-skills
  - academic-research-suite → Imbad0202/academic-research-skills-codex
  - research-paper-writing → Master-cai/Research-Paper-Writing-Skills
  - ablation-planner / experiment-plan / analyze-results / result-to-claim → wanshuiyin/Auto-claude-code-research-in-sleep (ARIS)
  - autoresearch-skill（原 0-autoresearch-skill）→ Orchestra-Research/AI-Research-SKILLs
  - paper-spine → WUBING2023/PaperSpine（dist/codex 构建）
  - paper-analyzer → zsyggg/paper-craft-skills
  - experimental-design / statistical-analysis / scientific-visualization / uncertainty-and-units → K-Dense-AI/scientific-agent-skills
- 规范化：7 个 skill 的 Claude 专用 frontmatter 字段（argument-hint / compatibility /
  author / tags / version）已移入 metadata；全部 21 个 skill 通过官方校验器。
- 上游版本（安装时 commit）：
| Yuan1z0825/nature-skills | 2375e0a |
| Imbad0202/academic-research-skills-codex | 3c37ef8 |
| Master-cai/Research-Paper-Writing-Skills | 77e7c2c |
| wanshuiyin/Auto-claude-code-research-in-sleep | 5371f05 |
| Orchestra-Research/AI-Research-SKILLs | 773a529 |
| WUBING2023/PaperSpine | 1a511c4 |
| zsyggg/paper-craft-skills | 3be47a2 |
| K-Dense-AI/scientific-agent-skills | 330c8e7 |

---

## D-006 补充安装 3 个 skill（按必要性判断）

- 日期：2026-09-16
- 决策：补充安装 `experiment-audit`（ARIS）、`research-review`（ARIS）、
  `statistical-power`（K-Dense-AI/scientific-agent-skills）。
- 理由：
  - `experiment-audit`：本项目核心风险是数据泄漏与协议不严，需要独立的审计流程；
  - `research-review`：对应"结果审查 → 假说判定 → 风险审查"的方向级复盘；
  - `statistical-power`：本项目最大硬伤是统计功效不足（22 训练窗口 / 11 正常测试窗口），
    需要量化"到底需要多少数据"。
- 明确不装：
  - google-deepmind/science-skills（生物基因组方向，与振动监测无关）；
  - ARIS `auto-review-loop`（依赖跨模型 CLI，本机为 Codex 单环境）；
  - ARIS 的海报 / 专利 / 投稿类 skill（当前阶段不需要）。
- 规范化：3 个 skill 的 `argument-hint` / `compatibility` 已移入 `metadata`。
- 结果：用户 skill 共 **24 个**，全部通过官方校验器。
- 上游版本：ARIS `5371f05`；K-Dense-AI/scientific-agent-skills `330c8e7`。
- 状态：**已确认（2026-09-16）**

---

## D-007 文献检索使用 Scopus，密钥不入库

- 日期：2026-09-16
- 决策：正式文献检索使用 Scopus Search API（`content/search/scopus`，
  `TITLE-ABS-KEY` 检索），替代此前仅凭 12 篇人工整理文献的做法。
- 安全：API key **不写入任何仓库文件**，仅在本机非仓库路径/环境变量中使用；
  建议项目负责人在本次检索后轮换该 key。
- 结果：扫描报告存于 Master 仓库 `docs/literature/SCOPUS_LITERATURE_SCAN_2026-09-16.md`，
  原始计数 `docs/literature/scopus_counts.csv`；本仓库
  `journal-track/LITERATURE_LANDSCAPE.md` 记录创新性定位。
- 影响：期刊线的贡献定位改为"功效感知 + 批次级独立 + 多层级评价"的方法学方向；
  技术交叉点（Mahalanobis + shrinkage + bearing = 1 篇）稀疏但不作为主要卖点。
- 状态：**已确认（2026-09-16）**

---

## D-008 Layer 3 口径定稿：不确定性来自"划分与样本量"

- 日期：2026-09-17
- 依据：EXP-V1-10（Master 仓库 `experiments/EXP-V1-10-selection-uncertainty.md`），
  其预注册与两份修订均**先于结果提交**；另有 `V1_TO_V2_GATE.md` 与 `FROZEN_PROTOCOL.md` 同时冻结。
- 决策：
  - Layer 3 在论文中统一表述为 **"报告的误报率主要由划分与样本量决定"**；
  - **不得**写成"模型选择过程本身是不确定性的来源"（本实验显示选择准则多数情况下不判别，
    该表述会误导为"选择摇摆"）；
  - **不得**写成"调参把随机波动读成有效"（机制性因果断言，本实验不支持）；
  - 报告规范主张保留：**任何单次划分的性能数字都必须同时报告重采样波动，
    或明确声明未测。**
- 关键数字（证据等级 **B**：单一试验台、单一批次、固定 2 文件测试集）：
  - 50 次重采样中 **92% 存在并列**、**86% 的最小验证误报恰为 0**；
  - 固定测试集下报告的误报率在 **0%–14.29%** 之间波动（SD **4.13 pp**，均值 3.86%）；
  - 只取模态配置的 44 个复制，SD 仍为 3.58 pp；
  - 非参零模型 N1 的测试误报 SD 区间 [0.016, 0.059] 覆盖观察值 0.0413。
- 明确不声称：**数据 / 装置结构导致的稳定性问题**——观察到的模态占比（0.88）
  反而**高于** N1 零模型上界（0.805），方向相反。
- 影响：
  - 会议线的三层故事（划分可靠性 / 模型选择可靠性 / 报告可靠性）**全部有量化证据**；
  - 期刊线的"功效感知"论点增加"划分方差"这一维；
  - V1 到此结束，V2-01（Paderborn 跨体系复现）为下一步。
- 状态：**已确认（2026-09-17）**

---

## D-009 论文主结果句更正 + 会议线定位冻结

- 日期：2026-09-18
- 决策：
  1. 论文定位冻结为**评价可靠性 / 应用方法学**，不主张新算法；
  2. 主结果句改为"名义样本量 ≠ 有效信息量"，**删除**"波动主要由划分组成决定"的表述
     （被 `EXP-V1-10-variance-decomposition.csv` 否证：种子 4.39 pp vs 划分 5.20 pp）；
  3. "约 60 条记录"改为"**80–96 条，依工况而定**"（EXP-V2-02，跨工况 3/4）；
  4. 所有主张必须登记在 `conference-track/CLAIM_EVIDENCE_MAP.md`，未登记者不得写入正文。
- 依据：Master 仓库 EXP-V1-10 / V1-11 / V2-01 / V2-02 与 `docs/literature/PROJECT_VALUE_ASSESSMENT.md`。
- 状态：**已确认（2026-09-18）**
