# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 01:27:04 EST 2016

@author: aaditya prakash
"""

from __future__ import division
from math import sqrt, ceil
from utilities import PrimeList
from itertools import permutations, takewhile

from time import clock

problem_number = '087'
problem_statement = """
How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
"""


def solve(limit):
    """ This method calculates the limit for the search for every progressive prime, so that
    not every combinatio of primes on the p_list is used, this reduces the number of iterations
    inside the loop from 751,088,405 to 11,334,707"""
    upper_limit = ceil(sqrt(limit - 2**4 - 2**3))
    p_list = PrimeList(upper_limit)

    num_set = set()
    for x in p_list:
        val = limit - 2**4 - x**3
        if val < 0: continue
        lim = ceil(sqrt(val))
        for y in takewhile(lambda i: i<lim, p_list):
            val = limit - min(x,y)**4 - max(x,y)**3
            if val < 0: continue
            lim = ceil(sqrt(val))
            for z in takewhile(lambda i: i<lim, p_list):

                for a,b,c in permutations([x,y,z]):
                    ans = a**2 + b**3 + c**4
                    if ans > limit: continue
                    num_set.add(ans)
                    if a ==b and b == c: break

    return len(num_set)




timeStart = clock()
print(solve(50e6))
print('Time (sec):' + str(clock() - timeStart))
answer = '1097343'



