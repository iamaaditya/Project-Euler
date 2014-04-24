"""
Created on 4/24/14 2:02 AM

@author: aaditya prakash

"""

import utilities as u
import time
import itertools
from fractions import Fraction

problem_number = '057'

problem_statement = """
In the first one-thousand expansions of sqrt(2),
how many fractions contain a numerator with more digits than denominator?
"""

gl = 8
def recur():
            global gl
            gl -= 1
            if(gl<1):
                return 2
            return 2 + Fraction(1,recur())

def Square_Root_Convergent(nLimit=1000):
    """
    Returns the number of fractions of expansion of sqrt(2) where
    the nubmerator is greater than denominator uner nLimit expansions
    """
    totalCount = 0
    global gl
    while gl < 1001:

        frac = (1 + Fraction(1,recur()))
        num = frac.numerator
        den = frac.denominator
        if(len(str(num)) > len(str(den))): totalCount += 1

        gl += 1
    return totalCount


timeStart = time.clock()
print(Square_Root_Convergent())
print('Time (sec):' + str(time.clock() - timeStart))
answer = '153'


