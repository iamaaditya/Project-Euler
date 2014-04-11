# -*- coding: utf-8 -*-
"""
Created on Tue Apr 08 15:57:41 2014

@author: aaditya prakash
"""

import utilities
import math
import time

problem_number = '016'
problem_statement = """
What is the sum of the digits of the number 21000?
"""



timeStart = time.clock()
print(utilities.SumDigits(2**1000))
print('Time (sec):' + str(time.clock() - timeStart))
print(time.clock() - timeStart)
answer = ''



