# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 21:16:53 EDT 2015
@author: aaditya prakash
"""

from time import clock
from itertools import permutations

problem_numbes = '068'
problem_statement = """
Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?
See the website for the figure of the 3-gon ring
"""

def magic_gon_ring():
    """ solves the magic gon ring problem for "n" polygon"""
    n = 3
    # n = 5

    numbers = [i for i in xrange(1,2*n+1)]

    for i in permutations(numbers):
        print i
    # print numbers
    


timeStart = clock()
print(magic_gon_ring())
print('Time (sec):' + str(clock() - timeStart))
answer = ''



