# -*- coding: utf-8 -*-
"""
Created on Fri Apr 04 21:53:54 2014

@author: aaditya prakash
"""

import utilities
import math

problem_number = '004'
problem_statement = """A palindromic number reads the same both ways.
            The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
            Find the largest palindrome made from the product of two 3-digit numbers."""

def largest_palindrome_prod_x_digits(parameter, x):
    """ Returns the Largest Palindrome which is product of two x digits number,
    which is smaller than parameter. Keep parameter equal to (10^x -1) * (10^x -1) for MAX """
    iterPal = utilities.PalindromeReverse(parameter)
    largestX = 10**x
    smallestX = 10**(x-1)
    while True:
        newPal = iterPal.next()
        largestFactor = utilities.LargestFactor(newPal, largestX)
        multiplier = newPal / largestFactor
        if(largestFactor > smallestX and multiplier > smallestX and multiplier < largestX):
            #print(largestFactor, multiplier, smallestX)
            return newPal
        if(iterPal <= 1):
            return 0

print(largest_palindrome_prod_x_digits(999*999, 3))

answer = '906609'