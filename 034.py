# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 02:27:44 2014

@author: aaditya prakash
"""

import utilities
import math
import time
from math import factorial

problem_number = '034'
problem_statement = """
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
"""

def Sum_Numbers_Factorial_Digits(nLimit=99999):
    """ Returns the sum of all numbers which are equal to sum of factorials
    of their digits """
    
    factList = [factorial(x) for x in xrange(10)]
    curiousNumbers = []
    for i in xrange(10,nLimit):
        
        if i == sum([factList[int(c)] for c in str(i)]):
            curiousNumbers.append(i)
    return(sum(curiousNumbers))

timeStart = time.clock()
print(Sum_Numbers_Factorial_Digits())
print('Time (sec):' + str(time.clock() - timeStart))
answer = '40730'



