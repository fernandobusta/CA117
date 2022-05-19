#!/usr/bin/env python3

import sys

def order(names):
    up = []
    down = []
    while len(names) > 1:
        min_val = min(names.values())
        key_min = get_key(names, min_val)
        up.append(key_min)
        del(names[key_min])
        key_min = get_key(names, min_val)
        down.append(key_min)
        del(names[key_min])

    if len(names) == 1:
        up.append(get_key(names, min(names.values())))
    return up, down[::-1]


def get_key(names, val):
    for k, v in names.items():
        if val == v:
            return k
    return None


names = {}

for name in sys.stdin:
    name = name.strip()
    names[name] = len(name)

if len(names) == 1:
    print(min(names.keys()))
else:
    up, down = order(names)
    print('{}\n{}'.format('\n'.join(up), '\n'.join(down)))
