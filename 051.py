"""
Created on 4/22/14 9:57 PM

@author: aaditya prakash

"""
import utilities as u

import time

from itertools import permutations
problem_number = '051'

problem_statement = """
Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""



def Prime_Count(sNum):
    if(sNum[0]=='0'): return 0
    sNum = ''.join(sNum)
    asCount = sNum.count('*')
    #print(sNum, asCount)
    count = 0
    for i in [str(i) for i in range(1 if sNum[0] =='*' else 0, 10)]:
        #print(sNum)
        if u.isPrimeFast(int(sNum.replace('*', i))): count += 1
    return count



def Prime_Digit_Replacement():
    result = []
    for num in range(10,100):
        for i in range(1,5):
            asterisk = '*'*i
            for perm in permutations(str(num)+asterisk):
                #print(''.join(perm))
                for lastDigit in '1379':

                    newNum = list(perm)
                    newNum.append(lastDigit)
                    #if(''.join(perm)=='*2*3*'): print(perm, newNum, Prime_Count(newNum))
                    if(Prime_Count(newNum)>=8): return newNum

timeStart = time.clock()
print(Prime_Digit_Replacement())
print('Time (sec):' + str(time.clock() - timeStart))
answer = '121313'


