#!/usr/bin/env python3

import sys

def cap(s):
    s = s.replace('m', 'M', 1)
    return s


for line in sys.stdin:
    s = line.strip()
    print(cap(s))
