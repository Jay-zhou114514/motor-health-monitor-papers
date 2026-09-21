#!/usr/bin/env python3
"""Wrap stray superscripts in math mode and escape remaining ^ and ~ so pdflatex compiles clean."""

from __future__ import annotations

import io
import re

TEX = r'<WORKDIR>\Documents\Codex\2026-09-15\github\motor-health-monitor-papers\conference-track\latex\PAPER_v1.0.tex'

with io.open(TEX, 'r', encoding='utf-8', newline='') as fh:
    text = fh.read()

before = text.count('^')
# 10^5, SD^2, 10^5-fold, etc. -> math mode
text = re.sub(r'(\d)\^(\{?\d+\}?)', r'\1$^{\2}$', text)
text = re.sub(r'([A-Za-z])\^(\{?\d+\}?)', r'\1$^{\2}$', text)
# any leftover caret or tilde
text = text.replace('^', r'\textasciicircum{}')
text = text.replace('~', r'\textasciitilde{}')

with io.open(TEX, 'w', encoding='utf-8', newline='') as fh:
    fh.write(text)

print(f'carets before={before} after={text.count("^")}')
