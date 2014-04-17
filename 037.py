# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 12:49:43 2014

@author: aaditya prakash
"""

import utilities
import math
import time

problem_number = '037'
problem_statement = """
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
"""

def Sum_All_Trunctable_Prime():
    iterPrime = utilities.Eratosthenes()
    totalSum = 0 
    count = 0 
    while count < 11: # since given that there are only 11
        p = iterPrime.next()
        if(p < 10): continue
        if( utilities.IsTrunctablePrime(p)): 
            totalSum += p
            count +=1

    return totalSum
timeStart = time.clock()
print(Sum_All_Trunctable_Prime())
print('Time (sec):' + str(time.clock() - timeStart))
answer = '748317'



