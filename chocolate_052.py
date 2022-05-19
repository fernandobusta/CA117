#!/usr/bin/env python3

import sys

def calories(kcals):
    bar = 400
    n = kcals // bar
    if kcals % bar:
        n += 1
    return n


for line in sys.stdin:
    kcals = int(line.strip())
    print(calories(kcals))
