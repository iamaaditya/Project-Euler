# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:06:14 EDT 2015
@author: aaditya prakash
"""

from __future__ import division
from time import clock
import re

problem_number = '089'
problem_statement = """
Find the number of characters saved by writing each of these in their minimal form. (For the given file with roman numerals in each line 
"""

def reduce_roman():
    """ reduces the given roman string into most efficient """
    pass

    in_str = open('./files/p089_roman.txt').read().splitlines()

    cumtotal = 0
    for str in in_str:
        red_str = str 

        red_str = re.sub(r'DCCCC', 'CM', red_str)
        red_str = re.sub(r'CCCC', 'CD', red_str)

        red_str = re.sub(r'LXXXX', 'XC', red_str)
        red_str = re.sub(r'XXXX', 'XL', red_str)

        red_str = re.sub(r'VIIII', 'IX', red_str)
        red_str = re.sub(r'IIII', 'IV', red_str)

        cumtotal +=  len(str) - len( red_str )

    return cumtotal

timeStart = clock()
print(reduce_roman())
print('Time (sec):' + str(clock() - timeStart))
# answer = '743'



