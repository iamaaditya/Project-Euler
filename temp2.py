# -*- coding: utf-8 -*-
"""
Created on Sat Apr 05 00:04:53 2014

@author: aaditya prakash
"""

import utilities
import math

import itertools

alphabet = ['0','1','2','3', '4', '5', '6', '7', '8', '9']
ns = ''.join(alphabet)
for p1, p2, prod in [[int(ns[0:a]), int(ns[a:b]), int(ns[b:])] for a, b in [(2, 5), (1, 5)]]:
    print p1, p2, prod, a, b