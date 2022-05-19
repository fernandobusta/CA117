#!/usr/bin/env python3

import sys

def count_vowelss(text):
    vowelss = {'a': 0,
               'e': 0,
               'i': 0,
               'o': 0,
               'u': 0}

    for i in text:
        if i in vowelss:
            vowelss[i] += 1
    return vowelss


text = ''
for line in sys.stdin:
    line = line.strip().lower()
    text += line

#sort the values from high to low
vowelss = count_vowelss(text)
def tagger(item):
    return item[1]


#find width of the widest value
max_width = len(str(max(vowelss.values())))

#print results
for k, v in reversed(sorted(vowelss.items(), key=tagger)):
    print(f'{k} : {v:>{max_width}}')
