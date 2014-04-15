# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 01:22:55 2014

@author: aaditya prakash
"""

import utilities
import math
import time

problem_number = '031'
problem_statement = """
How many different ways can £2 be made using any number of coins?
Coins : 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
"""

def Ways_to_Change_x(x):
    """ Returns the total ways, 'x' dollars/pound could be exchanged in coins"""
    n = 100*x
    S = [1,2,5,10,20,50,100,200]
    m = len(S) -1
    return utilities.Linear_Combinations(S, n, m)
    

timeStart = time.clock()
print(Ways_to_Change_x(2))
print('Time (sec):' + str(time.clock() - timeStart))
answer = '73682'



