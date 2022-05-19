#!/usr/bin/env python3

def fibonacci(n, previous=None):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
