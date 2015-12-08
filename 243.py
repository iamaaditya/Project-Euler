# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 21:04:00 EST 2015

@author: aaditya prakash
"""

from __future__ import division
from time import clock
from utilities import primes, totient

problem_number = '243'
problem_statement = """
Find the smallest denominator, whose resilience is < 15499/94744
"""

def smallest_resilience(a,b):

    p = primes()
    current = 1

    # larger steps, multiply by primes
    while True:
        pi = p.next()
        current *= pi
        if resilience(current) < (a/b):
            current /= pi
            break

    # finer steps, multiply by consecutive integers
    i = 2
    while True:
        if resilience(current*i) < a/b:
            return int(current*i)
        i += 1

def resilience(n):
    return totient(n)/(n-1)


timeStart = clock()
print(smallest_resilience(15499, 94744))
print('Time (sec):' + str(clock() - timeStart))
answer = '892371480'



