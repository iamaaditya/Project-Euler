"""
Created on 4/23/14 1:28 AM

@author: aaditya prakash

"""

import utilities as u
import time

problem_number = '0'

problem_statement = """
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""


def Multiple_Product(num):
    for multiple in range(2,7):
        sProduct = sorted(str(num*multiple))
        if(sProduct != sorted(str(num))): return False
    return True

def Permuted_Multiples():
    """
    Returns the smallest positive integer such that its multiple with 2 to 6 contain same digits
    """
    num = 1
    while True:
        num += 1
        if(Multiple_Product(num)): return num


timeStart = time.clock()
print(Permuted_Multiples())
print('Time (sec):' + str(time.clock() - timeStart))
answer = '142857'


