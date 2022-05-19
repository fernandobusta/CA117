#!/usr/bin/env python3

import sys

def upper(line):
    for s in line:
        if s.islower():
            line = line.replace(s, ' ')
    seq = line.split()
    return max(seq)


for line in sys.stdin:
    line = line.strip()
    print(upper(line))
