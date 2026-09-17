# Conference Track 状态

更新日期：2026-09-15

## 当前进度

| 项目 | 状态 |
| --- | --- |
| Baseline（EXP-V1-00） | 已完成 |
| 阈值敏感性（EXP-V1-01） | 已完成 |
| 特征消融（EXP-V1-02） | 已完成 |
| 误差定位与依赖结构验证（EXP-V1-03） | 已完成 |
| 良态特征集受控对照（EXP-V1-04） | 已完成，审查通过（2026-09-15） |

## 投稿门槛评估

| 门槛 | 是否满足 | 说明 |
| --- | --- | --- |
| 核心研究问题明确 | 基本满足 | 问题聚焦"为什么误报"，但机制表述仍在收敛 |
| 核心实验闭环 | **未满足** | 需要 V1-04 的正式判定与结论收敛 |
| 能解释现象/机制 | 部分满足 | 现有机制为 Level B，尚未达到"已证明" |
| 可复现 | 满足 | 脚本、日志、CSV、图均已入库 |
| 诚实区分证据等级 | 满足 | 采用 A/B/C/D 分级与谨慎表述 |

**结论：尚未达到会议投稿门槛。** 核心实验闭环需等待 EXP-V1-05 的结果。

EXP-V1-04 与 EXP-V1-05 的结果审查、假说判定与风险审查均已于 2026-09-15 完成（EXP-V1-05 判定为 B）；
会议线计划已更新为 v1.1，V1-05 锁定为 Covariance Geometry & Regularization。

## 下一步动作

1. 执行 EXP-V1-06-A：预注册"标准化投影幅度"指标后，在三折正常文件轮换中验证 H1。
2. 执行 EXP-V1-06-B：比较预定义 training-only 准则选择收缩强度 δ（测试集最后打开一次）。
3. 届时重新评估投稿门槛。



---

## 2026-09-16 更新

- EXP-V1-06 完成并通过确定性证据预检（21/21 引用数字一致）。
- 功效分析：H1 功效仅 0.087（需约 29 个正常文件）→ 判定改为"功效不足、无法判定"；
  H2 功效 0.180，效应 dz≈1.0，需约 10 个正常文件。
- 会议核心故事转为"距离膨胀 + 收缩缓解 + 功效不足≠被反驳"。
- 投稿门槛：由"未满足"调整为"基本满足"（单数据集版本可投稿；跨数据集验证会更强）。
- 下一步：EXP-V1-07（H2 跨数据集验证）。

---

## 2026-09-17 更新：EXP-V1-10 完成，三层故事全部有量化证据

### 实验进度（截至 2026-09-17）

| 实验 | 结果 | 在论文中的位置 |
| --- | --- | --- |
| EXP-V1-07 跨批次验证 | **1/27 折复现**（MFPT 1/3、IMS 0/24） | Layer 1：单折机制不可升级为一般结论 |
| EXP-V1-08 单类基线 | 3σ RMS 2.4%；OC-SVM 27–50% | Layer 2 起点 |
| EXP-V1-09 训练内超参 | iForest 3/3 达标、OC-SVM 0/3；**搜索成本 ≈ 10⁵ 倍**；模态占比 33% | Layer 2 |
| **EXP-V1-10 选择过程不确定性** | **92% 并列、86% 最小验证误报为 0；报告的误报率 0%–14.29%（SD 4.13 pp）** | **Layer 3** |

### 投稿门槛重新评估

| 门槛 | 是否满足 | 说明 |
| --- | --- | --- |
| 核心研究问题明确 | **满足** | "小样本、仅健康数据的轴承异常检测实验，结论有多可靠？" |
| 核心实验闭环 | **基本满足** | 三层各有预注册实验与产物；Layer 3 量化完成 |
| 能解释现象 | 满足（有限定） | 统一表述：**报告的误报率主要由划分与样本量决定** |
| 可复现 | 满足 | 脚本 / 日志 / CSV / 图全部入库，含可断点续跑实现 |
| 诚实区分证据等级 | 满足 | Level B；探索性检查标注为 Level C |
| 跨体系证据 | **未满足** | 只有 IMS（同试验台 3 批次）+ MFPT；需 V2-01（Paderborn） |

**结论：会议线的最小完整闭环已经具备，但"跨体系"仍是明显缺口。**
建议按 `V1_TO_V2_GATE.md` 先完成 G4（Paderborn 独立单元与许可核实 + V2-01 预注册），
再决定是"先投会议、同时补 V2"还是"等 V2-01 完成再投"。

### 论文的主结果句（措辞已按证据限定）

> With 10 healthy recordings, the selected configuration was indistinguishable in 92% of
> resamples, while the reported false-alarm rate varied between 0% and 14.3%
> (SD ≈ 4 pp) purely as a function of which recordings entered the training set.

### 下一步

1. **G4**：核实 Paderborn（Zenodo `15845309`，K001–K006）的独立单元定义、许可与获取方式；
2. 写 V2-01 预注册（跨体系复现：三层结论是否在另一试验台成立）；
3. 更新 `PAPER_OUTLINE.md`：Layer 3 的图表与结论按 EXP-V1-10 结果落位。

---

## 2026-09-18 更新：证据链完成，论文定位与主结果句已更正

**新增证据（Master 仓库）**：EXP-V1-10（选择过程不确定性）、方差分解、EXP-V1-11（样本量标度）、
**EXP-V2-01（Paderborn，名义 n vs 有效信息）**、EXP-V2-02（跨 4 工况稳健性）。

**门槛重新评估**：

| 门槛 | 状态 | 说明 |
| --- | --- | --- |
| 核心研究问题明确 | 满足 | 报告的误报率能不能信、要多大的健康样本 |
| 核心实验闭环 | **满足** | V1 三层 + V2 两个实验，全部有预注册与产物 |
| 能解释现象 | 满足（有限定） | 噪声下限 + 名义/有效样本量 |
| 可复现 | 满足 | 脚本 / 日志 / CSV / 图 + 断点续跑 |
| 诚实区分证据等级 | 满足 | Level B，探索性标 Level C |
| 跨体系证据 | **基本满足** | IMS + Paderborn（两个试验台、四个工况），但仅 6 个物理轴承 |

**主结果句（已更正——旧句被方差分解否证）**

> With ten healthy recordings, the training-internal selection criterion was
> non-discriminative in 92% of resamples, and the reported false-alarm rate varied
> between 0% and 14.3% (SD ≈ 4 pp). Increasing the nominal training size by resampling
> the same recordings did not reduce this uncertainty (SD 18.0 pp at n = 96), whereas
> using 96 *distinct* recordings reduced it to 0.0 pp; across four operating conditions,
> the direction held in 3/4 and the required number of recordings was 80–96.

**旧句（禁止再用）**："…purely as a function of which recordings entered the training set."
理由：方差分解显示随机种子来源的 SD 为 4.39 pp，与划分来源 5.20 pp 量级相当。

**下一步**：按 `CLAIM_EVIDENCE_MAP.md` 与 `PAPER_OUTLINE.md` 进入写作（先补 Fig. 1 概念图）。
