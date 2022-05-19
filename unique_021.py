#!/usr/bin/env python3

import sys

#get rid of punctuation
def punct(text):
    for ch in text:
        if not ch.isalpha() and not ch.isdigit():
            text = text.replace(ch, ' ')
        splitted_text = text.split()
    return splitted_text


#create a dict with all words
def rep(plain):
    words = {}
    for w in plain:
        if w.lower() not in words:
            words[w.lower()] = 1
        else:
            words[w.lower()] += 1
    return words


#getting text from stdin
text = ''
for line in sys.stdin:
    text = text + line


#printing result
plain = (punct(text))
words = (rep(plain))
print(len(words))
