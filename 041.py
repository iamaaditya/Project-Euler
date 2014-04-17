# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 15:26:25 2014

@author: aaditya prakash
"""

import utilities
import math
import time

problem_number = '041'
problem_statement = """
What is the largest n-digit pandigital prime that exists?
"""

def Largest_Pandigit_Prime():
    """ Returns the largest N digit Prime """
    
    # 9 and 8 digits cannot be because 1-9 and 1-8
    # pandigital numbers are divible by 3    
    for i in xrange(7, 3, -1):    
        print i        
        iterPan = utilities.Generate_n_Pandigit_Number_Prime(i)
        while True:
            try:    
                nextNum = iterPan.next()     
                if(utilities.isPrime(nextNum)): return nextNum
            except StopIteration:
                break
    return 2143
timeStart = time.clock()
print(Largest_Pandigit_Prime())
print('Time (sec):' + str(time.clock() - timeStart))
answer = '7652413'



