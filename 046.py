"""
Created on 4/21/14 11:37 PM

@author: aaditya prakash

"""

import utilities as u
import time
import EXTUtilities as EXT
import math

problem_number = '046'
problem_statement = """
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

def GoldBach_Other_Conjecture():
    """ Returns the  smallest value which breaks the
    Goldbach's other Conjecture, i.e every odd composite can be written as the sum of a prime and
    twice a square
    """
    iterPrime = u.Prime()

    lPrime = [next(iterPrime) for x in range(30000)]

    #Brute Force
    for comp in range(5, 999999, 2):
        if u.isPrimeFast(comp): continue
        for prim in lPrime:
            if prim > comp: break
            #print(comp, prim)
            if(EXT.is_square((comp-prim)/2)):
                #print(comp, prim, comp - prim, (comp-prim)/2)
                break
            if(prim == lPrime[-1]):
                print(comp, prim, comp - prim, (comp-prim)/2)
                return comp
    return False


def GoldBach_Other_Conjecture_FAST():
    """
     Faster implementation of Goldbach
    """
    comp = 31
    while True:
        comp +=2
        if u.isPrimeFast(comp): continue

        uLimit = int(math.ceil(math.sqrt(comp/2)))

        for i in range(1, uLimit):
            v = comp - 2*i*i
            if(u.isPrimeFast(v)): break
            if(i==uLimit-1):
                return comp

timeStart = time.clock()
print(GoldBach_Other_Conjecture_FAST())
print('Time (sec):' + str(time.clock() - timeStart))
answer = '5777'


