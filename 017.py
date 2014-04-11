# -*- coding: utf-8 -*-
"""
Created on Tue Apr 08 23:52:33 2014

@author: aaditya prakash
"""

import utilities
import math
import time

problem_number = '017'
problem_statement = """
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

def Letters_Under_x(Number):
    """ Returns the sum of letters in all numbers less than equal to 'number' 
    when written in words, includes 'and' for hundred above 
    assumes Number <= 1000 """
    belowHundred = [len(utilities.NumberToWord(i)) for i in range(1,100)]
    if(Number < 100): return sum(belowHundred[:Number])
    sumBelowHundred = sum(belowHundred)
    
    totalSum = sumBelowHundred
    
    for i in range(1,Number//100):
        totalSum += 100*(belowHundred[i-1] + len('hundred') + len('and')) + sumBelowHundred - len('and') # this last term because "100 does not have 'and'
    
    if(Number<1000):
        return totalSum + (Number%100 + 1)*(belowHundred[Number//100 -1] + len('hundred') + len('and')) + sum(belowHundred[:Number])   - len('and')
    return totalSum + len('onethousand')
    
timeStart = time.clock()
print(Letters_Under_x(999))
print('Time (sec):' + str(time.clock() - timeStart))
print(time.clock() - timeStart)
answer = '21124'



