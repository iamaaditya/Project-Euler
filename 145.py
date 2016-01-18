# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 12:23:48 EST 2016

@author: aaditya prakash
"""

from __future__ import division
from time import clock

problem_number = '145'
problem_statement = """

"""


def solve(limit):
    odds = set(map(str, [i for i in xrange(1,10,2)])) # set of odd digits
    count = 0
    for i in xrange(11, limit):
        if i%10 == 0: continue # since no trailing zeroes
        istr = str(i)

        # sum of first and last digit must be odd
        if not ((istr[0] in odds) ^ (istr[-1] in odds)): continue

        rev = int(istr[::-1])
        if len( set(str(i + rev)) - odds ) == 0: 
            # print i, rev, i + rev
            count += 1
    return count


timeStart = clock()
print(solve(int(1e8))) # there are no solutions for numbers in range 1e8 to 1e9
print('Time (sec):' + str(clock() - timeStart))
answer = '608720'

