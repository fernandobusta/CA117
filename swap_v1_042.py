#!/usr/bin/env python3

import sys

def swap_keys_values(d):
    keys = []
    values = []
    for (k, v) in d.items():
        keys.append(k)
        values.append(v)
    i = 0
    new_dic = {}
    while i < len(keys):
        new_dic[values[i]] = keys[i]
        i = i + 1
    return new_dic
