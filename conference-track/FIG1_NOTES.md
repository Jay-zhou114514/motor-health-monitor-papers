# Fig. 1 说明与 QA 状态（**已通过**）

生成：`src/make_fig1_concept.py`（matplotlib）
输出：`figures/fig1_three_faces.{png,pdf,svg}`（PNG 600 dpi；PDF/SVG 为矢量主件）

## 面板与主张对应（2×2 布局）

| 面板 | 对应主张 | 关键数字 |
| --- | --- | --- |
| (a) Scope | C8（EXP-V2-03） | within-bearing 0.00% vs bearing-level holdout 40.63%（折 0.4–97.1%） |
| (b) Units | C9（EXP-V2-05/06） | 固定 20 条记录：k=1 SD 23–38 pp；k=4 SD 8–14 pp；3σ RMS 与 iForest 各 6/6；马氏饱和不可检验 |
| (c) Definition | C10（EXP-V2-04） | 5 组规则 SD 极差：PRONOSTIA 2.40 pp、XJTU-SY 5.19 pp |
| (d) Checklist | §3.5 | 五条报告清单 |

## nature-figure 自动化 QA（2026-09-20）

| 检查 | 结果 | 报告 |
| --- | --- | --- |
| `validate_figure.py` | ✅ **19 pass / 2 warn / 0 fail → READY FOR VISUAL QA** | `figures/fig1.validate.txt` |
| `audit_pdf_text.py` | ✅ **PASS**（43 个文本段，最小 6.5 pt ≥ 5 pt） | `figures/fig1.pdftext.txt` |
| `audit_figure_collisions.py` | ✅ **0 fail / 0 warn → PASS** | `figures/fig1.collision.txt` |
| 面板对齐门 | ✅ 已接入并通过（2×2 各面板宽高在 1.5 pt 容差内） | 运行时 |

## 修订过程（记录用）

| 轮次 | 碰撞 fail | 关键改动 |
| --- | ---: | --- |
| 初版 | 69 | 单行三面板、393.7 mm 宽、200 dpi、无矢量可编辑设置 |
| 第 1 次 | 68 | 补 fonttype / SVG / 600 dpi / 183 mm / 对齐门 |
| 第 2 次 | 3 | **改为 2×2**；**文字不再放进填充图形内** |
| 第 3 次 | **0** | 删除压到虚线框与相邻文本的说明行；显式 `format="pdf"/"svg"`；指定 Arial |

**结论**：碰撞数从 69 降到 0 的关键不是参数微调，而是**布局与"文字/图形分离"的设计决定**——
前两次参数微调只降了 1 个，改布局一次降了 65 个。

## 交付状态

**✅ 通过自动化 QA，可进入投稿稿。**
仍需项目负责人做**最终视觉确认**（自动化检查不覆盖"示意图是否表意清楚"与灰度打印可读性）。