# -*- coding: utf-8 -*-
"""
Created on Tue Apr 08 00:55:53 2014

@author: aaditya prakash
"""

import utilities
import math
import time

problem_number = '000'
problem_statement = """
Which starting number, under one million, produces the longest collatz sequence chain?
"""

def Longest_Collatz_under_x(parameter):
    """ Returns the Starting Number, under 'parameter', which produces longest collatz sequence """
    largestNumber = 0
    longestSequence = 0
    for i in range(parameter):
        seqLength = utilities.LengthCollatz(i)
        if(seqLength > longestSequence):
            longestSequence = seqLength
            largestNumber = i
    return largestNumber
    
def Longest_Collatz_FAST(parameter):
    largestNumber = 0
    longestSequence = 0
    
    dicCollatz = {}
    
    for i in range(parameter):
        j = i        
        iSeq = 0        
        while True:
            if(i<=1):
                iSeq += 1
                dicCollatz[j] = iSeq
                break
            elif i in dicCollatz:
                iSeq += dicCollatz[i]
                dicCollatz[j] = iSeq
                break
            elif i%2==0:
                i /= 2
                iSeq += 1
            else:
                i = 3*i + 1
                iSeq += 1
        if( iSeq > longestSequence):
            longestSequence = iSeq
            largestNumber = j
            
    return largestNumber     
            
        

timeStart = time.clock()
print(Longest_Collatz_under_x(1000000))
print('Time (sec):' + str(time.clock() - timeStart))
answer = '837799'

timeStart = time.clock()
print(Longest_Collatz_FAST(1000000))
print('Time (sec):' + str(time.clock() - timeStart))
answer = '837799'



