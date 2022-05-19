#!/usr/bin/env python3

import sys

def pld(pattern, words):
    #here we will store our winners (they meet requirements of P)
    winners = []
    #get rid of words not equal to the length of pattern
    for w in words:
        if w != len(pattern):
            words.remove(w)

    for w in words:
        i = 0
        while i < len(w) and (w[i] == pattern[i] or pattern[i] == '-'):
            i += 1
        if i == len(w):
            winners.append(w)
    return ', '.join(winners)


st = [s.strip() for s in sys.stdin]
pattern = st[0]
words = st[1:]

print(pld(pattern, words))
