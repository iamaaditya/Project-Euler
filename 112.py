# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:07:25 EDT 2015
@author: aaditya prakash
"""

from __future__ import division
from time import clock
from utilities import GetDigits

problem_number = '112'
problem_statement = """
Find the least number for which the proportion of bouncy numbers is exactly 99%. Where bouncy numbers are thsoe which are neither monotically increasing or decreasing digits wise
"""

def Is_Bouncy(n):
    """ checks if the given number is bouncy """
    digits = GetDigits(n)
    decreasing = []
    increasing = []
    for i in xrange(len(digits)-1):
        decreasing.append(digits[i] >= digits[i+1])
        increasing.append(digits[i] <= digits[i+1])

    return (not all(increasing)) and (not all(decreasing))
     
def bouncy_numbers(p):
    """find the number where the % of bouncy numbers reaches exactly p """
    count = 0
    i = 100
    while True:
        if Is_Bouncy(i): count += 1
        if count == p*i: return i 
        i += 1


timeStart = clock()
print(bouncy_numbers(0.99))

print('Time (sec):' + str(clock() - timeStart))
answer = '1587000'



