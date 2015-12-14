# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 20:27:39 EST 2015

@author: aaditya prakash
"""

from __future__ import division
from time import clock
from collections import Counter
import numpy as np


problem_number = '075'
problem_statement = """
Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly 
one integer sided right angle triangle be formed?
"""

###################################################################################
# Generating all pythagorean triples from
# http://stackoverflow.com/questions/575117/generating-unique-ordered-pythagorean-triplets
def gen_prim_pyth_trips(limit=None):
    u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = np.mat(' 1  2  2;  2  1  2; 2 2 3')
    d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        # yield from m # changes from Python 3 to 2
        for mi in m:
            yield mi
        m = np.dot(m, uad)

def gen_all_pyth_trips(limit):
    for prim in gen_prim_pyth_trips(limit):
        i = prim
        for _ in range(limit//prim[2]):
            yield i
            i = i + prim
###################################################################################

def solve_singular_triplets(Limit):
    ll = list(gen_all_pyth_trips(Limit//2))
    sol_counter = Counter()
    for a,b,c in ll:
        if a+b+c <= Limit:
            sol_counter[a+b+c] += 1

    print len([k for k,v in sol_counter.iteritems() if v == 1])

timeStart = clock()
print solve_singular_triplets(1500000)
print('Time (sec):' + str(clock() - timeStart))
answer = '161667'



