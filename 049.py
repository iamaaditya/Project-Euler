"""
Created on 4/22/14 3:27 PM

@author: aaditya prakash

"""

import time
from utilities import isPrimeFast
from itertools import permutations

problem_number = '0'

problem_statement = """
find three four digit number which are permutations of each other and are equidistant (a-b = c-b)
and all three are primes
"""


def Prime_Permutations():
    """
    Returns all the four digit numbers which have prime permutations and are equidistant to each other
    """

    results = []

    for num in range(1000,9999+1):
        lP = []
        for s in permutations(str(num)):
            n = int(''.join(s))
            if(isPrimeFast(n)): lP.append(n)

        lDic = {}
        for i in range(len(lP)):
            for j in range(i+1, len(lP)):
                a = lP[i]
                b = lP[j]

                d = abs(a-b)
                c = a - d
                #print(i,j,lP[i], lP[j], d, "*****")

                if(d not in lDic):
                    lDic[d] = j
                elif(lDic[d]==i and (a-d) in lP and a!=lP[j] and (a-d) != a and (a-d) != b):
                    if( a < 1000 or b < 1000 or c < 1000): continue
                    res = str(c) + ' ' + str(a) + ' ' + str(b)
                    if res not in results : results.append(res)
    return results


timeStart = time.clock()
print(Prime_Permutations())
print('Time (sec):' + str(time.clock() - timeStart))
answer = '296962999629'


