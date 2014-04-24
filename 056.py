"""
Created on 4/24/14 1:49 AM

@author: aaditya prakash

"""

import utilities as u
import time
from EXTUtilities import sum_digits

problem_number = '056'

problem_statement = """
Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""


def Powerful_Digit_Sum(nLimit=100):
    """
    Returns the largest sum of the digits for a^b where a, b < nLimit
    """
    res = 0
    for a in range(1,nLimit):
        for b in range(1,nLimit):
            res = max(res, sum_digits(a**b))
    return res


timeStart = time.clock()
print(Powerful_Digit_Sum())
print('Time (sec):' + str(time.clock() - timeStart))
answer = '972'


