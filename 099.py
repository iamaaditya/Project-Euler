# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 16:46:10 EDT 2015

@author: aaditya prakash
"""

from math import log
from time import clock

problem_number = '099'
problem_statement = """
Using base_exp.txt, a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.
"""

def largest_exponential(fName):
    """ finds the largest exponential for a base pair in a given file"""

    with open(fName) as f:
        largest_base_pair = 0
        sol = 0
        for line_number, line in enumerate(f):
            base, exponent = map(int, line.split(','))
            base_exponent = exponent * log(base)
            if base_exponent > largest_base_pair: 
                largest_base_pair = base_exponent
                sol = line_number
    return sol + 1 # index begins from 0


timeStart = clock()
print(largest_exponential('./files/p099_base_exp.txt'))
print('Time (sec):' + str(clock() - timeStart))
answer = '709'



