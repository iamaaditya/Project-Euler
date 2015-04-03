# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:30:26 EDT 2015
@author: aaditya prakash
"""

from utilities import GetDigits
from time import clock
from math import factorial

problem_number = '074'
problem_statement = """
How many chains, with a starting number below one million, contain exactly sixty non-repeating terms? Chain means doing factorial of the digits and then summing up to get the next number
"""

chain_length_dict = dict()

def get_chain_length(n):
    """ returns the chain length for given n, uses the dict object to check every step and also populates the value intelligently for all items in the list, instead of only final value """
    numbers_seen = [n]
    chain_length = 1
    while True:
        if n in chain_length_dict :
            chain_length += chain_length_dict[n] -1 
            break
        n = sum([factorial(d) for d in GetDigits(n)])
        if n in numbers_seen: break
        chain_length += 1
        numbers_seen.append(n)

    ch = chain_length
    for nums in numbers_seen:
        if nums not in chain_length_dict:
            chain_length_dict[nums] = ch
        ch -= 1
        
    return chain_length

def get_longest_chain(N):
    """ returns the longest chain under the number N """
    longest_chain = 0
    chains_of_60 = 0
    for i in xrange(2,N):
        if i in chain_length_dict:
            chain_length = chain_length_dict[i]
        else:
            chain_length = get_chain_length(i)
        if chain_length == 60:
            chains_of_60 += 1
    return chains_of_60

timeStart = clock()
print get_longest_chain(1000000)
print('Time (sec):' + str(clock() - timeStart))
answer = '402'



