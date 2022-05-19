#!/usr/bin/env python3

import sys

def isprime(n):
    prime = []
    for a in range(2, n + 1):
        for i in range(2, 12):
            if i != a and a % i == 0:
                f = 1
                break
            else:
                f = 0
        if f == 0:
            prime.append(a)
    return prime


for n in sys.stdin:
    n = int(n.strip())
    print(f'Primes: {isprime(n)}')
