#!/usr/bin/env python3

import sys
import string
unique_words = []

for line in sys.stdin:
    new_line = []
    line = line.strip().split()
    for word in line:
        only_letters = word
        for i in word:
            if i in string.punctuation:
                only_letters = word.replace(i, '')
        if only_letters.lower() not in unique_words:
            unique_words.append(only_letters.lower())
            new_line.append(word)
        else:
            new_line.append('.')
    print(' '.join(new_line))
