#!/usr/bin/env python3

import sys

def middle(s):
    ch = int(((len(s) - 1) / 2))
    mid = s[ch]
    return mid


for word in sys.stdin:
    if len(word) % 2 == 0:
        s = word.strip()
        final = middle(s)
        print(final)
    else:
        print('No middle character!')
