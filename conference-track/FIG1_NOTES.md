# Fig. 1 说明与 QA 状态

生成：`src/make_fig1_concept.py`（matplotlib）
输出：`figures/fig1_three_faces.{png,pdf,svg}`（PNG 600 dpi；PNG/PDF/SVG 三格式）

## 面板与主张对应

| 面板 | 对应主张 | 关键数字 |
| --- | --- | --- |
| (a) Scope | C8（EXP-V2-03） | within-bearing 0.00% vs bearing-level holdout 40.63% |
| (b) Units | C9（EXP-V2-05/06） | 固定 20 条记录：k=1 SD 23–38 pp；k=4 SD 8–14 pp；RMS 与 iForest 各 6/6；马氏饱和不可检验 |
| (c) Definition | C10（EXP-V2-04） | 5 组规则 SD 极差：PRONOSTIA 2.40 pp、XJTU-SY 5.19 pp |

## nature-figure 自动化 QA 结果（2026-09-20）

按 `nature-figure` skill 的规范执行三项自动化检查。**这些检查替代了生成方无法完成的视觉检查。**

| 检查 | 命令 | 结果 |
| --- | --- | --- |
| 源码规范 | `validate_figure.py` | **19 pass / 1 warn / 1 fail → FIX BEFORE DELIVERY** |
| PDF 字体 | `audit_pdf_text.py` | ✅ **PASS**（最小 7 pt ≥ 5 pt，66 个文本段全部达标） |
| 几何重叠 | `audit_figure_collisions.py` | ❌ **68 fail / 14 warn → FIX BEFORE DELIVERY** |

### 已修复项（本轮由 QA 发现）

| 检查项 | 原状态 | 现状 |
| --- | --- | --- |
| EDITABLE-TEXT | ❌ 缺 `svg.fonttype`/`pdf.fonttype` | ✅ 已按字典写法配置 |
| EXPORT-VECTOR | ❌ 缺 SVG | ✅ PNG+PDF+SVG 三格式 |
| RASTER-DPI | ❌ 200 dpi | ✅ 600 dpi |
| FINAL-WIDTH | ❌ 393.7 mm | ✅ **182.9 mm**（期刊双栏宽度） |
| PANEL-ALIGNMENT-GATE | ❌ 未接对齐门 | ✅ 已接入并通过（三面板宽高在容差内） |

### 尚未修复（**必须在下一次迭代解决**）

**`audit_figure_collisions` 报 68 fail / 14 warn**，类型集中于 `text-fill-edge`：
**示意图内的文字与方框边缘重叠**（如 `#1`–`#6` 等标签、`5555`、`SD ≈ 8–14 pp`）。

根因判断：图从 393 mm 压到期刊宽度 183 mm 后，**方框按比例缩小但文字为固定磅值**，
文字与图形的比例失衡。两次参数微调仅把 fail 从 69 降到 68，
**说明这是设计问题而非参数问题**。

**建议的下一步（不要继续盲调）**：
按 `nature-figure` 的 `references/multipanel-evidence-architecture.md` 重新设计——
可选方案：① 改为 **2 行 × 2 列**布局以获得更大的单面板宽度；
② 把说明性文字移出图形（改为图注）；③ 减少单面板内的示意图元素数量。

## 交付状态

**❌ 未通过交付前检查，不得进入投稿稿。**
本图此前被标为"待人工视觉检查"；**现在有了更硬的结论：自动化 QA 已判定它不合格**，
且不合格原因是生成方无法看到的结构缺陷。