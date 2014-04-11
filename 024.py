# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 17:21:57 2014

@author: aaditya prakash
"""

import utilities
import math
import time
import itertools

problem_number = '024'
problem_statement = """
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

def Lexicographic_Permutation(number, listInput):
    """ Returns the number'th lexicographic permuation of given listInput """

    permuts = itertools.permutations(listInput, 10)

    allPermuts = []
    for e in permuts:
        allPermuts.append(e)

    return "".join(list(allPermuts[number-1]))
    
    

timeStart = time.clock()
print(Lexicographic_Permutation(1000000, ['0','1','2','3', '4', '5', '6', '7', '8', '9']))
print('Time (sec):' + str(time.clock() - timeStart))
answer = '2783915460'



