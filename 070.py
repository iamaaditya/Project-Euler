# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 22:55:12 EDT 2015

@author: aaditya prakash
"""

from __future__ import division
from utilities import PrimeList
from time import clock
import logging

problem_number = '070'
problem_statement = """
Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
"""

# p = True
p  = False

def totient_permuation(n):
    """ finds the number such that its totient function of which is its permuation and ratio of number to totient is min"""
    ratio_n_phi = 100000000
    smallest_i = 0
    for i in PrimeList(n):
        # if i % 1000 == 0 :
        #     print i, smallest_i
        # t = totient_function(i)
        t = i - 1
        if p : print i,t, i/t
        if i/t < ratio_n_phi:
            ratio_n_phi = i / t
            smallest_i = i
    return smallest_i

def sort_str(n):
    return ''.join(sorted(str(n)))

def check_permuation():
    for i in xrange(10000000,100,-1):
        if p: print i, sort_str(i)
        if sort_str(i) == sort_str(i-1):
            print i, i-1

check_permuation()

timeStart = clock()
# print(totient_permuation(10**7))
# print(totient_permuation(100))
print('Time (sec):' + str(clock() - timeStart))
answer = ''



