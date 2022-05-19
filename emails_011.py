#!/usr/bin/env python3

import sys

def name(s):
    ch = s
    i = 0
    while ch[i] != '.':
        i += 1
    first_name = ch[:i].capitalize()
    last_name = ch[i + 1:].capitalize()
    return (first_name + ' ' + last_name)


for email in sys.stdin:
    tokens = email.strip()
    j = 0
    while tokens[j].isdigit() is not True:
        j += 1
    s = email[:j]
    print(name(s))
