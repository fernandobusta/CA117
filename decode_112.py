#!/usr/bin/env python3

import sys

def breaker(line):
    vowel = ['a', 'e', 'i', 'o', 'u']
    i = 0
    while i < len(line):
        if line[i] in vowel:
            line = line[:i] + line[i + 2:]
        i += 1
    return line


for line in sys.stdin:
    line = line.strip()
    print(breaker(line))
