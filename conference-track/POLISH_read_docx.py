#!/usr/bin/env python3
"""Extract readable text (paragraphs + tables) from the recommended-conferences docx."""

from __future__ import annotations

import io
import os
import re
import zipfile

DOCX = r'C:\Users\32597\Desktop\会议推荐.docx'
OUT = r'C:\Users\32597\Documents\Codex\2026-09-15\github\motor-health-monitor-papers\conference-track\会议推荐_提取.txt'

with zipfile.ZipFile(DOCX) as zf:
    names = zf.namelist()
    xml = zf.read('word/document.xml').decode('utf-8', 'replace')

print('docx parts:', [n for n in names if n.startswith('word/')][:10])

# paragraph boundaries -> newlines; table cells -> tabs
text = xml
text = text.replace('</w:p>', '\n')
text = text.replace('</w:tc>', '\t')
text = re.sub(r'<w:tab[^>]*/>', '\t', text)
text = re.sub(r'<w:br[^>]*/>', '\n', text)
text = re.sub(r'<[^>]+>', '', text)
text = text.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
lines = [ln.rstrip() for ln in text.split('\n')]
lines = [ln for ln in lines if ln.strip()]

body = '\n'.join(lines)
with io.open(OUT, 'w', encoding='utf-8', newline='') as fh:
    fh.write(body)
print('extracted lines:', len(lines))
print('---')
print(body[:4000])
