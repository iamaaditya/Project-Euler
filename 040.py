# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 01:31:13 2014

@author: aaditya prakash
"""

import utilities
import math
import time

problem_number = '040'
problem_statement = """
Champernowne's constant
 dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

def Nth_frac(n):
    """ Returns the Nth number of the Champernowe_fraction """
    if n <= 9: return n
    pSep = 0
    tSum = 0
    i=0
    while True:
        i+=1
                
        dSep = i*9*10**(i-1)
        tSum += pSep
        if n < dSep:
            #print n, dSep, pSep, i, tSum
            fwd=(n-tSum)//i
            if( (n-tSum)%2 == 0 ): fwd -= 1
            sNextNum = str((10**(i-1))+fwd)
            #print sNextNum, (n-tSum)//i, (n-tSum)%i            
            return sNextNum[(n-tSum)%i-1]
            
        
        pSep = dSep


def Champernowne_Constant():
    """ Calculates the Champernowne constant 
    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000 """
    
    prod = 1
    
    for i in range(7):
        prod *= int(Nth_frac(10**i))
    
    return prod
    
        
    
    
timeStart = time.clock()
print(Champernowne_Constant())
#print(Nth_frac(21))
print('Time (sec):' + str(time.clock() - timeStart))
answer = ''



