#!/usr/bin/env python3
"""Shim v4: patch the v2 builder (output name, wrapped formula, equation trigger) and run it."""

from __future__ import annotations

import io

V2 = (r'C:\Users\32597\Documents\Codex\2026-09-15\github\motor-health-monitor-papers'
      r'\conference-track\tools\md2docx_isdmd2.py')

with io.open(V2, 'r', encoding='utf-8') as fh:
    src = fh.read()

before = src
src = src.replace('PAPER_v1.0_ISDMD.docx', 'PAPER_v1.0_ISDMD_v4.docx')
assert src != before, 'output name not replaced'

before = src
src = src.replace(
    "lines = read(MD).split('\\n')",
    "text_md = read(MD).replace('20,' + chr(10) + '60)', '20, 60)')\n"
    "lines = text_md.split('\\n')",
)
assert src != before, 'formula collapse not inserted'

before = src
src = src.replace(
    "if 'H = clip(max(20, 0.10\u00b7N), 20, 60)' in s and 'swept five variants' in s:",
    "if 'H = clip(' in s:",
)
assert src != before, 'equation trigger not replaced'

exec(compile(src, 'md2docx_isdmd_v4', 'exec'))
