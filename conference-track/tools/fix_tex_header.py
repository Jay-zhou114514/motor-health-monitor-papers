#!/usr/bin/env python3
"""Drop the Chinese front-matter that md2tex.py carried into the LaTeX body, and strip any
remaining CJK so that pdflatex can compile. The LaTeX \title block already carries the title."""

from __future__ import annotations

import io
import re

TEX = r'<WORKDIR>\Documents\Codex\2026-09-15\github\motor-health-monitor-papers\conference-track\latex\PAPER_v1.0.tex'

with io.open(TEX, 'r', encoding='utf-8', newline='') as fh:
    text = fh.read()

anchor = text.index(r'\maketitle') + len(r'\maketitle')
first_section = text.index(r'\section{', anchor)
dropped = text[anchor:first_section]
text = text[:anchor] + '\n' + text[first_section:]

before = len(re.findall(r'[\u3000-\u9fff\uff00-\uffef]', text))
text = re.sub(r'[\u3000-\u9fff\uff00-\uffef]+', ' ', text)
after = len(re.findall(r'[\u3000-\u9fff\uff00-\uffef]', text))

with io.open(TEX, 'w', encoding='utf-8', newline='') as fh:
    fh.write(text)

print(f'dropped {len(dropped)} chars of front matter; CJK removed: {before} -> {after}')
