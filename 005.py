# -*- coding: utf-8 -*-
"""
Created on Fri Apr 04 23:07:47 2014

@author: aaditya prakash
"""

import utilities
import math

problem_number = '005'
problem_statement = """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10
    without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def smallest_divisible_until_x(parameter):
    """ Returns the smallest positive number that is evenly divisible by all numbers from 1 to parameter """
    dictFactorsAll = {}
    dictFactorsOne = {}
    for p in utilities.PrimeList(parameter): dictFactorsAll[p]=0

    for i in range(1, parameter+1):
        for p in utilities.PrimeList(parameter): dictFactorsOne[p]=0
        #print(dictFactorsOne)
        dictFactorsOne = utilities.PrimeFactors(dictFactorsOne, i)
        for k in dictFactorsAll:
            dictFactorsAll[k] = max(dictFactorsAll[k], dictFactorsOne[k])

    prod = 1
    for k in dictFactorsAll:
        prod *= k**dictFactorsAll[k]

    return(prod)

print(smallest_divisible_until_x(20))

answer = '232792560'