# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 22:59:00 EST 2016

@author: aaditya prakash
"""

from __future__ import division
from utilities import is_square
from time import clock

problem_number = '080'
problem_statement = """
For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
"""

def solve():
    """ returns the sum of the first 100 decimal digits for first non perfect square numbers"""

    return sum( [sum(sqrt_list(i,100)[0]) for i in xrange(2, 101) if not is_square(i)])


def sqrt_list(n, precision):
    """ source http://stackoverflow.com/a/5187974 """
    ndigits = []        # break n into list of digits
    n_int = int(n)
    n_fraction = n - n_int

    while n_int:                            # generate list of digits of integral part
        ndigits.append(n_int % 10)
        n_int //= 10
    if len(ndigits) % 2: ndigits.append(0)  # ndigits will be processed in groups of 2

    decimal_point_index = len(ndigits) // 2  # remember decimal point position
    while n_fraction:                       # insert digits from fractional part
        n_fraction *= 10
        ndigits.insert(0, int(n_fraction))
        n_fraction -= int(n_fraction)
    if len(ndigits) % 2: ndigits.insert(0, 0)  # ndigits will be processed in groups of 2

    rootlist = []
    root = carry = 0                        # the algorithm
    while root == 0 or (len(rootlist) < precision and (ndigits or carry != 0)):
        carry = carry * 100
        if ndigits: carry += ndigits.pop() * 10 + ndigits.pop()
        x = 9
        while (20 * root + x) * x > carry:
                x -= 1
        carry -= (20 * root + x) * x
        root = root * 10 + x
        rootlist.append(x)
    return rootlist, decimal_point_index


timeStart = clock()
print(solve())
print('Time (sec):' + str(clock() - timeStart))
answer = ''



