# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 16:48:32 2014

@author: aaditya prakash
"""

import utilities
import math
import time
from itertools import permutations

problem_number = '043'
problem_statement = """
Find the sum of all 0 to 9 pandigital numbers with this property.
Property: 3 char consecutive substring is divisible by prime numbers upto 17
"""

def Sub_String_Divisiblity():
    """ Returns the sum of all the 0-9 pandigital numbers which are
    divisible by 2,3,5,7,11,17 with 3 consecutive digits starting from 
    second position onwards """
    
    digits = [i for i in xrange(10)]
    
    #count = 0
    totalSum = 0
    for num in permutations(digits):
        #count += 1

        if num[0]== 0 : continue
        elif num[3]%2 : continue
        elif (num[2]+num[3]+num[4])%3 : continue
        elif num[5] not in [0, 5] : continue
        elif (num[4]*100 + num[5]*10 + num[6])%7 : continue        
        elif (num[5]*100 + num[6]*10 + num[7])%11 : continue        
        elif (num[6]*100 + num[7]*10 + num[8])%13 : continue                
        elif (num[7]*100 + num[8]*10 + num[9])%17 : continue        
        else:
            totalSum += int(''.join(map(str, num)))

    return totalSum
timeStart = time.clock()
print(Sub_String_Divisiblity())
print('Time (sec):' + str(time.clock() - timeStart))
answer = '16695334890'



