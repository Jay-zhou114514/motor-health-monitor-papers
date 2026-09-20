#!/usr/bin/env python3
"""Print the relative order of heading-1 titles, the figure image and its caption."""

from __future__ import annotations

import sys

from docx import Document

path = sys.argv[1]
doc = Document(path)
for i, par in enumerate(doc.paragraphs):
    text = par.text.strip()
    has_image = 'graphicData' in par._p.xml
    is_h1 = par.style.name.startswith('Heading 1')
    is_caption = text.startswith('Figure 1')
    if has_image or is_h1 or is_caption:
        kind = 'IMG' if has_image else ('CAP' if is_caption else 'H1 ')
        print(f'{i:4d} {kind} {text[:64]}')
