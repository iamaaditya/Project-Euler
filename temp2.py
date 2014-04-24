import time
import itertools
from utilities import isPrime

from collections import Counter
from urllib.request import urlopen

def problem54():
    def rank(hand):
        consecutive = lambda heights: len(set(heights)) == 5 and heights[0] - heights[-1] == 4

        heights, colors = zip(*hand)
        heights = sorted(['23456789TJQKA'.index(h) for h in heights], reverse=True)
        counts, highest = zip(*sorted([(heights.count(h), h) for h in set(heights)], reverse=True))

        if consecutive(heights) and len(set(colors)) == 1:
            return (8, heights) # StraightFlush
        elif counts[0] == 4:
            return (7, highest) # FourOfAKind
        elif counts[0] == 3 and counts[1] == 2:
            return (6, highest) # FullHouse
        elif len(set(colors)) == 1:
            return (5, heights) # Flush
        elif consecutive(heights):
            return (4, heights) # Straight
        elif counts[0] == 3:
            return (3, highest) # ThreeOfAKind
        elif counts[0] == 2 and counts[1] == 2:
            return (2, highest) # TwoPairs
        elif counts[0] == 2:
            return (1, highest) # OnePair
        else:
            return (0, heights) # HighCard

    with open('poker.txt') as f:

        #res =[1 for p in (l.split() for l in f) if rank(p[:5]) > rank(p[5:])]
        resCount = 0
        lineCount = 1
        for l in f:
            p = l.split()
            res = 1 if rank(p[:5]) > rank(p[5:]) else 0
            print(res, lineCount)
            lineCount += 1
            resCount += res
        return resCount

print(problem54())