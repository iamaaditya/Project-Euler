# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 17:04:32 EDT 2015

@author: aaditya prakash
"""
from __future__ import division
import utilities
import math
from time import clock

problem_number = '076'
problem_statement = """
How many different ways can one hundred be written as a sum of at least two positive integers?
"""

sums_dict = {}
def counting_summations(n):
    """ first lets do a small number by permuating all numbers """

    sum = 0
    for i in xrange(n-1, 0, -1):
        sum += sum_i_to_n(n-i, i) 
    return sum

def sum_i_to_n(n,i):
    """ this function recursively calculates, number of ways to summing upto n using numbers less than and equal to i """
    global sums_dict
    if (n,i) in sums_dict:
        return sums_dict[(n,i)]
    sum = 0
    if i <= 1 or n <= 1: 
        return 1
    for l in xrange(i, 0, -1):
        if l > n: continue
        ans = sum_i_to_n(n-l, min(l,n-l))
        sums_dict[(n-l,min(l,n-l))] = ans
        sum += ans
    return sum

timeStart = clock()
print(counting_summations(100))
print('Time (sec):' + str(clock() - timeStart))
answer = '190569291'



