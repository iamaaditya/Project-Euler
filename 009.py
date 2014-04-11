# -*- coding: utf-8 -*-
"""
Created on Sun Apr 06 13:59:47 2014

@author: aaditya prakash
"""

import utilities
import math



problem_number = '009'
problem_statement = """
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def pythagorean_triplet_sum(number):
    """ Returns the any pythagorean triplet whose sum is equal to number """
    
    # on solving the a^2 + b^2 = c^2 and a + b + c = number, we get
    # ab = number*(a+b - number/2)
    # on rearranging we get
    # b = number(a-number/2)/(a-number)
    
    for a in range(1,number):
        b = number*(a-number/2)/(a-number)
        c = int(math.sqrt(a**2 + b**2))
        if( a + b + c == 1000): 
            print(a,b,c)            
            break
    return a*b*c
    
print(pythagorean_triplet_sum(1000))

answer = '31875000'