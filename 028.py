# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 23:18:50 2014

@author: aaditya prakash
"""

import utilities
import math
import time
import numpy as np

problem_number = '028'
problem_statement = """
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
(Starting from center and moving to right clockwise, making spiral matrix)
"""

def Sum_Diagonals_Spiral_Matrix(N):
    """ Retuns the sum of the digonal elements of the Spiral Matrix of NxN
    where 1 is at center and increments towards right and clockwise """
    
    mat = utilities.Make_Spiral_Matrix(N)
    
    return sum(np.diag(mat)) + sum(np.diag(np.fliplr(mat))) - mat[N//2,N//2]

timeStart = time.clock()
print(Sum_Diagonals_Spiral_Matrix(1001))
print('Time (sec):' + str(time.clock() - timeStart))
answer = '669171001'



