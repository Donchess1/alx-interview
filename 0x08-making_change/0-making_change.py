#!/usr/bin/python3

"""coin change using greedy algorithm"""

def makeChange(coins, total):
    trial = [float ('inf')] * (total+1) #creating default counter list 0-total+1
    trial[0]= 0 # zeroing the first element
    for coin in coins:
        for x in range (coin, total+1):
            trial[x] = min(trial[x], trial[x-coin]+1)
    return trial[total] if trial[total] != float ('inf') else -1
