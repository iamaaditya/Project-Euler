# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 23:16:51 EST 2015
Updated on Mon Jan  4 22:53:53 EST 2016 

@author: aaditya prakash
"""
from __future__ import division
from time import clock
from math import exp, sqrt, pi

problem_number = '078'
problem_statement = """
Find the least value of n for which p(n) is divisible by one million, where p(n) is the number of ways a coin can be partitioned, similar to 76 with integer partition
"""


def solve():
    i = 1 
    while True:
        if generating_fn_integer_partition(i) % 1000000 == 0 : return i
        i += 1

def pentagonal(n):
    """ returns the nth pentagonal number """
    return int((3 * n * n - n ) / 2)

sols = {}
def generating_fn_integer_partition(n):
    if n < 0: return 0
    if n == 0 : return 1
    global sols # used to memoize the solutions

    if n in sols: return sols[n]

    ans = 0
    i = 1
    while True:
        ip = pentagonal(i)
        sign = int( (-1)**(i+1) )
        
        ans += sign * generating_fn_integer_partition(n - ip)
        if i > 0: i *= -1
        else: i = -1*i +  1

        if ip > n: break
    sols[n] = ans
    return ans

timeStart = clock()
print solve()
print('Time (sec):' + str(clock() - timeStart))
answer = '55374'


# NOT USED, for informational purpose
def upper_bound(k):
    """Ramanujan's upper bound for number of partitions of k"""
    return int(exp(pi*sqrt(2.0*k/3.0))/(4.0*k*sqrt(3.0)))

sums_dict = {}
def sum_i_to_n(n,i):
    """ this function recursively calculates, number of ways to partition n using numbers less than and equal to i """
    global sums_dict
    if (n,i) in sums_dict:
        return sums_dict[(n,i)]
    sum = 0
    if i <= 1 or n <= 1: 
        return 1
    for l in xrange(i, 0, -1):
        if l > n: continue
        ans = sum_i_to_n(n-l, min(l,n-l))
        sums_dict[(n-l,min(l,n-l))] = ans
        sum += ans
    return sum



