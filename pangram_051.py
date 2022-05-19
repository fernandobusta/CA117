#!/usr/bin/env python3

import sys

def ispanagram(line):
    all = set('abcdefghijklmnopqrtsuvwxyz')
    letter = [s.lower() for s in line if s.isalpha()]
    letter = set(letter)
    inter = (all & letter)
    if len(inter) == len(all):
        message = 'pangram'
    else:
        missing = sorted(all - letter)
        message = (f'missing {"".join(missing)}')
    return message


for line in sys.stdin:
    line = line.strip()
    print(ispanagram(line))
