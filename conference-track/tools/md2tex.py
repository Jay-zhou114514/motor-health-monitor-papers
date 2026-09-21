#!/usr/bin/env python3
"""Convert the submission draft (Markdown) into a pdflatex-safe LaTeX skeleton.

Deliberately conservative: pipe tables become tabular, inline code becomes texttt,
and Unicode that pdflatex cannot handle is mapped to LaTeX commands. The output uses the
article class so that a venue template (IOP JPCS / IEEEtran) can be swapped in later.
"""

from __future__ import annotations

import io
import os
import re

SRC = r'<WORKDIR>\Documents\Codex\2026-09-15\github\motor-health-monitor-papers\conference-track\PAPER_v1.0_submission-draft.md'
OUT = r'<WORKDIR>\Documents\Codex\2026-09-15\github\motor-health-monitor-papers\conference-track\latex\PAPER_v1.0.tex'

UNICODE = [
    ('σ', r'$\sigma$'), ('×', r'$\times$'), ('≈', r'$\approx$'), ('≤', r'$\le$'),
    ('≥', r'$\ge$'), ('·', r'$\cdot$'), ('⁵', r'$^{5}$'), ('²', r'$^{2}$'),
    ('–', '--'), ('—', '---'), ('§', r'\S'), ('°', r'$^\circ$'),
    ('μ', r'$\mu$'), ('q̂', r'$\hat{q}$'), ('′', "'"),
]

PREAMBLE = r"""\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage[margin=1in]{geometry}
\usepackage[hidelinks]{hyperref}
\usepackage{enumitem}
\setlist{nosep,leftmargin=*}
\newcommand{\code}[1]{\texttt{#1}}
\title{Three Faces of Evaluation Uncertainty in Healthy-Data-Only Bearing Anomaly Detection}
\author{motor-health-monitor project}
\date{\today}
\begin{document}
\maketitle
"""


def esc(text: str) -> str:
    for bad, good in (('\\', r'\textbackslash{}'), ('&', r'\&'), ('%', r'\%'),
                      ('#', r'\#'), ('$', r'\$'), ('_', r'\_'), ('{', r'\{'), ('}', r'\}')):
        text = text.replace(bad, good)
    return text


def inline(text: str) -> str:
    parts = re.split(r'(`[^`]*`)', text)
    out = []
    for part in parts:
        if part.startswith('`') and part.endswith('`') and len(part) > 2:
            out.append(r'\code{' + esc(part[1:-1]) + '}')
        else:
            piece = esc(part)
            for bad, good in UNICODE:
                piece = piece.replace(bad, good)
            piece = re.sub(r'\*\*([^*]+)\*\*', r'\\textbf{\1}', piece)
            piece = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'\\emph{\1}', piece)
            out.append(piece)
    return ''.join(out)


def table(rows: list[str]) -> str:
    cells = [[c.strip() for c in row.strip().strip('|').split('|')] for row in rows]
    header, sep, body = cells[0], cells[1], cells[2:]
    align = ''.join('r' if c.endswith(':') else 'l' for c in sep)
    out = [r'\begin{table}[t]', r'\centering', r'\small',
           r'\begin{tabular}{' + align + '}', r'\toprule',
           ' & '.join(inline(c) for c in header) + r' \\', r'\midrule']
    for row in body:
        out.append(' & '.join(inline(c) for c in row) + r' \\')
    out += [r'\bottomrule', r'\end{tabular}', r'\end{table}']
    return '\n'.join(out)


with io.open(SRC, 'r', encoding='utf-8', newline='') as fh:
    lines = fh.read().split('\n')

body: list[str] = []
i = 0
skip_title = False
while i < len(lines):
    line = lines[i].rstrip()
    stripped = line.strip()

    if stripped.startswith('|'):
        block = []
        while i < len(lines) and lines[i].strip().startswith('|'):
            block.append(lines[i])
            i += 1
        body.append(table(block))
        continue

    if stripped.startswith('## '):
        heading = stripped[3:].strip()
        if heading.lower() == 'title':
            skip_title = True
            i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1
            if i < len(lines):
                i += 1  # drop the bold title line; it is in \title{}
            while i < len(lines) and not lines[i].strip().startswith('---'):
                i += 1
            continue
        body.append('\\section{' + inline(heading) + '}')
    elif stripped.startswith('### '):
        body.append('\\subsection{' + inline(stripped[4:].strip()) + '}')
    elif stripped.startswith('> '):
        quote = []
        while i < len(lines) and lines[i].strip().startswith('>'):
            quote.append(lines[i].strip()[1:].strip())
            i += 1
        body.append('\\begin{quote}\n' + ' '.join(inline(q) for q in quote) + '\n\\end{quote}')
        continue
    elif re.match(r'^\d+\.\s', stripped):
        items = []
        while i < len(lines) and re.match(r'^\s*\d+\.\s', lines[i]):
            item = re.sub(r'^\s*\d+\.\s*', '', lines[i])
            i += 1
            while i < len(lines) and lines[i].startswith('   ') and not re.match(r'^\s*\d+\.\s', lines[i]):
                item += ' ' + lines[i].strip()
                i += 1
            items.append('  \\item ' + inline(item.strip()))
        body.append('\\begin{enumerate}\n' + '\n'.join(items) + '\n\\end{enumerate}')
        continue
    elif stripped.startswith('- '):
        items = []
        while i < len(lines) and lines[i].strip().startswith('- '):
            item = lines[i].strip()[2:]
            i += 1
            while i < len(lines) and lines[i].startswith('  ') and not lines[i].strip().startswith('- '):
                item += ' ' + lines[i].strip()
                i += 1
            items.append('  \\item ' + inline(item.strip()))
        body.append('\\begin{itemize}\n' + '\n'.join(items) + '\n\\end{itemize}')
        continue
    elif stripped == '---':
        body.append('')
    elif stripped:
        para = [stripped]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(
                r'^(#|\||>|- |\d+\.\s|---)', lines[i].strip()):
            para.append(lines[i].strip())
            i += 1
        body.append(inline(' '.join(para)))
        continue
    i += 1

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with io.open(OUT, 'w', encoding='utf-8', newline='') as fh:
    fh.write(PREAMBLE + '\n' + '\n\n'.join(body) +
             '\n\n\\section*{Bibliography}\n'
             'References are maintained in \\code{REFERENCES.md}; a BibTeX file will be '
             'generated from it when the venue template is applied.\n'
             '\\end{document}\n')
print('wrote', OUT)
