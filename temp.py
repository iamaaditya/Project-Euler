# -*- coding: utf-8 -*-
"""
Created on Thu Apr 03 22:29:02 2014

@author: owner2
"""
import utilities as uu
import math

import time

import numpy as np

import itertools
from itertools import permutations
from itertools import product
from itertools import combinations
from fractions import gcd
from EXTUtilities import is_prime


timeStart = time.clock()
count = 0
for i in xrange(100000000):
    if(uu.isPrime(i) and not is_prime(i)): print i
    
#print count

print('Time (sec):' + str(time.clock() - timeStart))

#print "***"
#
#timeStart = time.clock()
#count = 0
#for i in xrange(1000000):
#    if(uu.isPrime(i)): count += 1
#    
#print count

print('Time (sec):' + str(time.clock() - timeStart))
