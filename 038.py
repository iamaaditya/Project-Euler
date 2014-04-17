# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 13:48:40 2014

@author: aaditya prakash
"""

import utilities
import math
import time

problem_number = '038'
problem_statement = """
What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
def Largest_PanDigital_By_Concatenation():
    """ Returns the largest 9 digit pandigital number
    that can be obtained by concatenating a integer's 
    product with (1..n), where n > 1 """
    
    dicL = {1:9, 2:4, 3:3, 4:2}
    digitList = [str(i) for i in xrange(1,10)]
    largestPd = 0
    for i in xrange(10000):
        sl = len(str(i))
        nD = dicL[sl]    
        
        pd = ''
        for j in xrange(1, nD+1):
            pd += str(i*j)
        pdSorted = sorted(pd)
        if pdSorted == digitList and int(pd) > largestPd:
            largestPd = int(pd)
            
    return largestPd
    
timeStart = time.clock()
print(Largest_PanDigital_By_Concatenation())
print('Time (sec):' + str(time.clock() - timeStart))
answer = '932718654'



