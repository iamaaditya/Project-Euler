# -*- coding: utf-8 -*-
"""
Created on Sat Apr 05 00:04:53 2014

@author: aaditya prakash
"""

import utilities
import math

import itertools

def check_dif(dif):
    min_n, b, a = 2, 2, 3
    while a * min_n - b <= dif:
        if (dif + b) % a == 0:
            yield (a, b)
        b += 2 + 3 * (min_n - 1)
        min_n += 1
        a = 3 * (min_n - 1)
    return
    
for i in check_dif(10000):
    print i


