#!/usr/bin/python3

"""coin change using dynamic programming"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    trial = [float('inf')] * (total+1)   # creating default counter list
    trial[0] = 0   # zeroing the first element
    for coin in coins:
        for x in range(coin, total + 1):
            trial[x] = min(trial[x], trial[x-coin] + 1)
    return trial[total] if trial[total] != float('inf') else -1
