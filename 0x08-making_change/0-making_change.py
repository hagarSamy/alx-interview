#!/usr/bin/python3
"""
makeChange
"""


def makeChange(coins, total):
    '''determine the fewest number of coins needed to meet a given amount total.'''
    if total <= 0:
        return 0
    from collections import deque

    # Sort the coins in descending order to try the largest coins first
    coins.sort(reverse=True)
    
    count = 0  # To count the number of coins used
    
    for coin in coins:
        if total == 0:
            break
        # Use as many of the current coin as possible
        if coin <= total:
            num_coins = total // coin
            count += num_coins
            total -= num_coins * coin
    
    # If we can't reach 0, return -1
    return count if total == 0 else -1
