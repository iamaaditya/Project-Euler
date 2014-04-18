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


s = '1'

for i in range(len(s)):
    print s[i:] + s[:i]



print('Time (sec):' + str(time.clock() - timeStart))
