# -*- coding: utf-8 -*-
"""
Created on Fri Apr 04 00:00:34 2014

@author: aaditya prakash
"""

import utilities
import math

problem_number = '003'
problem_statement = """The prime factors of 13195 are 5, 7, 13 and 29.
                    What is the largest prime factor of the number 600851475143 ?"""

def largest_prime_factor(parameter):
    """ Returns largest Prime factor of the given 'parameter' as number """
    iterPrime = utilities.PrimeReverse(math.ceil(math.sqrt(parameter)))
    if(utilities.isPrime(parameter)):
        return parameter
    while True:
        nextPrime = iterPrime.next()
        if(parameter % nextPrime == 0 or nextPrime == 2):
            return nextPrime

print(largest_prime_factor(600851475143))

answer = '6857'