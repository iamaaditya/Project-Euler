"""
Created on 4/24/14 1:29 AM

@author: aaditya prakash

"""

import utilities as u
import time

problem_number = '055'

problem_statement = """
How many Lychrel numbers are there below ten-thousand?
Lyrchrel Numbers are the numbers which produce palindromic number when added to their reverse
or after several iterations
"""


def Lyrchrel_Numbers(nLimit =10000):
    """
    Returns the number of Lyrchrel Numbers below the nLimit
    """

    countLy = 0
    for n in range(0,nLimit):
        j = n
        for st in range(0, 50):
            n = n+int(str(n)[::-1])
            if(u.IsPalindrome(str(n))):
                countLy += 1
                break

    return nLimit - countLy



timeStart = time.clock()
print(Lyrchrel_Numbers())
print('Time (sec):' + str(time.clock() - timeStart))
answer = '249'


