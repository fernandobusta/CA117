#!/usr/bin/env python3

def reverse_list(l, new_list=None):
    if new_list is None:
        new_list = []
    if not l:
        return new_list
    new_list.append(l.pop())
    return reverse_list(l, new_list)
