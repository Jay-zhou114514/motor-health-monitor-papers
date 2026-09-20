#!/usr/bin/env python3
"""Build the ISDMD submission .docx from the official IOP-ConfSer Word template.

Format rules taken from the conference checklist: A4, single column, margins 4.0/2.7/2.5 cm,
Times New Roman throughout, single spacing, no keywords. Author block left as a placeholder.
"""

from __future__ import annotations

import io
import os
import re

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt

TRACK = r'C:\Users\32597\Documents\Codex\2026-09-15\github\motor-health-monitor-papers\conference-track'
MD = os.path.join(TRACK, 'PAPER_v1.0_submission-draft.md')
TEMPLATE = os.path.join(TRACK, 'latex', 'isdmd-template', 'ISDMD 2026 Template',
                        'WordGuidelines', 'WordGuidelines', 'IOP-ConfSer-template.docx')
OUT = os.path.join(TRACK, 'latex', 'PAPER_v1.0_ISDMD.docx')
FIGURE = os.path.join(TRACK, 'figures', 'fig1_three_faces.png')


def read(path):
    with io.open(path, 'r', encoding='utf-8', newline='') as fh:
        return fh.read()


def strip_markup(text: str) -> str:
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'\1', text)
    text = re.sub(r'`([^`]+)`', r'\1', text)
    return text


doc = Document(TEMPLATE)

# keep the section properties (page size, margins, headers) but clear the sample body
body = doc.element.body
for child in list(body):
    if child.tag.endswith('}sectPr'):
        continue
    body.remove(child)

normal = doc.styles['Normal']
normal.font.name = 'Times New Roman'
normal.font.size = Pt(10.5)
normal.paragraph_format.space_after = Pt(6)
normal.paragraph_format.line_spacing = 1.0


def para(text, style=None, align=None, italic=False):
    p = doc.add_paragraph(style=style)
    run = p.add_run(strip_markup(text))
    run.italic = italic
    if align is not None:
        p.alignment = align
    return p


lines = read(MD).split('\n')

# ---- title / authors / abstract from the markdown
title = 'Three Faces of Evaluation Uncertainty in Healthy-Data-Only Bearing Anomaly Detection'
para(title, style='Heading 1', align=WD_ALIGN_PARAGRAPH.CENTER)
para('Author One*, Author Two', align=WD_ALIGN_PARAGRAPH.CENTER)
para('Affiliation, City, Postal Code, Country', align=WD_ALIGN_PARAGRAPH.CENTER)
para('*Corresponding author: name@example.com', align=WD_ALIGN_PARAGRAPH.CENTER, italic=True)

abstract = []
in_abstract = False
for line in lines:
    s = line.strip()
    if s.startswith('## Abstract'):
        in_abstract = True
        continue
    if in_abstract:
        if s.startswith('---') or s.startswith('## '):
            break
        if s:
            abstract.append(s)
para('Abstract', style='Heading 2')
para(' '.join(abstract))

# ---- body
section = None
skip = {'1. Introduction'}  # abstract already emitted
i = 0
while i < len(lines):
    s = lines[i].strip()
    if s.startswith('## '):
        section = s[3:].strip()
        if section.lower() == 'title':
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('---'):
                i += 1
            continue
        if section not in skip:
            para(section, style='Heading 1')
    elif s.startswith('### '):
        para(s[4:].strip(), style='Heading 2')
    elif s.startswith('|'):
        rows = []
        while i < len(lines) and lines[i].strip().startswith('|'):
            rows.append(lines[i])
            i += 1
        cells = [[c.strip() for c in r.strip().strip('|').split('|')] for r in rows]
        header, body_rows = cells[0], cells[2:]
        table = doc.add_table(rows=1, cols=len(header))
        table.style = 'Table Grid'
        for j, cell in enumerate(header):
            table.rows[0].cells[j].text = strip_markup(cell)
        for row in body_rows:
            cells_row = table.add_row().cells
            for j, cell in enumerate(row[:len(header)]):
                cells_row[j].text = strip_markup(cell)
        continue
    elif s and not s.startswith('>') and not re.match(r'^(\d+\.\s|- |---)', s):
        para(s)
        # figure caption placement
        if s.startswith('**Fig. 1'):
            pass
    i += 1

# ---- figure (inserted at the end with the required caption wording)
if os.path.isfile(FIGURE):
    doc.add_paragraph()
    doc.add_picture(FIGURE, width=Inches(6.0))
    para('Figure 1. Three faces of evaluation uncertainty in healthy-data-only bearing anomaly '
         'detection: evaluation scope (a), independent units (b), the healthy/degraded boundary '
         '(c), and the reporting checklist (d).')

doc.save(OUT)
print('wrote', OUT)
