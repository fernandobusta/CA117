#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.lower()
    lines = line.strip().split()
    print(lines[0] in lines[1])
