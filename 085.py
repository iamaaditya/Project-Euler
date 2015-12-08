# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:33:57 EDT 2015
@author: aaditya prakash
"""

from __future__ import division
from time import clock

problem_number = '085'
problem_statement = """
Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.
"""

def number_of_sub_rectangles(a,b):
    """ returns the number of sub rectangles in a given rectangle of size a x b """
    # best to use the formula a * b * (a+1) * (b+1) / 4
    tot = 0 
    for m in xrange(1,a+1):
        for n in xrange(1,b+1):
            tot += (a - m + 1) * (b - n + 1)
    return tot


def counting_rectangles(N):
    """ returns the area of the rectangle, which has as close to as N possible sub rectangles"""
    max_so_far = 1
    best_area = 0
    for a in xrange(1,200):
        for b in xrange(a, 200):
            num = number_of_sub_rectangles(a,b)
            if num > max_so_far and num < N:
                max_so_far = num
                best_area = a*b
    return best_area



timeStart = clock()
print(counting_rectangles(2000000))
print('Time (sec):' + str(clock() - timeStart))
answer = '2772'



