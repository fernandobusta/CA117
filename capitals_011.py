#!/usr/bin/env python3

import sys

def cap(s):
    newcap = s.upper()
    s = newcap[0] + s[1:-1] + newcap[len(newcap) - 1]
    return s


for word in sys.stdin:
    if len(word) > 2:
        s = word.strip()
        final = cap(s)
        print(final)
