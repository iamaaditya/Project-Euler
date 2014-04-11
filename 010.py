# -*- coding: utf-8 -*-
"""
Created on Sun Apr 06 14:20:05 2014

@author: aaditya prakash
"""

import utilities
import math

problem_number = '010'
problem_statement = """
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def sum_of_primes_below_x(number):
    """ Returns the sum of all prime numbers below 'number' """
    listOfPrimes = utilities.PrimeList(number)
    sumP = 0    
    for i in listOfPrimes:
        sumP += i
    return sumP
    
print(sum_of_primes_below_x(2000000))

answer = '142913828922'