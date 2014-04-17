# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 12:05:52 2014

@author: aaditya prakash
"""

import utilities
import math
import time

problem_number = '036'
problem_statement = """
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
"""

def Sum_All_Palindrome_A_B_under(pLimit, A=10, B=2):
    """ Returns the sum of all the palindromes in base A and B
    (no trailing zeros) under a given pLimit (base A) 
    assumes the bases to be 2, 8, 10, 16"""
    
    lA, lB = int(A//4.1), int(B//4.1)
    baseList = [bin, int, oct, hex]
    aBase, bBase = baseList[lA], baseList[lB]
    
    totalSum = 0
    for i in xrange(1, pLimit, 2): 
    # All even numbers in binary have trailing zeros
        sD = str(i)        
        sB = bin(i)[2:]
        if(utilities.IsPalindrome(sD) and utilities.IsPalindrome(sB)): totalSum +=i
    return totalSum
        

timeStart = time.clock()
print(Sum_All_Palindrome_A_B_under(1000000,10,2))
print('Time (sec):' + str(time.clock() - timeStart))
answer = '872187'



