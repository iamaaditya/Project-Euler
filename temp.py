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

from time import time
from math import sqrt

from itertools import permutations
from itertools import combinations


#121313
#[121313, 222323, 323333, 424343, 525353, 626363, 828383, 929393]
import itertools

ss = '121313'
a = 2
b = 4

ls = list(ss)
#itertools.product([i for i in range(len(ss))], [i for i in range(len(ss))], [i for i in range(len(ss))]):
for a,b,c in [[0,2,4]]:
    #print(a,b,c)
    count = 0
    for d in '0123456789':
        ls[a], ls[b] , ls[c]= d, d, d
        num = int(''.join(ls))
        print(num, uu.isPrimeFast(num))
        if(uu.isPrimeFast(num)):
            count +=1
            #print(num)
        # else:
        #     print(num, d)
        if(count >= 8):
            print(count, a, b, c,d, num)
# c = '12342522233'
# for d in ex.list_duplicates(c):
#     print(d)