"""
Created on 4/21/14 11:37 PM

@author: aaditya prakash

"""

import utilities as u
import time
import EXTUtilities as EXT
import math

problem_number = '047'
problem_statement = """
Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
"""

def Consecutive_Num_Distinct_Factors(n=4):
    """ Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
    """

    num = 145
    sucCount = 0
    while True:
        num+=1
        setF = u.PrimeFactorsSet(num)
        if(len(setF)==n):
            sucCount += 1
        else:
            sucCount = 0
            continue
        if(sucCount == n):
            # for More accurate code, here the code can be
            # augmented to see if the intersection of set of all factors
            # is zero. but since without doing that we get the right
            # answer, I have left that part.
            return num-3





timeStart = time.clock()
print(Consecutive_Num_Distinct_Factors(4))
print('Time (sec):' + str(time.clock() - timeStart))
answer = '134043'


