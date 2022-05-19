#!/usr/bin/env python3

class BankAccount(object):

    def __init__(b, balance=0):
        b.balance = balance

    def deposit(b, amount):
        b.balance += amount

    def withdraw(b, amount):
        if b.balance >= amount:
            b.balance -= amount

    def __str__(b):
        return (f'Your current balance is {b.balance:.2f} euro')
