"""
Created on 4/24/14 5:52 PM

@author: aaditya prakash

"""

import utilities as u
import time

problem_number = '058'

problem_statement = """
In a spiral matrix, 1 as center and moving out clockwise from right, find the size of the matrix which
would have less than 10% of diagonal (both) elements as prime
"""


def Spiral_Primes(pcntLimit=10):
    """
    Returns the smallest dimensions of the circular monotonic matrix which would have
    less than pcntLimit% of the diagonal elements as prime
    """

    ll = [1]
    n = 1
    totalLen = 1
    prLen = 0
    e = ll[-1]
    while True:
        n += 2
        newElements = [e+(n-1)*i for i in range(1,4+1)]
        e = newElements[-1]
        totalLen += 4
        prLen += len(list(filter(u.isPrimeFast, newElements)))

        if(pcntLimit*prLen < totalLen):
            return n





timeStart = time.clock()
print(Spiral_Primes())
print('Time (sec):' + str(time.clock() - timeStart))
answer = '26241'


