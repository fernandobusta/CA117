#!/usr/bin/env python3

import sys

#get rid of the punctuation
def punct(s):
    for ch in s:
        if not ch.isalpha() and not ch.isdigit():
            s = s.replace(ch, '')
    return s


#check if it is a palindrome
def pal(s_joined):
    reversed = s_joined[::-1]
    return (reversed.lower() == s_joined.lower())


for s in sys.stdin:
    s = s.strip()
    s_joined = (punct(s))
    print(pal(s_joined))
