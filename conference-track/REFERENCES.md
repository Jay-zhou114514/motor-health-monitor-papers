# 参考文献（全部经 Crossref / arXiv / 既有全文核实）

核实脚本：Master `src/lit_verify_references.py`；元数据快照 `docs/literature/REFERENCES_VERIFIED.csv`。
**未出现在本文件中的文献不得进入正文。**

## A. 评价方法与基准（通用异常检测 / 机器学习）

1. Wu, R., & Keogh, E. J. (2021). Current time series anomaly detection benchmarks are flawed and are creating the illusion of progress. *IEEE Transactions on Knowledge and Data Engineering*. https://doi.org/10.1109/TKDE.2021.3112126
   - 核实：Crossref DOI ✓
2. Kim, S., Choi, K., Choi, H.-S., Lee, B., & Yoon, S. (2021). Towards a rigorous evaluation of time-series anomaly detection. *arXiv:2109.05257*.
   - 核实：arXiv API ✓
3. Sehili, M. E. A., & Zhang, Z. (2023). Multivariate time series anomaly detection: Fancy algorithms and flawed evaluation methodology. *arXiv:2308.13068*.
   - 核实：arXiv API ✓
4. Bouthillier, X., Delaunay, P., Bronzi, M., et al. (2021). Accounting for variance in machine learning benchmarks. *arXiv:2103.03098*.
   - 核实：arXiv API ✓
5. "Why ranking anomaly detection algorithms isn't as reliable as you may think" (2026). *arXiv:2608.04613*.
   - 核实：arXiv API ✓（作者列表需在定稿前补齐）
6. MSAD: A deep dive into model selection for time series anomaly detection (2025). *arXiv:2510.26643*.
   - 核实：arXiv API ✓
7. mTSBench: Benchmarking multivariate time series anomaly detection and model selection at scale (2025). *arXiv:2506.21550*.
   - 核实：arXiv API ✓
8. TAB: Unified benchmarking of time series anomaly detection methods (2025). *arXiv:2506.18046*.
   - 核实：arXiv API ✓
9. PATE: Proximity-aware time series anomaly evaluation (2024). *Proceedings of the ACM SIGKDD Conference*. https://doi.org/10.1145/3637528.3671971
   - 核实：Crossref DOI ✓
10. A problem-oriented taxonomy of evaluation metrics for time series anomaly detection (2026). *Neurocomputing*. https://doi.org/10.1016/j.neucom.2026.134547
    - 核实：Crossref DOI ✓
11. A robust framework for evaluation of unsupervised time-series anomaly detection (2024). *LNCS*. https://doi.org/10.1007/978-3-031-78395-1_4
    - 核实：Crossref DOI ✓
12. Baumann, D., & Baumann, K. (2014). Reliable estimation of prediction errors for QSAR models under model uncertainty using double cross-validation. *Journal of Cheminformatics*. https://doi.org/10.1186/1758-2946-6-10
    - 核实：Crossref DOI ✓（标题以 Crossref 返回为准，定稿前复核）

## B. 故障诊断中的样本量与评价

13. Minimum sample size determination of vibration signals in machine learning approach to fault diagnosis using power analysis (2010). *Expert Systems with Applications*. https://doi.org/10.1016/j.eswa.2010.06.068
    - 核实：Crossref DOI ✓
14. Determination of minimum sample size for fault diagnosis of automobile hydraulic brake system using power analysis (2015). *Engineering Science and Technology, an International Journal*. https://doi.org/10.1016/j.jestch.2014.09.007
    - 核实：Crossref DOI ✓；摘要已读（有监督分类、以准确率为目标）
15. Vieira, J. P., Bauler, V. A., Rosa, R. K., & Silva, D. (2026). Towards a more realistic evaluation of machine learning models for bearing fault diagnosis. *Mechanical Systems and Signal Processing, 258*, 114640. https://doi.org/10.1016/j.ymssp.2026.114640
    - 核实：全文已读（Master `docs/literature/EVIDENCE_MATRIX.md`）
16. Knap, P., Jachymczyk, U., & Lalik, K. (2026). Leakage-safe, reproducible benchmarking for vibration-based fault diagnosis. *PHM Society European Conference, 9*(1), 1–8. https://doi.org/10.36001/phme.2026.v9i1.4924
    - 核实：全文已读（同上）

## C. 本文使用的公开数据集（引用必须指向原始论文/官方源）

17. IMS bearing data — NASA/University of Cincinnati IMS test bed（引用以官方描述为准，定稿前补齐）。
18. Lessmeier, C., Kimotho, J. K., Zimmer, D., & Sextro, W. (2016). Condition monitoring of bearing damage in electromechanical drive systems by using motor current signals of electric motors: A benchmark data set for data-driven classification. *PHM Society European Conference*. —— **Paderborn 数据集的原始论文；定稿前必须核实完整著录**
    - 数据源核实：帕德堡 KAt 数据中心目录（2016 年文件），Zenodo `15845309` 为第三方镜像
19. MFPT / MathWorks bearing fault data set（定稿前补齐官方著录）

## D. 待办（写作前必须清零）

- [ ] 第 5、6、7、8、13、14 项的**作者列表**补齐（arXiv/S2 元数据）
- [ ] 第 17、18、19 项的官方著录补齐并核实
- [ ] 第 12 项标题以 Crossref 返回原文为准复核