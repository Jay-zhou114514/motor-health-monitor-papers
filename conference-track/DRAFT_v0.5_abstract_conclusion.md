# Draft v0.5 — Abstract and Conclusion

> 按 `nature-writing` skill 起草。轴值：task=manuscript｜paper_type=methods（见 §Assumptions）｜
> section=abstract + conclusion｜language=zh-to-en｜journal=generic
> **简化加载声明**：本次只加载 stance / output-format / section:abstract / section:conclusion / paper_type:methods
> 五个片段；manifest 的 7 个 `always_load` 共享层文件未加载（上下文限制），写作时以项目既有纪律替代。

---

## Abstract

Condition monitoring is frequently deployed where only healthy-machine data are
available: a detector is fitted on healthy recordings, the alarm threshold is placed at a
quantile of the training score distribution, and the reported false-alarm rate is the
number that decides whether the monitor is usable. We ask how far that number can be
trusted and what determines it. Using four public bearing datasets under a pre-registered
protocol, we find that the reported false-alarm rate is governed less by the detector than
by three analyst choices. Holding out whole bearings, rather than only held-out recordings,
raised the same detector's false-alarm rate from 0.00% to 40.63%. At a fixed sample size,
increasing the number of distinct training bearings reduced the spread of the reported rate
for two of three detectors (6 of 6 conditions each), whereas the third saturated and could
not be evaluated this way. Moving the healthy/degraded boundary — a choice that
run-to-failure data leave to the analyst — shifted the reported uncertainty by 2.4–5.2
percentage points, with the same rule binding on opposite sides in different datasets. We
give a five-point reporting checklist and state where each claim stops.

*(≈175 words)*

---

## Conclusion

The practical reliability of a false-alarm rate in healthy-data-only bearing anomaly
detection is set less by the detector than by three choices the analyst makes: whether
evaluation keeps physical units apart, how many independent units enter training, and
where healthy data end. Each was quantified here on more than one dataset, with the
boundary of each claim stated alongside it.

The decisive evidence is comparative rather than absolute. Holding out whole bearings moved
the reported rate by an order of magnitude (0.00% to 40.63%) on the same detector and the
same data. At a fixed sample size, adding distinct training bearings halved the spread of
the reported rate for two detectors, while the third saturated at 67–100% false alarms and
therefore became uninformative rather than unstable. Sweeping the healthy/degraded boundary
moved the reported uncertainty by 2.4–5.2 percentage points without any change to the
detector.

The implication is bounded but immediate for reporting practice: a study that reports a
single within-bearing number may present a detector with a 40% false-alarm rate as having
none, and a study that does not disclose its healthy/degraded boundary may present a number
that moves by several percentage points under a defensible alternative. The five-point
checklist in §3.5 addresses these cases without requiring new models or additional data.

We do not claim a new detector, a new method for locating degradation onset, or generality
beyond the rigs studied. All evidence is from public datasets; none comes from our own
hardware, and a prospective self-collected study is the natural next test.

---

## 中文说明（结构性选择）

1. **摘要开头不写 "Here, we"**——按 skill 的诊断规则，那通常意味着背景缺失；改为先立场景（只有健康数据可用）。
2. **摘要只留一个主论断**（"三个分析者选择决定可信度"），支撑证据压到三条，且每条都带边界或数字。
3. **结论用"贡献 → 决定性证据 → 应用 → 边界"四段**，且最后一段主动否认三类过度主张（新检测器 / 新起点检测法 / 跨设备泛化）。
4. **应用范围写得比证据窄**：只说"对报告实践"有直接影响，不说"提升了检测性能"。