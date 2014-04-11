# -*- coding: utf-8 -*-
"""
Created on Sat Apr 05 00:04:53 2014

@author: aaditya prakash
"""

import utilities
import math

import itertools

alphabet = ['0','1','2','3', '4', '5', '6', '7', '8', '9']

combos = itertools.permutations(alphabet, 10)

usable_combos = []
for e in combos:
    usable_combos.append(e)

print usable_combos[1000000-1]