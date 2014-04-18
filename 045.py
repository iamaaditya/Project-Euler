# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 01:07:13 2014

@author: aaditya prakash
"""

import utilities
import math
import time

problem_number = '045'
problem_statement = """
Find the next (> 40755) Triangle number 
"""

def Triangle_Pentagon_Hexagon(n=285):
    """ Returns the Trianglular number greater than 'n'th number
    which is also pentagonal and hexagonal """
    
    iterTri = utilities.TriangleNumber(n+1)

    while True:
        nextTri = iterTri.next()
        # Every hexagonal number is also triangle number thus the second 
        # check is redundant but since the code is efficient 
        # I have left it there
        if(utilities.IsPentagonal(nextTri) and utilities.IsHexagonal(nextTri)): 
            return nextTri

timeStart = time.clock()
print(Triangle_Pentagon_Hexagon())
print('Time (sec):' + str(time.clock() - timeStart))
answer = ''



