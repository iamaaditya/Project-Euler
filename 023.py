# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 15:24:53 2014

@author: aaditya prakash
"""

import utilities
import math
import time
import itertools

problem_number = '023'
problem_statement = """
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
def Sum_All_Abundant_Number_below_x(number=28124):
    """ Returns the sum of all positive integers < number which CANNOT be represented
    as sum of two abundante numbers(whose sum of factors are less than itself) 
    by default number=28124 is the upper limit """    
    
    # Make a list of abundant numbers below 'number'
    listAbundant = []
    iterAbundant = utilities.Abundant()
    while True:
        nextAbundant = iterAbundant.next()
        if(nextAbundant >= number): break
        listAbundant.append(nextAbundant)
    
    twoCombination = itertools.combinations(listAbundant, 2)
    sumTwoCombination = set()
    for e in twoCombination:
        sumTwoCombination.update([sum(list(e))])
    
    for k in listAbundant:
        sumTwoCombination.update([k+k])
    
    NotInTwoCombination = set(range(1,number)) - sumTwoCombination
    totalSum = sum(list(NotInTwoCombination))

    return totalSum
 
def Sum_All_Abundant_Number_below_x_FAST(number=28124):
    """ Returns the sum of all positive integers < number which CANNOT be represented
    as sum of two abundante numbers(whose sum of factors are less than itself) 
    by default number=28124 is the upper limit """    
    
    # Make a list of abundant numbers below 'number'
    listAbundant = []
    iterAbundant = utilities.Abundant()
    while True:
        nextAbundant = iterAbundant.next()
        if(nextAbundant >= number): break
        listAbundant.append(nextAbundant)
    
    AbundantNumsOfSums = []
    for i in xrange(len(listAbundant)):
        for j in xrange(i,len(listAbundant)):
            newNum = listAbundant[i] + listAbundant[j]
            if newNum < number : AbundantNumsOfSums.append(newNum)
    
    totalSum = sum(list(set(range(1,number)) - set(AbundantNumsOfSums)))
    return totalSum

timeStart = time.clock()
print(Sum_All_Abundant_Number_below_x_FAST())
print('Time (sec):' + str(time.clock() - timeStart))
answer = '4179871'



