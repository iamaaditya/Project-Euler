# -*- coding: utf-8 -*-
"""
Created on Thu Apr 03 23:50:56 2014

@author: aaditya prakash
"""
import re
#import numpy as np
from collections import deque
from itertools import permutations 
import math
from functools import reduce

def is_square(i):
    x = i // 2
    seen = set([x])
    while x * x != i:
        x = (x + (i // x) ) // 2
        if x in seen: return False
        seen.add(x)
    return True

def Fibonacci():
    """ generator function to generate infinite values of fib series """
    a,b = 0,1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


def generate_cube(start):
    """ yields cubes starting from start^3"""
    while True:
        yield start**3
        start += 1

def isPrime(n):
    """ returns true if given number is prime, false otherwise """
    if(n < 2): return False    
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

def isPrimeFast(n):
    """"precondition n is a nonnegative integer postcondition:  return True if n is prime and False otherwise."""
    if n < 2:
         return False;
    if n % 2 == 0:
         # return False
         return n == 2
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

def Prime(number=2):
    """ generator function to generate infinite values of prime numbers starting from 'number' """
    while True:
        if isPrimeFast(number):
            yield number
        number += 1

def PrimeReverse(number):
    """ generator function to generate infinite values of prime numbers starting from 'number' but going lower """
    while True:
        if number < 2:
            yield 2
        elif isPrime(number):
            yield number
        number -= 1

def PrimeList(number):
    """ return a list of all the prime number less then given 'number ' """
    iterPrime = Prime(2)
    primeList = []
    nextPrime = iterPrime.next()
    #primeList.append(nextPrime)

    while nextPrime < number:
        primeList.append(nextPrime)
        nextPrime = iterPrime.next()

    return primeList

def NthPrime(number):
    """ returns the nth prime number, where 'n' = number. 2 is first prime """
    iterPrime = Prime(2)
    for i in range(number):
        nextPrime = iterPrime.next()
    return nextPrime
        
    
    
def isPalindrome(s):
    """ check if the given string is palindrome """
    s = str(s)
    for i in range(len(s)/2+1):
        #print s[i], s[len(s)-1-i]
        if s[i] != s[len(s)-1-i]:
            return False
    return True

def Palindrome(number):
    """ generator function to generate infinite palindrome larger than given number """
    while True:
        if isPalindrome(number):
            yield number
        number += 1

def PalindromeReverse(number):
    """ generator function to generate infinite palindrome smaller than given number in reverse """
    while True:
        if number < 1:
            yield 1
        elif isPalindrome(number):
            yield number
        number -= 1

def LargestFactor(number, parameter):
    """ Returns largest Factor of 'number' smaller than 'parameter' """
    parameter -= 1
    while parameter > 0:
        if(number % parameter == 0):
            return parameter
        parameter -= 1

def PrimeFactors(dictPrime, number):
    """ Returns the prime factors of the given 'number',
    assumes a dict with all prime numbers less then 'number' as key
    updates this dictionary with count of every prime factor """
    d = 2
    while d*d <= number:
        while (number % d) == 0:
            # this inner loop or multiple entries of same prime factor
            dictPrime[d] += 1
            number /= d
        d += 1
    if number > 1:
       dictPrime[number] += 1
    return dictPrime
    
def AllFactors(number):
    """ Returns all the factors of the given number, very effficient code 
    returns SET and is not necessarily monotonic"""
    return set(reduce(list.__add__, 
                ([i, number//i] for i in range(1, int(number**0.5) + 1) if number % i == 0)))

def PrimeFactorsSet(number):
    """ Returns all the factors of the given number, very effficient code
    returns SET and is not necessarily monotonic"""
    #return set(reduce(list.__add__,
    #            ([i, number] for i in range(1, int(number**0.5) + 1) if number % i == 0 )))
    return set( i for i in range(1, int(number//2) + 1) if number % i == 0 and isPrime(i))

def NumberOfPrimeFactors(number):
    lenP = 0
    for i in range(1, int(number//2) + 1):
        if number % i == 0 and isPrime(i):
            lenP +=1
    return lenP

def TriangleNumber(number):
    """ Generator Function to generate Triangle Numbers starting from 'number' """
    while True:
        yield number*(number+1)/2
        number += 1
        
def LengthCollatz(number):
    """ Returns the length of the collatz sequence of given 'number' """
    leng = 1
    while True:
        if(number<=1):
            return leng
        elif(number%2==0): 
            number /= 2
        else:
            number = 3*number + 1
        leng += 1

def SumDigits_slow(Number):
    """ Returns the sum of the digits of a given number """
    return sum(map(int, str(Number)))

def SumDigits(n):
    """ source StackOverflow """
    r = 0
    while n:
        r,n = r + n%10, n / 10
    return r

    
def NumberToWord(Number):
    """ Returns the given number in Word. Number < 100 assumed """
    dicWord = {1:'one', 2:'two', 3:'three',4:'four',5:'five',
                6:'six', 7:'seven',8:'eight',9:'nine', 10:'ten', 11:'eleven',
                12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen',
                17:'seventeen', 18:'eighteen', 19:'nineteen',
                20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty',
                70:'seventy', 80:'eighty',90:'ninety'}
    if(Number in dicWord or Number <= 20): return dicWord[Number]                
    return dicWord[(Number//10)*10] + dicWord[(Number % 10)]
    
def IsAbundant(number):
    """ Returns true if the given 'number' is abundant
    i.e sum of all its factors is > number """
    sumAllFactors = sum(list(sorted(AllFactors(number)))[:-1])
    return sumAllFactors > number
    
def Abundant(number=1):
    """ generator function to generate infinite values of abundant numbers starting from 'number' """
    while True:
        if IsAbundant(number):
            yield number
        number += 1

def Longest_Repeating_Sub_String(strIn):
    largest = ''
    i = 1
    
    while 1:
        m = re.search("(" + ("\w" * i) + ").*\\1.*\\1", strIn)
        if not m:
            break
        largest = m.group(1)
        i += 1
    return largest
    
def Length_Recurring_Cycle(nu, de):
    """ Returns the length of recurring decimal cycle for the fraction
    'nu(merator)'/'de(nominator)' """
    
    x = 10 * nu % de
    count = 0
    y=x
    for c in xrange(de):
        y = 10*y % de
        count += 1
        if(y == x):
            return count
    return 0
    
def Make_Spiral_Matrix(n):
    """ Retuns a Spiral Matrix, of NxN, puts values starting at 1 from
    the center and moves to right clockwise """
    dx,dy = 1,0            # Starting increments
    x,y = 0,0              # Starting location
    myarray = [[None]* n for j in range(n)]
    for i in range(n**2, 0, -1):
        myarray[x][y] = i
        nx,ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<n and myarray[nx][ny] == None:
            x,y = nx,ny
        else:
            dx,dy = -dy,dx
            x,y = x+dx, y+dy
    return np.fliplr(np.matrix(myarray).transpose())
    
def Linear_Combinations(S, n, m):
    """ Returns the total possiblity of making linear combinations of m elements 
    of list 'S' to make a total of 'n' """
    
    if n==0: return 1
    if n<0: return 0
    if m <=0 and n >= 1: return 1
        
    return Linear_Combinations(S, n, m-1) + Linear_Combinations(S, n-S[m], m)
    
def Reduce_Fraction(num, den):
    """ ** USE fractions.Fraction instead **
    Returns the reduced form of the given fraction as 'num' and 'den' 
    assumes num <= den
    """
    
    newNum = num
    newDen = den
    numFactors = sorted(AllFactors(num), reverse=True)[:-1]
    #print(numFactors)
    for i in  range(len(numFactors)):
        f = numFactors[i]
        if (newDen % f == 0 and newNum % f == 0):
            #print 'Before: ' , newNum, newDen, f            
            newNum //= f
            newDen //= f
            #print 'After: ' , newNum, newDen, f            
    return newNum, newDen
    
def IsCircularPrime(num):
    """ Checks if the given number is circular prime
    - all combinations of given number is prime """
    
    a = str(num)
    n = len(a)

    llC = [[a[i - j] for i in range(n)] for j in range(n)]
    
    for l in llC:
        lNum = int(''.join(l))
        if(not isPrime(lNum)): return False 
    return True
    
def Eratosthenes():
	'''Yields the sequence of prime numbers via the Sieve of Eratosthenes.
    ** This code is due to David Eppstein, UC Irvine **     
     '''
	D = {}  # map composite integers to primes witnessing their compositeness
	q = 2   # first integer to test for primality
	while 1:
		if q not in D:
			yield q        # not marked composite, must be prime
			D[q*q] = [q]   # first multiple of q not already marked
		else:
			for p in D[q]: # move each witness to its next multiple
				D.setdefault(p+q,[]).append(p)
			del D[q]       # no longer need D[q], free memory
		q += 1
  
def IsPalindrome(s):
    """ Checks if the given string 's' is palindrome """
    sR = s[::-1]
    return s==sR
    
def IsTrunctablePrime(num):
    """ Checks if the given PRIME number is Trunctable Prime on both direction """
    for i in range(1,len(str(num))):
        if(not isPrime(num//(10**i))): return False
    for i in range(1, len(str(num))):
        if(not isPrime(num % (10**i))): return False
    return True    
    
def Generate_n_Pandigit_Number(n):
    """ Returns a pan digit number containing 1..'n' digits """
    digits = [str(i) for i in xrange(n, 0, -1)]

    for num in permutations(digits):
        yield int(''.join(num))
    
def Generate_n_Pandigit_Number_Prime(n):
    """ Returns a pan digit number containing 1..'n' digits """
    digits = [str(i) for i in xrange(n, 0, -1)]

    for num in permutations(digits, len(digits)-1):
        ln = list(num)
        if('1' not in ln): ln.append('1')
        elif('3' not in ln): ln.append('3')
        elif('7' not in ln): ln.append('7')
        else: continue
        yield  int(''.join(ln))

def Pentagonal_Numbers():
    """ Generator function for pentagonal numbers 
    Pn = n*(3n-1)/2 """
    
    n = 0    
    while True:
        n+= 1
        yield n*(3*n -1)/2

def IsPentagonal(n):
    """ Checks if the given number 'n' is pentagonal """
    check = (math.sqrt(24*n + 1) + 1)/6
    return int(check) == check

def IsTriangular(n):
    """ Checks if the given number 'n' is pentagonal """
    check = (math.sqrt(8*n + 1) - 1)/2
    return int(check) == check
        
def IsHexagonal(n):
    """ Checks if the given number 'n' is hexagonal """
    check = (math.sqrt(8*n + 1) + 1)/4
    return int(check) == check

def totient_function(n):
    """ returns the value of totient function, uses 
    Euler's formula, and vast prime checking methods"""

    if isPrimeFast(n): return n-1
    prime_list = PrimeList(n)
    total = 1
    for p in prime_list:
        if n % p == 0: 
            total *= (1 - 1/p)

    return total*n


