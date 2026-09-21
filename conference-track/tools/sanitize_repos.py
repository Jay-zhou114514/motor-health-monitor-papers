#!/usr/bin/env python3
"""Remove personal identifiers and Red-Bird (红鸟) references from tracked text files.

Handles: local Windows path with the account name, the GitHub account handle, and every
mention of the 红鸟 programme. Dates are deliberately NOT touched: they are the evidence that
pre-registration preceded the runs, and the frozen protocol forbids rewriting them.
"""

from __future__ import annotations

import io
import os
import re
import subprocess

REPOS = [r'C:\Users\32597\Documents\Codex\2026-09-06\github\motor-health-monitor',
         r'C:\Users\32597\Documents\Codex\2026-09-15\github\motor-health-monitor-papers']
BINARY_EXT = {'.png', '.jpg', '.jpeg', '.gif', '.pdf', '.doc', '.docx', '.rar', '.zip',
              '.pyc', '.xlsx', '.ico', '.pfb', '.pkl', '.npy'}

TEXT_REPLACEMENTS = [
    (r'C:\\Users\\32597', r'<WORKDIR>'),
    (r'C:/Users/32597', r'<WORKDIR>'),
    (r'32597', r'<user>'),
    (r'Jay-zhou114514', r'<ACCOUNT>'),
    (r'红鸟挑战营', r''),
    (r'红鸟硕士项目', r''),
    (r'红鸟展示项', r'展示项'),
    (r'红鸟/申请展示项', r'申请展示项'),
    (r'红鸟/申请', r'申请'),
    (r'红鸟', r''),
]


def tracked(repo):
    out = subprocess.run(['git', '-C', repo, 'ls-files'], capture_output=True, text=True)
    return [line.strip() for line in out.stdout.splitlines() if line.strip()]


changed_total = 0
for repo in REPOS:
    print(f'=== {os.path.basename(repo)} ===')
    for rel in tracked(repo):
        path = os.path.join(repo, rel)
        if not os.path.isfile(path) or os.path.splitext(path)[1].lower() in BINARY_EXT:
            continue
        try:
            with io.open(path, 'r', encoding='utf-8', newline='') as fh:
                original = fh.read()
        except UnicodeDecodeError:
            continue
        text = original

        # drop whole lines that exist only to describe the application programme
        kept = [ln for ln in text.split('\n')
                if '红鸟' not in ln or ('展示项' in ln or 'A+C' in ln)]
        text = '\n'.join(kept)

        # drop the dedicated section if one exists
        text = re.sub(r'\n## 红鸟[^\n]*\n.*?(?=\n## |\Z)', '\n', text, flags=re.DOTALL)

        for pattern, repl in TEXT_REPLACEMENTS:
            text = re.sub(pattern, repl, text)

        # tidy the artefacts of deleting the programme name inside sentences
        text = text.replace('自采作展示项', '自采作展示项').replace('（A+C 决定：自采作展示项，不进本论文）',
                                                        '（A+C 决定：自采数据不进本论文）')
        text = re.sub(r'[ \t]+\n', '\n', text)

        if text != original:
            with io.open(path, 'w', encoding='utf-8', newline='') as fh:
                fh.write(text)
            changed_total += 1
            print(f'  sanitized {rel}')
print(f'\ntotal files changed: {changed_total}')
