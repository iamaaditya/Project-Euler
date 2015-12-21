# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 18:55:19 EST 2015
@author: aaditya prakash
"""

from __future__ import division
from time import clock
from utilities import PrimeList
from itertools import takewhile

problem_number = '077'
problem_statement = """
What is the first value which can be written as the sum of primes in over five thousand different ways?
"""


sums_dict = {} # used for memoization
primes = PrimeList(200)

def sum_rem_to_i(n, i):
    """ recursively calculates number of ways of summing upto n using primes less than and equal to i """
    # since the smallest prime is >1, there is no way to sum lesser than that
    if i <= 1 or n <= 1: return 0

    if i == 2 and n == 2: return 1    # summing upto 2 using only 2, only 1 way

    if i == 3 and n in [3, 4, 5]: return 1 # summing upto 3 using only 3, only 1 way

    # if using only 2, but any number
    if i==2: return 1 if n%2 == 0 else 0 # if number is even, there is 1 way 2 2 2 2...

    # Memoization for speed
    global sums_dict
    if (n, i) in sums_dict:
        return sums_dict[(n,i)]

    sum = 0
    # for l in xrange(i, 0, -1):
    for l in reversed(list(takewhile(lambda x: x <= i, primes))):
        # print "L: " , l
        if l > n: continue
        if l == n :
            ans = 1
        else:
            ans = sum_rem_to_i(n-l, min(l,n-l))
        sums_dict[(n-l,min(l,n-l))] = ans
        sum += ans
    return sum


def solve(N):
    """ returns the smallest number that has interger partiion in N ways """
    i = 2
    while True:
        if sum_rem_to_i(i,i-1)>= N: return i
        i += 1
    
timeStart = clock()
print solve(5000)
print('Time (sec):' + str(clock() - timeStart))
answer = '71'



