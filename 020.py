# -*- coding: utf-8 -*-
"""
Created on Wed Apr 09 22:14:40 2014

@author: aaditya prakash
"""

import utilities
import math
import time
from scipy import misc

problem_number = '020'
problem_statement = """
Find the sum of the digits in the number 100!
"""

def Sum_digits_x_Factorial(number):
    """ Returns the sum of the digits of the 'number' factorial """
    return utilities.SumDigits(misc.factorial(number, exact=True))

timeStart = time.clock()
print(Sum_digits_x_Factorial(100))
print('Time (sec):' + str(time.clock() - timeStart))
answer = ''



