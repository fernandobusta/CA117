#!/usr/bin/env python3

import sys

def nice(line):
    if line.count('n') == 1 and line.count('i') == 1 and line.count('c') == 1 and line.count('e') == 1:
        return line


def order(word):
    seq = []
    for i in word:
        if i == 'n' or i == 'i' or i == 'c' or i == 'e':
            seq.append(i)
    if seq == ['n', 'i', 'c', 'e']:
        return word


for line in sys.stdin:
    line = line.strip()
    if nice(line) is not None:
        if order(nice(line)) is not None:
            print(order(nice(line)))
