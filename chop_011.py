#!/usr/bin/env python3

import sys

def chop(s):
    return s[1:-1]


for name in sys.stdin:
    name = name.strip()
    if len(name) > 2:
        print(chop(name))
