#!/usr/bin/env python3

import sys

def lists(words):
    vowels = [w for w in words if 'a' in w and 'e' in w and 'i' in w and 'o' in w and 'u' in w]
    shortest = min(vowels, key=len)
    end_iary = [w for w in words if w[-4:] == 'iary']
    iary = len(end_iary)
    #max e
    w_e = {}
    for w in words:
        w_e[w] = 0
        for i in w:
            if i == 'e':
                w_e[w] += 1
    max_e = max(w_e.values())
    most_e = [w for w in w_e if w_e[w] == max_e]
    return shortest, iary, most_e


words = []
for line in sys.stdin:
    words.append(line.strip())

values = (lists(words))
#print results
print(f'Shortest word containing all vowels: {values[0]}')
print(f'Words ending in iary: {values[1]}')
print(f"Words with most e's: {values[2]}")
