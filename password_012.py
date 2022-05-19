#!/usr/bin/env python3

import sys

for line in sys.stdin:
    security = [0, 0, 0, 0]
    line = line.strip()
    for ch in line:
        if ch.islower():
            security[0] = 1
        elif ch.isupper():
            security[1] = 1
        elif ch.isdigit():
            security[2] = 1
        else:
            security[3] = 1
    print(sum(security))
