"""
Created on 4/23/14 5:36 PM

@author: aaditya prakash

"""

import utilities as u
import time

from scipy.misc import factorial

import math

problem_number = '0'

problem_statement = """
How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
"""

def Combinatoric_Selection_BRUTE(Limit=1000000, nLimit=100):
    """ Returns the number of elements in choose(nLimit,0:nLimit), which are greater than Limit
    """
    count = 0
    for n in range(1,nLimit+1):
        for r in range(2,n-1):
            x = factorial(n, exact=True)/(factorial(r, exact=True)*factorial(n-r, exact=True))
            if (x > Limit): count += 1

    return count

def Combinatoric_Selection_FAST(Limit=1000000, nLimit=100):
    """ Returns the number of elements in choose(nLimit,0:nLimit), which are greater than Limit
     ** This Solution does not use nCr formula or Factorial. Direct computation. Super Fast **
    """
    result = 0
    for n in range(23, nLimit+1):
        num = n
        p = Limit/num
        count = 1
        while p > 1:
            num -= 1
            count += 1
            p = p*count/num
        result += n-2*count + 1
    return result


timeStart = time.clock()
print(Combinatoric_Selection_FAST())
print('Time (sec):' + str(time.clock() - timeStart))
answer = '4075'


