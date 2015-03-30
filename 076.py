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

def counting_summations_v1(n):
    """ returns number of ways to counting upto n, by using atleast two positive integers"""

    sols = {}
    sols[1] = 1
    sols[2] = 2
    sols[3] = 3

    for i in xrange(4,n+1):
        ans = 0
        for j in xrange(i-1,0,-1):
            ans += sols[i-j]
        sols[i] = ans
        print sols
    return sols[n] 

def counting_summations_v2(n):
    """ returns number of ways to counting upto n, by using atleast two positive integers"""
    sols = {}
    sols[1] = 1
    sols[2] = 2
    sols[3] = 3

    
    for i in xrange(4,n+1):
        ans = 0
        for j in xrange(i-1,int(math.ceil(n/2))-1,-1):
            ans += sols[i-j]
        sols[i] = ans
        print sols
    return sols[n]*2  

def counting_summations(n):
    """ first lets do a small number by permuating all numbers """

    for i in xrange(n-1, 0, -1):
        print i, "rem:" ,n -i

timeStart = clock()
print(counting_summations(6))
print('Time (sec):' + str(clock() - timeStart))
answer = ''



