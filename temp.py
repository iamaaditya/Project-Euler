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
timeStart = time.clock()


import math



pydict = {}

for m in xrange(23):
    for n in xrange(1, m, 2):
        if gcd(m, n)==1:
            per = 2 * m ** 2 + 2 * m * n
            k = 1
            while per * k <= 1000:
                pydict[per * k] = pydict.get(per * k, 0) + 1
                k += 1

#print(sorted(pydict.get()))
#print sorted(pydict.items(), key=lambda q: q[1], reverse=True)[0]

print sorted(pydict, key=pydict.get, reverse=True)[0]



print('Time (sec):' + str(time.clock() - timeStart))
