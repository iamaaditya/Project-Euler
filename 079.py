# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 01:09:53 EDT 2015

@author: aaditya prakash
"""

from utilities import find_all
from time import clock
from string import digits
from itertools import permutations

problem_number = '079'
problem_statement = """
Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length
"""


def check_solution(key_list, passcode):
    
    for k in key_list:
        k0 =  min(find_all(passcode, k[0]))
        k1 = list(find_all(passcode, k[1]))
        k2 = max(find_all(passcode, k[2]))
        if not (k0 < max(k1) and min(k1) < k2): return False
    else:
        return True
        
def passcode_derviation():
    """ """
    key_list = set(read_data())
    unique_digits_in_key_list = [d for d in digits if d in ''.join(key_list)]
    for p in permutations(unique_digits_in_key_list):
        if check_solution(key_list, ''.join(p)): return p

def read_data():
    """reads the given file and returns the nubmers as a list"""

    with open("./keylog.txt") as f:
        lines = f.readlines()

    return map(str.strip, lines)

timeStart = clock()
print(passcode_derviation())
print('Time (sec):' + str(clock() - timeStart))
answer = ''



