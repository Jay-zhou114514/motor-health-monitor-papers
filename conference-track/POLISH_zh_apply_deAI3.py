#!/usr/bin/env python3
"""Final mechanical part of the humanizer-zh pass: no em dashes left, no decorative bold
on negations. Both are category-level rules from the skill, so they do not need exact strings."""

from __future__ import annotations

import io
import os
import re

ZH = os.path.join(
    r'<WORKDIR>\Documents\Codex\2026-09-15\github\motor-health-monitor-papers',
    'conference-track', 'PAPER_v1.0_中文版.md',
)

with io.open(ZH, 'r', encoding='utf-8', newline='') as fh:
    text = fh.read()

# 1. em dashes: the skill forbids them in the final text unless the author's sample uses them
before = text.count('——')
text = re.sub(r'\s*——\s*', '；', text)
print(f'em dashes replaced: {before} -> {text.count("——")}')

# 2. decorative bold around negation particles and a few pure emphasis words
unbolded = 0
for token in ('**不是**', '**并非**', '**首先**', '**也是**', '**同样**', '**只**'):
    count = text.count(token)
    if count:
        text = text.replace(token, token.strip('*'))
        unbolded += count
print(f'decorative bold removed: {unbolded}')

with io.open(ZH, 'w', encoding='utf-8', newline='') as fh:
    fh.write(text)

print('remaining em dashes:', text.count('——'))
print('remaining bold spans:', len(re.findall(r'\*\*[^*]{1,20}\*\*', text)))
