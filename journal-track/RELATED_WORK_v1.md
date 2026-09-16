# 相关工作 v1（期刊线，2026-09-16）

- 完整综述：Master 仓库 `docs/literature/LIT_REVIEW_v1.md`
- 检索数据：`docs/literature/scopus_counts_combined.csv`、`scopus_top_papers.csv`
- 检索源：Scopus（`TITLE-ABS-KEY`），两轮检索（第二轮修正了关键词碰撞）

## 1. 必须引用的核心文献（DOI 已验证）

| 主题 | 文献 | DOI |
| --- | --- | --- |
| ML 评价中的泄漏与复现危机 | Leakage and the reproducibility crisis in machine-learning-based science (2023, Patterns) | 10.1016/j.patter.2023.100804 |
| 轴承诊断的现实评估（最接近的先行工作） | Towards a more realistic evaluation of ML models for bearing fault diagnosis (2026, MSSP) | 10.1016/j.ymssp.2026.114640 |
| 已定样本量下的评价 | Evaluation of a decided sample size in machine learning applications (2023, BMC Bioinformatics) | 10.1186/s12859-023-05156-9 |
| 泄漏安全基准（Scopus 未收录，需另引） | Leakage-Safe, Reproducible Benchmarking for Vibration-Based Fault Diagnosis (2026, PHME) | 10.36001/phme.2026.v9i1.4924 |
| 跨设备泛化（拥挤方向） | Deep discriminative transfer learning network for cross-machine fault diagnosis (2023, MSSP) | 10.1016/j.ymssp.2022.109884 |

## 2. 关键计量（两轮检索，节选）

| 检索式 | 命中 |
| --- | ---: |
| data leakage ∧ machine learning（排除隐私/联邦） | 992 |
| statistical power ∧ evaluation ∧ machine learning | 69 |
| power analysis ∧ fault diagnosis | 43 |
| bearing-wise / file-wise / recording-level / segment-wise ∧ 诊断 | 13 |
| benchmark ∧ bearing fault diagnosis | 291 |
| failed replication / negative results ∧ ML/异常检测 | 1,894 |

检索方法学发现（建议写入论文方法或脚注）：第一轮关键词检索存在关键词碰撞——
`data leakage` 命中的是隐私泄漏、`power analysis` 命中的是瞬时功率分析；
第二轮通过加限定词与 NOT 修正。这说明该领域的文献计量容易被误读。

## 3. 差距与贡献定位

Gap：现有工作已建立"泄漏会高估性能"的认识（Kapoor 2023；Vieira 2026），
但尚未把 (i) 统计功效、(ii) 评价单元的独立性（文件/批次/设备）、
(iii) 多层级评价协议合并为一套可操作流程；也几乎没有工作公开报告
"单数据集上看似显著、跨批次不复现"的实例。

期刊线贡献草案：

> 提出并示范一套"功效感知 + 单元独立 + 多层级"的状态监测检测器评价协议，
> 并以一个"看似显著但不复现"的实例（EXP-V1-07）说明其对结论的影响。

该定位与两篇先行工作互补：
+
+- Vieira et al. (2026, MSSP，**已读 40 页全文**)：数据泄漏审计 + bearing-wise 划分 + 多标签 + ROC 指标 + 轴承数量影响；面向**有标签分类**，关键词 unsupervised / one-class / anomaly detection / statistical power / sample size **均为 0 命中**；
+- Knap et al. (2026, PHME，**已读全文**)：给出 CWRU+Paderborn 的 6 个固定跨域场景 +
+  recording-level 泄漏安全评估；但不涉及统计功效，也不报告负结果。
+
+因此我们的增量边界是：**功效分析 + 评价单元独立性口径 + 公开报告"看似显著但不复现"的实例**。
+"泄漏安全划分"本身已非新意，不得作为卖点。

## 3.1 arXiv 盲区补充（Scopus 未覆盖）

| 文献 | arXiv |
| --- | --- |
| A statistical approach to estimating sample size of ML models (2026) | 2609.09547 |
| Don't push the button! Exploring data leakage risks in ML and transfer learning (2024) | 2401.13796 |
| LeakageDetector / LeakageDetector 2.0 (2025) | 2503.14723 / 2509.15971 |
| Evaluating reliability in ML models … A systematic review of data leakage (2026) | 2607.11963 |

## 4. 下一步

1. 全文精读上述 5 篇（尤其 2026 MSSP），补齐作者、方法、结论与局限；
2. 补充 Scopus 盲区检索（PHM Society、IEEE Xplore、arXiv）；
3. 把 `LIT_REVIEW_v1.md` 第 8 节的英文 Related Work 草稿并入论文骨架；
4. 补经典 ML 基线（One-Class SVM / Isolation Forest），支撑"简单 vs 现代"的对比。



