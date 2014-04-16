# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 19:50:34 2014

@author: aaditya prakash
"""

import time
import numpy as np
from fractions import Fraction

problem_number = '033'
problem_statement = """
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

def Product_Digit_Cancelling_Fraction():
    """ Returns the Denominator of product of four non-trivial 
    fractios such that num and denom have a digit in common and 
    after removing the digit the fraction left is a simplied form of the given
    fraction 
    **
    Changed from custom reduce Fraction implementation to buitlin Fraction()"""

    spNum = []
    spDen = []    
    for n in xrange(10, 100):
        for d in xrange(n+1, 100):
            d1, d2 = str(d)
            n1, n2 = str(n)
            d1 = int(d1)
            d2 = int(d2)
            n1 = int(n1)
            n2 = int(n2)
            # filtering trivial cases
            if d2 == 0 or n2 == 0 or n1 ==0 or n2==0: continue                  

            if d1 == n1 and Fraction(n,d) == Fraction(n2,d2):
                spNum.append(n)
                spDen.append(d)
            
            elif d1 == n2 and Fraction(n,d) == Fraction(n1,d2):
                spNum.append(n)
                spDen.append(d)
            
            elif d2 == n1 and Fraction(n,d) == Fraction(n2,d1):
                spNum.append(n)
                spDen.append(d)
            
            elif d2 == n2 and Fraction(n,d) == Fraction(n1,d1):
                spNum.append(n)
                spDen.append(d)
            #print spNum, spDen    
    return Fraction(np.prod(spNum), np.prod(spDen))

timeStart = time.clock()
print(Product_Digit_Cancelling_Fraction())
print('Time (sec):' + str(time.clock() - timeStart))
answer = '100'



