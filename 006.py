# -*- coding: utf-8 -*-
"""
Created on Sat Apr 05 01:57:17 2014

@author: aaditya prakash
"""

import utilities
import math

problem_number = '006'
problem_statement = """
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the
sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""

def diff_sum_of_sq_sq_of_sum(parameter):
    """ Returns the difference between the sum of the squares to square of the sum of first 'parameter' natural numbers """
    n = parameter
    sum_of_n = n*(n+1)/2
    square_of_sums = sum_of_n**2
    sum_of_squares = n*(n+1)*(2*n + 1)/6
    diffSS = square_of_sums - sum_of_squares
    return diffSS

print(diff_sum_of_sq_sq_of_sum(100))

answer = '25164150'