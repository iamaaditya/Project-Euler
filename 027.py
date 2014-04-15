# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 20:13:05 2014

@author: aaditya prakash
"""

import utilities
import math
import time

problem_number = '027'
problem_statement = """
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

def Prod_coeff_most_primes(aLimit, bLimit):
    """ Returns the product of coeffficient of the quadratic formula
    x^2 + ax + b where for values of from 0 produces most number of 
    consecutive primes, with a limited to aLimit and llly b """
    
    longestChain = 0
    aLongest = 0
    bLongest = 0
 
    for a in xrange(-1*aLimit + 1, aLimit):
        for b in xrange(-1*bLimit +1, bLimit):
            chain = 0
            for i in xrange(max(aLimit, bLimit)):
                eqn = i*i + a*i + b
                if eqn < 0 : break
                if i==a and a==b: break
                if(utilities.isPrime(eqn)): chain += 1
                else: break
            if(chain > longestChain):
                longestChain = chain
                aLongest = a
                bLongest = b
    return aLongest*bLongest
        


timeStart = time.clock()
print(Prod_coeff_most_primes(1000,1000))
print('Time (sec):' + str(time.clock() - timeStart))
answer = '-59231'



