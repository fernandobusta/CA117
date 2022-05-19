#!/usr/bin/env python3

import sys

def contains(chars, s):
    for c in chars:
        if c not in s:
            return False
        s = s.replace(c, '', 1)
    return True


for line in sys.stdin:
    line = line.strip().split()
    chars = line[0].lower()
    s = line[1].lower()
    print(contains(chars, s))
