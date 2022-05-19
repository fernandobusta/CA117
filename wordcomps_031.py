#!/usr/bin/env python3

import sys

def word_sort(words):
    a = [word for word in words if len(word) == 17]
    b = [word for word in words if len(word) >= 18]
    #get words with 4 a's
    c = []
    for w in words:
        counter = 0
        for letter in w:
            if letter == 'a' or letter == 'A':
                counter += 1
        if counter == 4:
            c.append(w)
    #get 2 or more q's
    d = []
    for w in words:
        counter = 0
        for letter in w:
            if letter == 'q' or letter == 'Q':
                counter += 1
        if counter >= 2:
            d.append(w)
    e = [word for word in words if 'cie' in word]
    #anagrams of 'angle'
    f = []
    for w in words:
        wl = w.lower()
        if 'a' in wl and 'n' in wl and 'g' in wl and 'l' in wl and 'e' in wl and len(wl) == 5 and w != 'angle':
            if w not in f:
                f.append(w)
    return a, b, c, d, e, f


words = []
for word in sys.stdin:
    word = word.strip()
    words.append(word)

lists = word_sort(words)
#print results
print(f'Words containing 17 letters: {lists[0]}')
print(f'Words containing 18+ letters: {lists[1]}')
print(f"Words with 4 a's: {lists[2]}")
print(f"Words with 2+ q's: {lists[3]}")
print(f'Words containing cie: {lists[4]}')
print(f'Anagrams of angle: {lists[5]}')
