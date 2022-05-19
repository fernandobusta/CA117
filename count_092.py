#!/usr/bin/env python3

def count_letters(s, counter=0):
    if s == '':
        return counter
    counter += 1
    return count_letters(s[1:], counter)
