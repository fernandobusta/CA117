#!/usr/bin/env python3

def swap_unique_keys_values(d):
    values = set()
    new_dic = {}
    for (k, v) in d.items():
        try:
            if not (v in values):
                values.add(v)
                new_dic[v] = k
            else:
                new_dic.pop(v)
        except KeyError:
            pass
    return new_dic
