# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 18:50:49 EDT 2015
@author: aaditya prakash
"""
from __future__ import division
from time import clock
from fractions import gcd
from utilities import isPrimeFast
# from utilities import totient_function
from utilities import PrimeList
from sympy.ntheory import mobius


problem_number = '072'
problem_statement = """
How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?
"""

prime_list = list()
def totient(n):
    global prime_list

    if isPrimeFast(n): 
        return n-1
    total = 1
    for p in prime_list:
        if p > n: break
        if n % p == 0: 
            total *= (1 - 1/p)
    return total*n
    
def using_totient(D):
    """ """
    count = 0
    global prime_list
    prime_list.extend(PrimeList(D))
    for n in xrange(2, D+1):
        count += totient(n)

    return count

def using_farey( n, asc=True ):
    """Code from wiki: Python function to print the nth Farey sequence, either ascending or descending."""
    if asc: 
        a, b, c, d = 0, 1,  1  , n     # (*)
    else:
        a, b, c, d = 1, 1, n-1 , n     # (*)
    # print "%d/%d" % (a,b)
    count = 0
    while (asc and c <= n) or (not asc and a > 0):
        k = int((n + b)/d)
        a, b, c, d = c, d, k*c - a, k*d - b
        # print "%d/%d" % (a,b) 
        count += 1
    return count - 1

def using_mobius(n):
    count = 0
    for k in xrange(1,n+1):
        count += mobius(k)*((n//k)**2)
    return (1 + count)/2 - 1


timeStart = clock()
print using_mobius(10**6)

print('Time (sec):' + str(clock() - timeStart))
answer = '303963552391'



