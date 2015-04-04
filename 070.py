# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 22:55:12 EDT 2015

@author: aaditya prakash
"""

from __future__ import division
from utilities import PrimeRange
from EXTUtilities import totientsbelow
from math import ceil
from math import sqrt
from time import clock

problem_number = '070'
problem_statement = """
Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
"""

def sort_str(n):
    return ''.join(sorted(str(n)))

def check_totient_permuation(n,tot):
    return sort_str(n)== sort_str(int(tot))

def totient_permuation_filtered(n):
    """ finds the number such that its totient function of which is its permuation and ratio of number to totient is min"""
    smallest_ratio = 2
    smallest_n = 0
    ns = int(ceil(sqrt(n)))
    pl = PrimeRange(ns-2000, ns+2000)
    for a in pl:
        for b in pl:
            i = a * b
            if i > 10**7 : continue
            tot = (a-1)*(b-1)
            if check_totient_permuation(i, tot): 
                ratio_n_phi = i/tot
                if ratio_n_phi < smallest_ratio:
                    smallest_ratio = ratio_n_phi
                    smallest_n = i
    return smallest_n

def using_totients_below(n):
    """ finds the number such that its totient function of which is its permuation and ratio of number to totient is min"""
    totient_iterator = totientsbelow(n)
    smallest_i = 2
    for i in totient_iterator:
        n = i[0]
        tot = i[1]
        if check_totient_permuation(n, tot): 
            # print i, i[0]/i[1]
            ratio_n_phi = n/tot
            if ratio_n_phi < smallest_i:
                print n, tot, ratio_n_phi
                smallest_i = ratio_n_phi

timeStart = clock()
print(totient_permuation_filtered(10**7))
# print(using_totients_below(10**7))
print('Time (sec):' + str(clock() - timeStart))
answer = '8319823'



