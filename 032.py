# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 12:15:49 2014

@author: aaditya prakash
"""

import utilities
import math
import time
import numpy as np
from itertools import permutations

problem_number = '032'
problem_statement = """
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
"""
def Sum_Products_Pandigital_MMM(n=9):
    """ Returns the sum of all products whose multiplicant/multiplier/product
    can be written as 1 through n digitial """
    
    digitsSets = set([i for i in range(1,n+1)])
    setPanProducts = set()    
    limit = sum([(n)*(10**i) for i in range(n//2)])
    loop = 0
    for multiplier in xrange(limit//2 + 2):
        for multiplicand in xrange(multiplier, limit//multiplier + 1):
            loop += 1
            product = multiplier * multiplicand
            productDigitsSet = set(map(int, str(str(multiplier)+str(multiplicand) + str(product))))
            if(productDigitsSet == digitsSets): 
                setPanProducts.update([product])
    return sum(list(setPanProducts))
    
def BETTER_Sum_Prod_Pandigital():
    """ This code is due to kremlin_ from projectueuler.net """
    sum_set = set()
    for num in permutations([str(i) for i in range(1, 10)]):
        ns = ''.join(num)
        for p1, p2, prod in [[int(ns[0:a]), int(ns[a:b]), int(ns[b:])] for a, b in [(2, 5), (1, 5)]]:
            if p1 * p2 == prod:
                sum_set.add(prod)
    return sum(list(sum_set))

timeStart = time.clock()
print(Sum_Products_Pandigital_MMM(9))
print('Time (sec):' + str(time.clock() - timeStart))
answer = '45228'

timeStart = time.clock()
print(BETTER_Sum_Prod_Pandigital())
print('Time (sec):' + str(time.clock() - timeStart))



