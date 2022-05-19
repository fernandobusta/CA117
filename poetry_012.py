#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
max = 0

for x in lines:
    x = x.rstrip('\n')
    if len(x) > max:
        max = len(x)

for x in lines:
    y = x
    y = y.rstrip('\n')
    print(f"{y: ^{max}}")
