# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 00:21:13 EDT 2015
@author: aaditya prakash
"""

from __future__ import division
from fractions import Fraction
from math import floor
from time import clock

problem_number = '071'
problem_statement = """
By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.
"""

def ordered_fractions(D):
    """ solves 071, orders the fractions for all values less than d and returns the one before 3/7"""
    sols = []
    lower = 3/7 - 0.000001
    upper = 3/7 + 0.000001
    for n in xrange(1,int(upper*D)):
        for d in xrange(min(D, int(floor(n/lower))), int(floor(n/upper)), -1):
            f = n / d
            if f > lower and f < upper: sols.append(Fraction(n,d))
    
    sols_decimal = [(f.numerator/f.denominator, f.numerator, f.denominator) for f in sols]
    
    sols_decimal.sort(key=lambda p: p[0])
    for i, f in enumerate(sols_decimal):
        if f[1] == 3 and f[2] == 7:
            return sols_decimal[i-1][1]
        


timeStart = clock()
print(ordered_fractions(1000000))
print('Time (sec):' + str(clock() - timeStart))
answer = '428570'



