# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 00:58:04 EDT 2015

@author: aaditya prakash
"""

import utilities
import math
import time

problem_number = '097'
problem_statement = """
However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×27830457+1.
Find the last ten digits of this prime number.
"""

def mod_large(a,b,c):
    """ returns a**b mod c for very large b """
    ans = 1
    while b>0:
        ans *= a
        ans %= c
        b -= 1
    return ans


def large_mersenne_prime():
    """ Solve the Projet Euler Problem 097 """
    m = 28433
    n = 7830457
    c = 10**10
    return ((m%c) * (mod_large(2,n,c)) + 1%c ) % c



timeStart = time.clock()
print(large_mersenne_prime())
print('Time (sec):' + str(time.clock() - timeStart))
answer = '8739992577'



