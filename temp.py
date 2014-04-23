# -*- coding: utf-8 -*-
"""
Created on Thu Apr 03 22:29:02 2014

@author: owner2
"""
import utilities as uu
import EXTUtilities as ex
import math

import time

import utilities as u

import time
from math import sqrt
import itertools
from itertools import permutations
from itertools import combinations
from scipy.misc import factorial

timeStart = time.clock()
N = 100
fact = [1] * (N+1)
for i in range(2, N+1):
    fact[i] = fact[i-1] * i

def choose(n, r):
    return (fact[n]/fact[r]/fact[n-r])

print (sum(sum(1 if (choose(n,r) > 1000000) else 0 for r in range(0,n+1)) for n in range(0,N+1)))


print('Time (sec):' + str(time.clock() - timeStart))