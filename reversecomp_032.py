#!/usr/bin/env python3

import sys

w = [line.strip() for line in sys.stdin if len(line) > 5]
x = [i.lower() for i in w]
x.sort()

def binsearch(query, sorted_list):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] < query:
            low = mid + 1
        elif sorted_list[mid] > query:
            high = mid - 1
        else:
            return True
    return False


found = [st for st in w if binsearch(st[::-1].lower(), x)]
print(found)
