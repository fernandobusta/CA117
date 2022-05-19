#!/usr/bin/env python3

import sys

def plural(a, b, word):
    vocal = ['a', 'e', 'i', 'o', 'u']
    ab = a + b
    if b == 'x' or b == 's' or b == 'z' or b == 'o':
        return (word + 'es')
    elif ab == 'ch' or ab == 'sh':
        return (word + 'es')
    elif b == 'f':
        return (word[:len(word) - 1] + 'ves')
    elif ab == 'fe':
        return (word[:len(word) - 2] + 'ves')
    elif b == 'y' and a not in vocal:
        return (word[:len(word) - 1] + 'ies')
    else:
        return (word + 's')


for word in sys.stdin:
    word = word.strip()
    b = word[len(word) - 1]
    a = word[len(word) - 2]
    print(plural(a, b, word))
