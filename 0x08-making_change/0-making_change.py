#!/usr/bin/python3

""" Contains makeChange function"""


def makeChange(coins, total):
    """
    Return: lest number of coins that we needed to meet total
        If total 0 or smallest => return 0
        else If total cannot be met any number of coins => return -1
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
