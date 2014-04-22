# -*- coding: utf-8 -*-
"""
Created on Thu Apr 03 22:29:02 2014

@author: owner2
"""
import utilities as uu
import EXTUtilities as ex
import math

import time

#import numpy as np

import itertools
from itertools import permutations
from itertools import product
from itertools import combinations
from fractions import gcd
timeStart = time.clock()


import numpy as np
import math

for i in xrange(20000,90000):
    if ex.is_square(i): print i, math.sqrt(i)

print('Time (sec):' + str(time.clock() - timeStart))
