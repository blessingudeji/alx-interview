#!/usr/bin/python3
'''makeChange function.'''
import sys


def makeChange(coins, total):
    '''
    Determine the fewest number of coins needed
    '''
    if total <= 0:
        return 0

    # Initialize the table with sys.maxsize
    table = [sys.maxsize] * (total + 1)
    table[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                change = table[i - coin]
                if change != sys.maxsize and change + 1 < table[i]:
                    table[i] = change + 1

    return table[total] if table[total] != sys.maxsize else -1
