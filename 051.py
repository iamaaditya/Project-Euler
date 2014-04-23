"""
Created on 4/22/14 9:57 PM

@author: aaditya prakash

"""
import utilities as u
import EXTUtilities as ex
import time
from itertools import product
problem_number = '051'

problem_statement = """
Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""



def repPrime(d):
    if not '*' in d:
        return 1 if u.isPrime(int(d)) else 0
    else:
        c=0
        for i in [str(i) for i in range(1 if d[0]=='*' else 0,10)]:
            if u.isPrime(int(d.replace('*',str(i)))):
                c+=1
    return c

def Prime_Digit_Replacement_FAST(n=5):
    for i in range(n):
        for p in product(['*']+[str(k) for k in range(10)],repeat=i+1):
            #print(p)
            if p[0]=='0':
                continue
            for j in [1,3,7,9]:
                s=''.join(p)+str(j)
                c=repPrime(s)
                if c>=8:
                    return s

timeStart = time.clock()
print(Prime_Digit_Replacement_FAST())
print('Time (sec):' + str(time.clock() - timeStart))
answer = '121313'


