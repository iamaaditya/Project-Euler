# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 17:43:58 EDT 2015
@author: aaditya prakash
"""

from __future__ import division
from fractions import Fraction
from fractions import gcd
from math import floor
from time import clock

problem_number = '073'
problem_statement = """
How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?
"""

def slow_counting_fractions_range(D):
    """ solves 073, orders the fractions for all values less than d and returns the one before 3/7"""

    sols = set() 
    lower = 1/3
    upper = 1/2
    count_sols_2 = 0

    for n in xrange(1,int(upper*D)):
        for d in xrange(min(D, int(floor(n/lower))), int(floor(n/upper)), -1):
            f = n / d
            if f > lower and f < upper: 
                sols.add(Fraction(n,d))
    return len(sols)

def counting_fractions_range(D):
    """ faster method for counting the reduced fractions, by extracting only the actual fractions the counting part is just reducing using gcd instead of using the fractions class like slower solution"""
    count = 0
    for n in xrange(1, D+1):
        for k in xrange(n//3 + 1, (n-1)//2 + 1):
            if gcd(n,k) == 1 : count += 1
    return count


timeStart = clock()
print counting_fractions_range(12000)
print('Time (sec):' + str(clock() - timeStart))
answer = '7295372'



