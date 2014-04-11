# -*- coding: utf-8 -*-
"""
Created on Tue Apr 08 15:43:34 2014

@author: aaditya prakash
"""

import utilities
import math
import time
import scipy.misc

problem_number = '015'
problem_statement = """
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""

def Total_Routes_x_grid(number1, number2):
    """ Returns the total number of paths from top left to bottom right in a given grid 
    of size number1 x number2 """
    
    # Since in number x number grid, to reach from top left
    # to bottom right, one must travel atleast (number1+number2) units
    # out of which atleast number1 must be bottom and number2 right
    # but the order does not matter
    # thus this problem is equivalent to x Choose y, where x is total paths
    # and y is equal to number of paths in one direction
    return scipy.misc.comb((number1+number2), number1, exact=True)
    

timeStart = time.clock()
print(Total_Routes_x_grid(20,20))
print('Time (sec):' + str(time.clock() - timeStart))
answer = ''



