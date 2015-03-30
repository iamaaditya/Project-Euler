# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 22:25:17 EDT 2015

@author: aaditya prakash
"""
from __future__ import division
import utilities
import math
from time import clock
from fractions import Fraction
from utilities import SumDigits
from itertools import cycle

problem_number = '066'
problem_statement = """
Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained., eqn is x^2 - D*y^2 = 1
"""

def frac(b, term, v):
    return Fraction(b, term + v)

def sqrt_convergent(n):
    """ generates the convergent for the sqrt(n) """
    l = Continued_Fraction_number_generator(n)
    a = l.next()
    fg = Fraction(1,l.next())
    while True:
        newFraction = a + fg
        yield newFraction.numerator, newFraction.denominator
        fg = frac(1, fg,l.next()) 

def Continued_Fraction_number_generator(n):
    """ for the sqrt(n), generates the number which goes on the CF formula 1 + 1/ x + ( 1/ x + ....))) """
    a = n
    b = 0
    c = 1
    while True:
        if c == 0: c = 1
        alpha = int(math.floor((math.sqrt(a)+b)/c))
        yield alpha
        bnew = c*alpha - b
        cnew = a-bnew**2
        anew = a
        if cnew % c == 0:
            cnew = cnew / c
        else:
            anew = a * c
            bnew = bnew * c
        a,b,c = anew,bnew,cnew

def Pells_Eq_Solution(D):
    """ returns the smallest solution for the Quadratic Pells Equation for a given D"""
    ds = sqrt_convergent(D)
    for i in xrange(200):
        x,y = ds.next()
        if x**2 - D*(y**2) == 1:
            return x,y
    return 0,0
    
def solve_66():
    """ solves the problem 66 of the project euler, returns the D <= 1000 for which 
    minimal sol for x has the largest value in x """
    sols = {}
    for D in xrange(2,1001):
        sols[D], v = Pells_Eq_Solution(D)
    for s in sorted(sols, key=sols.get, reverse=True):
        print "ans (D):", s, "Value of x:", sols[s]
        break


timeStart = clock()
solve_66()
print('Time (sec):' + str(clock() - timeStart))
answer = '661'



