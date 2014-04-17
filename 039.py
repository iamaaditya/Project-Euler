# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 22:42:14 2014

@author: aaditya prakash
"""

import utilities
import math
import time
from fractions import gcd
from collections import Counter

problem_number = '039'
problem_statement = """
For which value of perimeter, p ≤ 1000, is the number of 
solutions for right angle triangle is maximised?
"""

def Maxima_Perimeter(pLimit):
    """ Returns the value of p < pLimit for which perimeter
    the number of interger solutions to right angle triangle is maximised """
    
    maximalP = 0
    maximalSols = 0
    for p in xrange(3,pLimit):
        numOfSols = 0
        for a in xrange(1,p-2):
            for b in xrange(a,p-2):
                c = p - a - b
                if c*c == a*a + b*b: numOfSols += 1
        if numOfSols > maximalSols:
            maximalSols = numOfSols
            maximalP = p
    return maximalP

def BETTER_Maxima_Perimeter(pLimit):
    
    count = Counter()
    for m in xrange(25):
        for n in xrange(m % 2 + 1, m, 2): #even or add depending on m
            if gcd(m, n)==1:
                p = 2 * m ** 2 + 2 * m * n
                k = 1
                while p * k <= pLimit:
                    count[p * k] = count.get(p * k, 0) + 1
                    k += 1
    return count.most_common()[0][0]
    
timeStart = time.clock()
#print(Maxima_Perimeter(1000))
print('Time (sec):' + str(time.clock() - timeStart))
answer = '840'


timeStart = time.clock()
print(BETTER_Maxima_Perimeter(1000))
print('Time (sec):' + str(time.clock() - timeStart))


