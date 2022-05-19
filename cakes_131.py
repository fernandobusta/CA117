#!/usr/bin/env python3

import sys

def three_cakes(prices):
    if len(prices) < 3:
        return sum(prices)
    total = sum(prices) - min(prices)
    return total


def get_price(prices):
    total = 0
    while len(prices) > 3:
        #take the three first -> three_cake()
        total += three_cakes(prices[:3])
        prices = prices[3:]
    total += three_cakes(prices)
    return total


for line in sys.stdin:
    prices = [int(n) for n in line.strip().split()]
    prices = sorted(prices)[::-1]
    print(get_price(prices))
