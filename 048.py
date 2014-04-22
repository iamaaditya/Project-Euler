"""
Created on 4/22/14 3:20 PM

@author: aaditya prakash

"""
import time

problem_number = '048'

problem_statement = """
Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""


def Self_Powers(n=1000,x=10):
    """
     Returns the last x digits of 1^1 + 2^2 + 3^3 + ... n^n
    """
    return str(sum([x**x for x in range(1,n+1)]))[-x:]




timeStart = time.clock()
print(Self_Powers())
print('Time (sec):' + str(time.clock() - timeStart))
answer = '9110846700'


