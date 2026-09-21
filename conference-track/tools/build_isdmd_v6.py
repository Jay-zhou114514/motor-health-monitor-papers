#!/usr/bin/env python3
"""Shim v6: put Figure 1 at the end of the Results section and drop the duplicated caption section."""

from __future__ import annotations

import io

V4 = (r'<WORKDIR>\Documents\Codex\2026-09-15\github\motor-health-monitor-papers'
      r'\conference-track\tools\build_isdmd_v4.py')

with io.open(V4, 'r', encoding='utf-8') as fh:
    src = fh.read()

# v4 already targets v4.docx; point it at v6
src = src.replace('PAPER_v1.0_ISDMD_v4.docx', 'PAPER_v1.0_ISDMD_v6.docx')
assert 'ISDMD_v6' in src

# 1. insert the figure before the "4." heading instead of after it
old_heading = ("        if section != '1. Introduction':\n"
               "            para(section, style='Heading 1')\n"
               "        if section.startswith('4.') and not inserted_figure and os.path.isfile(FIGURE):\n")
new_heading = ("        if section.startswith('4.') and not inserted_figure and os.path.isfile(FIGURE):\n"
               "            doc.add_picture(FIGURE, width=Inches(6.0))\n"
               "            para('Figure 1. Three faces of evaluation uncertainty in "
               "healthy-data-only bearing anomaly detection: evaluation scope (a), independent "
               "units (b), the healthy/degraded boundary (c), and the reporting checklist (d).')\n"
               "            inserted_figure = True\n"
               "        if section != '1. Introduction':\n"
               "            para(section, style='Heading 1')\n"
               "        if False and not inserted_figure and os.path.isfile(FIGURE):\n")
assert old_heading in src, 'heading/figure block not found'
src = src.replace(old_heading, new_heading, 1)

# 2. drop the duplicated caption section from the markdown before it is parsed
src = src.replace(
    "text_md = read(MD).replace('20,' + chr(10) + '60)', '20, 60)')",
    "text_md = read(MD).replace('20,' + chr(10) + '60)', '20, 60)')\n"
    "text_md = re.sub(r'## Figure 1 caption.*?(?=\\n## )', '', text_md, flags=re.DOTALL)",
)

exec(compile(src, 'md2docx_isdmd_v6', 'exec'))
