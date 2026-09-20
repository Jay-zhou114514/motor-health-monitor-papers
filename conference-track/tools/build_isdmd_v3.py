#!/usr/bin/env python3
"""Patch the v2 docx builder in memory so the display equation becomes a Word equation object,
then run it and write PAPER_v1.0_ISDMD_v3.docx.

The only reason for this shim: the source paragraph is wrapped across lines in the Markdown, so
v2's line-based test never saw the whole formula.
"""

from __future__ import annotations

import io
import re

V2 = r'C:\Users\32597\Documents\Codex\2026-09-15\github\motor-health-monitor-papers\conference-track\tools\md2docx_isdmd2.py'

with io.open(V2, 'r', encoding='utf-8') as fh:
    src = fh.read()

src = src.replace('PAPER_v1.0_ISDMD_v2.docx', 'PAPER_v1.0_ISDMD_v3.docx')
src = src.replace('PAPER_v1.0_ISDMD_v2', 'PAPER_v1.0_ISDMD_v3')

# collapse the wrapped formula before the line split
src = src.replace(
    "lines = read(MD).split('\\n')",
    "text_md = read(MD)\n"
    "text_md = re.sub(r'H = clip\\(max\\(20, 0\\.10\u00b7N\\), 20,\\s*60\\)', "
    "'H = clip(max(20, 0.10\u00b7N), 20, 60)', text_md)\n"
    "lines = text_md.split('\\n')",
)

# trigger on the formula alone, and split the sentence around it
src = src.replace(
    "if 'H = clip(max(20, 0.10\u00b7N), 20, 60)' in s and 'swept five variants' in s:",
    "if 'H = clip(' in s:",
)
src = src.replace(
    "head = s.split('We froze one healthy-phase rule')[0]\n            para(head)",
    "formula = 'H = clip(max(20, 0.10\u00b7N), 20, 60)'\n"
    "            head, tail = s.split('H = clip(')[0].rstrip(' ,'), "
    "'H = clip(' + s.split('H = clip(', 1)[1].split('60)', 1)[1]\n"
    "            para(head)",
)
src = src.replace(
    "para('with H/N \u2264 0.25. We swept five variants of it \u2014 fraction 5/10/20% and floor '\n"
    "                 '10/20/30 \u2014 on two independently collected run-to-failure datasets.')",
    "para('with H/N \u2264 0.25.' + tail)",
)

exec(compile(src, 'md2docx_isdmd3', 'exec'))
