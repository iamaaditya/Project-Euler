# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 02:57:10 2014

@author: aaditya prakash
"""

import utilities
import math
import time

problem_number = '035'
problem_statement = """
How many circular primes are there below one million?
"""

def Number_Circular_Primes(nLimit):
    """ Returns the number of circular primes below nLimit """
    count = 0    
    for i in xrange(2,nLimit):
        if(utilities.isPrime(i)): 
            if(utilities.IsCircularPrime(i)):
                count += 1
    
    return count    

timeStart = time.clock()
print(Number_Circular_Primes(1000000))
print('Time (sec):' + str(time.clock() - timeStart))
answer = '55'



