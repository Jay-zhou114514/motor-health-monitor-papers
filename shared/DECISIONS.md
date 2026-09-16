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
