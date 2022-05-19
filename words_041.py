#!/usr/bin/env python3

import sys
import string

def words(s):
    punct = []
    word_count = {}
    #find the punctuation
    for i in s:
        if i in string.punctuation and i != "'":
          s = s.replace(i, " ")
    tokens = s.split()
    #assigning values to each word
    for w in tokens:
        if w not in word_count:
            word_count[w] = 1
        else:
            word_count[w] += 1
    return sorted(word_count.items())


#collecting data from input
s = ""
for line in sys.stdin:
    line = line.strip().lower()
    s = s + " " + line

#print result
for i in words(s):
    print(f'{i[0]} : {i[1]}')
