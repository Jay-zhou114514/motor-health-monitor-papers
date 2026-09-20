#!/usr/bin/env python3
"""Shim v7: patch the v2 docx builder directly.

  * output -> PAPER_v1.0_ISDMD_v7.docx
  * collapse the wrapped display formula and use it to trigger the Word equation
  * insert Figure 1 right after the Results heading (was: after the Related Work heading)
  * drop the duplicated "## Figure 1 caption" section carried over from the Markdown
"""

from __future__ import annotations

import io

V2 = (r'C:\Users\32597\Documents\Codex\2026-09-15\github\motor-health-monitor-papers'
      r'\conference-track\tools\md2docx_isdmd2.py')

with io.open(V2, 'r', encoding='utf-8') as fh:
    src = fh.read()


def patch(old, new, label, count=1):
    global src
    assert old in src, f'patch failed: {label}'
    src = src.replace(old, new, count)
    print(f'  ok  {label}')


patch('PAPER_v1.0_ISDMD.docx', 'PAPER_v1.0_ISDMD_v7.docx', 'output name')

patch(
    "lines = read(MD).split('\\n')",
    "text_md = read(MD).replace('20,' + chr(10) + '60)', '20, 60)')\n"
    "text_md = re.sub(r'## Figure 1 caption.*?(?=\\n## )', '', text_md, flags=re.DOTALL)\n"
    "lines = text_md.split('\\n')",
    'formula collapse + drop duplicated caption section',
)

patch(
    "if 'H = clip(max(20, 0.10\u00b7N), 20, 60)' in s and 'swept five variants' in s:",
    "if 'H = clip(' in s:",
    'equation trigger',
)

patch(
    "if section.startswith('4.') and not inserted_figure and os.path.isfile(FIGURE):",
    "if section.startswith('3.') and not inserted_figure and os.path.isfile(FIGURE):",
    'figure moved to the start of the Results section',
)

exec(compile(src, 'md2docx_isdmd_v7', 'exec'))
