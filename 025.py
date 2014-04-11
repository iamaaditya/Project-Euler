# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 17:29:33 2014

@author: aaditya prakash
"""

import utilities
import math
import time

problem_number = '025'
problem_statement = """
What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

def First_term_xDigits_Fib(number):
    """ Returns the first Fib term to contain 'number' digits """
    
    iterFib = utilities.Fibonacci()
    
    countTerm = 0
    while True:
        newFib = iterFib.next()
        if(len(str(newFib)) >= number): return countTerm
        countTerm += 1

timeStart = time.clock()
print(First_term_xDigits_Fib(1000))
print('Time (sec):' + str(time.clock() - timeStart))
answer = '4782'



