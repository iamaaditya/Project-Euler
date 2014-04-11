# -*- coding: utf-8 -*-
"""
Created on Wed Apr 09 22:20:17 2014

@author: aaditya prakash
"""

import utilities
import math
import time

problem_number = '021'
problem_statement = """
Evaluate the sum of all the amicable numbers under 10000.
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
"""

def Sum_Amicable_belox_x(number):
    """ Returns the sum of all amicable numbers below 'number' """
    
    totalSum = 0
    amicable = {}
    for i in range(1,number):
        if(utilities.isPrime(i)): continue
        sumOfFactors = sum(list(sorted(utilities.AllFactors(i)))[:-1])
        if sumOfFactors in amicable:
            if amicable[sumOfFactors] == i:
                totalSum += i + sumOfFactors
                #print i, sumOfFactors
        amicable[i] = sumOfFactors
    return totalSum
    
    
timeStart = time.clock()
print(Sum_Amicable_belox_x(10000))
print('Time (sec):' + str(time.clock() - timeStart))
answer = '31626'



