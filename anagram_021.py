#!/usr/bin/env python3

import sys


def isanagram(both):
    first = sorted(both[0])
    second = sorted(both[1])
    return (first == second)


both = []
for words in sys.stdin:
    both = words.strip().split()
    print(isanagram(both))
