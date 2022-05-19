#!/usr/bin/env python3

import sys

def nice(line):
    if line.count('n') == 1 and line.count('i') == 1 and line.count('c') == 1 and line.count('e') == 1:
        return line


for line in sys.stdin:
    line = line.strip()
    if nice(line) is not None:
        print(nice(line))
