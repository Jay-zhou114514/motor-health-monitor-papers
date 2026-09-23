# 相关工作 v2：与 conformal / 覆盖率文献的对话（骨架）

- 日期：2026-09-23
- 来源：本地 12 篇 PDF（`manual_pdfs/`）的摘要级摘要（`EXP-V3-04-digests.md`）+
  项目既有文献库（`REFERENCES.md`）。
- **状态：骨架**。每条陈述只依据摘要级材料；正式引用前必须按 `citation-audit` 逐条核对原文
  （本项目反模式第 14 条）。

## 0. 一句话定位

> 阈值校准与覆盖率保证已经是 PHM/过程监测的**活跃议题**（本批 12 篇里 5–6 篇属于该方向），
> 但既有工作止步于**类级（class-conditional）或组级（group-wise）**覆盖；
> **"未见物理单元（整颗轴承/试验台）层面的覆盖率"尚无量化答案**——这正是本文要填的缺口。

## 1. 对话组 A：conformal 与阈值校准（覆盖率保证）

| 文献（本地文件） | 做了什么 | 与本文的关系 |
| --- | --- | --- |
| Diallo, Homri, Dantan（J. Process Control, 2025）`1.pdf` | 把 conformal prediction 与经典阈值法（PCA/AE）比较，重复 10 次随机划分评估 **FAR 稳定性**；给出分位数取整式 | **最近的方法论邻居**：同样关心"误报率可控性"，但对象是过程工业仿真数据，**没有物理单元维度** |
| `3.pdf` | conformal + Temporal Quantile Adjustment（TQA）自适应阈值；比较四种阈值方案；滑动窗口 50 步 | 展示"阈值应随流数据自适应"；本文关心的是**跨单元**而非**跨时间**的失效 |
| `4.pdf` | **类条件（Mondrian 式）conformal**：按故障类别分别取分位，报告每类覆盖率与空集率 | 与我们的 M1（Mondrian）对应：他们按**类别**分组，我们按**物理单元/工况**分组；结论：类别分组有效、单元分组在 3–6 单元/组时无效 |
| `1-s2.0-S0967066126003229` | Windowed symmetric CP：用滑动窗口更新分位数，缓解固定校准集 | 覆盖"时间维"的自适应；本文指出**单元维**的自适应缺乏数据支持 |
| `1-s2.0-S0360544226013897` | 系统研究**误校准（miscalibration）**场景（样本不平衡、域漂移）并评估校准方法 | 与我们"口径/单元/边界"三轴互补：他们从"数据分布场景"出发，我们从"评测与报告口径"出发 |

**本文相对 A 组的增量**：
1. 覆盖率的**条件层级**被显式区分（marginal → group → unit），并给出各层级所需的数据支持；
2. 结论落在**物理单元**（未见轴承）而非类别或仿真域；
3. 提供**覆盖率 vs 单元数 / 目标单元数据量**的量化曲线。

## 2. 对话组 B：组级依赖与单元级划分（最关键的邻居）

| 文献 | 做了什么 | 与本文的关系 |
| --- | --- | --- |
| **almeida et al., 2026（SHM）** | 风电机组轴承：**K=5 组级（group-wise）折**；明确说明**重叠窗口导致统计依赖**；conformal 有限样本修正；报告跨折 mean±std | **本文最重要的对话对象**：他们已经做到"组级覆盖 + 依赖显式处理"，但组 = 物理信号窗口组，**不是"未见物理单元"**；本文补上"单元级"这一层与其数据要求 |

**差异化的三句话（可直接写进 Related Work 结尾）**：
- 他们用组级折处理重叠窗口依赖，我们用**整颗轴承留出**处理单元依赖；
- 他们报告类级/组级覆盖，我们报告**跨单元覆盖率及其 Wilson 区间**；
- 他们给覆盖保证，我们给**"达到该保证需要多少独立单元/多少目标单元数据"**的支持曲线。

## 3. 对话组 C：OOD / 开集诊断与阈值选择

| 文献 | 做了什么 | 与本文的关系 |
| --- | --- | --- |
| `1-s2.0-S0019057826003836` | 未知故障（OOD）检测；阈值 γ 取训练样本 OOD 分数的 **95 分位** | 阈值同样来自训练分布——**与本文 M0 同源**，但未讨论"换单元后阈值是否仍成立" |
| `1-s2.0-S0950705126008166` | 开集 + 增量诊断；训练/测试各 105/45 样本 | 关注"新类别"而非"新单元"；本文指出单元位移是另一类失效 |
| `1-s2.0-S1270963826021346` | OOD 拒识 + risk-coverage 曲线；固定种子 42 的 80/10/10 单次划分 | risk-coverage 与我们"覆盖率"指标同族，但他们只在**固定划分**下评估，未量化划分/单元带来的不确定性 |

**增量**：这三个工作都在"分数分布"层面做阈值或拒识，**没有任何一个报告阈值在未见物理单元上的失效**。

## 4. 对话组 D：误报治理与告警疲劳

| 文献 | 做了什么 | 与本文的关系 |
| --- | --- | --- |
| `Quantifying and mitigating alarm fatigue...` | 汇总大量先例的 FAR/TPR 指标；把误报治理作为工程问题 | 提供"为什么误报率重要"的工程动机；本文补充"报告不实的误报率会让这种治理建立在错误数字上" |

## 5. 对话组 E：时序漂移与重校准

| 文献 | 做了什么 | 与本文的关系 |
| --- | --- | --- |
| `7.pdf` | 时序类别先验漂移；ECE 与后验重校准；bootstrap；固定种子 42 | 处理"时间维"的漂移与校准；本文处理"单元维"；两者可并列作为"校准失效的两个来源" |

## 6. 必须新增到 `REFERENCES.md` 的条目（待逐条 Crossref/DOI 核实）

1. Diallo, Homri, Dantan (2025). *Reducing false alarms in fault detection: a comparative analysis between conformal prediction and classical methods applied to PCA and autoencoders.* Journal of Process Control. `1.pdf`
2. Almeida et al. (2026). *Reliability-constrained maintenance optimization for safety-critical wind turbine bearings.* Structural Health Monitoring.
3. （其余 4–5 篇需从 PDF 首页补全作者/年份/期刊；本批文件中含 `1-s2.0-…`、`3.pdf`、`4.pdf`、`7.pdf` 等匿名文件名）

**核实要求**：从每篇 PDF 首页取 DOI → Crossref 核对作者/标题/年份/期刊 → 写入 `REFERENCES.md` →
在 `CITATION_AUDIT.md` 记录核对结果。

## 7. 论文中可用的三句"对话式"表述（草稿）

1. *Conformal prediction has been applied to fault detection to control false alarms (Diallo et al., 2025; …), with recent work extending it to group-wise folds under overlapping-window dependence (Almeida et al., 2026) and to online recalibration under temporal drift (…).*
2. *These results establish marginal and group-level guarantees. What remains open is the level that matters for deployment: an unseen physical unit.*
3. *We show that at the unit level, global calibration, group-conditional calibration and localized calibration all fail to deliver nominal coverage at the unit counts available in public bearing data, and we quantify how much target-unit data is needed to improve — but not guarantee — it.*

## 8. 待办

1. 补足审计样本（本地 12 篇 → 预注册的 30 篇）；
2. 对 `unknown` 编码项做全文复核（尤其 R5 独立单元数、R4 新增 vs 重采样）；
3. 逐条核实并写入 `REFERENCES.md`；
4. 把本骨架并入正文 §4，替换现有 Related Work 中与 [15][16] 的重复表述。
