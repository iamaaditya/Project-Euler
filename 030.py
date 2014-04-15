# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 00:37:58 2014

@author: aaditya prakash
"""

import utilities
import math
import time

problem_number = '030'
problem_statement = """
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

def Sum_Numbers_x_Power_Digits(x):
    """ Returns the Sum of all the numbers that can be written as the sum of xth power
    of their digits"""
    totalSum = 0    
    for i in xrange(10, 999999):
        if i == sum([int(j)**x for j in str(i)]):
            totalSum += i
    return totalSum

timeStart = time.clock()
print(Sum_Numbers_x_Power_Digits(5))
print('Time (sec):' + str(time.clock() - timeStart))
answer = '443839'



