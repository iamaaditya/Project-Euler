"""
Created on 4/22/14 4:04 PM

@author: aaditya prakash

"""
import time
import utilities as u

problem_number = '050'

problem_statement = """
Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""


def Consecutive_Prime_Sum(n=1000000):
    """
    Returns the prime below 'n' which can be written as the sum of most consecutive primes
    """
    primeSeed = 1
    largest = 0
    largestN = 0
    result = 0

    while True:
        prevPrimeSeed = primeSeed
        primeSeed +=1
        prevLargest = largest
        prevLargestN = largestN

        iterPrime = u.Prime(primeSeed)


        p = next(iterPrime)
        sumP = 0
        i = 0

        while True:
            #print(i, p, sumP)
            if( sumP + p < n):
                sumP += p
                i += 1
            else: break
            if(u.isPrimeFast(sumP)):
                largest = sumP
                largestN = i

            p = next(iterPrime)
            #i += 1
        #print("*****", sumP, i, prevLargest, prevLargestN, largest, largestN , primeSeed, prevPrimeSeed)

        # this is very tricky because the function is not convex, highest sum for a particular range of
        # prime seed does not mean that is the global maxima. (which is surprisingly but not so cool !!)
        if(largestN > prevLargestN): result = max(result, largest)
        if i <= prevLargestN: return result

timeStart = time.clock()
print(Consecutive_Prime_Sum())
print('Time (sec):' + str(time.clock() - timeStart))
answer = '997651'


