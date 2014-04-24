# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 16:11:22 2014

@author: aaditya prakash

Collection of extemely useful python functions, collected from internet

*** These are not written by me and I have pointed the source for each
"""

from functools import reduce

#PRIMALITY TESTING

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite

def is_prime(n, _precision_for_huge_n=16):
    """ Primality testing, uses Miller-Rabin TEST 
     This is optimzied verstion, which is deterministic 
     upto  341550071728321  and beyond that it is probabilitic 
     source: http://rosettacode.org/wiki/Miller-Rabin_primality_test#Python"""
        
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])


_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]


def is_square(apositiveint):
  """ Efficient and non floating reliant code to check if a given
  number is a perfect square
  Source: Alex Martelli 
  http://stackoverflow.com/questions/2489435/how-could-i-check-if-a-number-is-a-perfect-square """
  #print(apositiveint)
  if(apositiveint==1): return True
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    try:
        x = (x + (apositiveint // x)) // 2
    except ZeroDivisionError:
        return False

    if x in seen: return False
    seen.add(x)
  return True

def find_all(a_str, sub):
    """ Find all instnaces of a given substring in a given string
    http://stackoverflow.com/questions/4664850/find-all-occurrences-of-a-substring-in-python
    """
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

def list_duplicates(seq):
  """ Returns the duplicate items in the list
   http://stackoverflow.com/a/9836685/1189865
  """

  seen = set()
  seen_add = seen.add
  # adds all elements it doesn't know yet to seen and all other to seen_twice
  seen_twice = set( x for x in seq if x in seen or seen_add(x) )
  # turn the set into a list (as requested)
  return list( seen_twice )

def sum_digits(n):
    """
    Function that returns the sum of the digits,
    This is much faster than converting the int to str and using map
    http://stackoverflow.com/a/14940026/1189865
    """
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r

# following three functions
# source: http://stackoverflow.com/a/147539/1189865
def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""
    return reduce(lcm, args)