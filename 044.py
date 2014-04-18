# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 23:14:26 2014

@author: aaditya prakash
"""

import utilities
import math
import time

problem_number = '044'
problem_statement = """
Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?

Pentagonal Number : Pn = n(3n-1)/2
"""


def Pentagonal_Pair_Smallest_Diff_IMPROVED():
    """ Returns the smallest diff of two pentagonal number such that 
    their difference and sum are also pentagonal number """
    
    iterPent = utilities.Pentagonal_Numbers()
    
    pentList = [iterPent.next() for i in xrange(10)]
    
    #for i in xrange(len(pentList)):
    i=0
    while True:
        i+=1
        for j in xrange(i-1, -1, -1):
            d = pentList[i]-pentList[j]
            s = pentList[i] + pentList[j]
            if utilities.IsPentagonal(d) and utilities.IsPentagonal(s):
                return d
            while s > pentList[-1]:
                pentList.append(iterPent.next())
     
timeStart = time.clock()
print(Pentagonal_Pair_Smallest_Diff_IMPROVED())
print('Time (sec):' + str(time.clock() - timeStart))
answer = '5482660'



