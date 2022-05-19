#!/usr/bin/env python3

import sys


def qu(w):
    words = [s for s in w if 'q' in s.lower().replace('qu', '')]
    return words


w = []
for line in sys.stdin:
    line = line.strip()
    w.append(line)

#print results
print(f'Words with q but no u: {qu(w)}')
