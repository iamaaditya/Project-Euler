# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 01:56:04 EDT 2015

@author: aaditya prakash
"""

import utilities
import math
from time import clock

problem_number = '092'
problem_statement = """
How many starting numbers below ten million will arrive at 89? (on repetitively summing the square of the digits
"""

def SumDigitsSquare(n):
    r = 0
    while n:
        r,n = r + (n%10)**2, n // 10
    return r

sols = {} 

def ContinuousSumDigitsSquare(n):
    """ returns either 81 or 1, by continuously repetitively calling SumDigitsSquare """
    global sols
    ans = n
    while True:
        ans= SumDigitsSquare(ans)
        if ans in sols: return sols[ans]
        if ans == 89 or ans == 1 : 
            sols[n] = ans 
            return ans

def square_digits_chain():
    """ square_digits_chain square digits sum , key is to memoize the prior solutions"""
    count = 0
    for i in xrange(1, 10000000):
        r = ContinuousSumDigitsSquare(i)
        if r == 89: count += 1
    return count



timeStart = clock()
print(square_digits_chain())
print('Time (sec):' + str(clock() - timeStart))
answer = '8581146'



