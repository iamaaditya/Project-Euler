# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 21:10:45 2014

@author: aaditya prakash
"""

import utilities
import math
import time

problem_number = '026'
problem_statement = """
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

def Largest_Recurring_Decimal_underX(number):
    """ Returns the largest d for which 1/d has the longest recurring decimal cycle, where
    d is less than number """
    
    largestRecur = 0
    largestD = 0
    
    for i in range(2,number):
        lenR = utilities.Length_Recurring_Cycle(1,i)
        
        if(lenR > largestRecur):
            largestRecur = lenR
            largestD = i
    return largestD

timeStart = time.clock()
print(Largest_Recurring_Decimal_underX(1000))
print('Time (sec):' + str(time.clock() - timeStart))
answer = '983'



