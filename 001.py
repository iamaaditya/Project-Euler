# -*- coding: utf-8 -*-
"""
Created on Thu Apr 03 22:29:02 2014

@author: aaditya prakash
"""


problem_number = '001'
problem_statement = 'If we list all the natural numbers below 10 that are' \
                    ' multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. ' \
                    'Find the sum of all the multiples of 3 or 5 below 1000.'


print(problem_statement)



def sum_multiples_below_x_y(parameter, x, y):
    sum = 0
    for i in range(1,parameter):
        if( i % x == 0 or i % y == 0) : sum += i
    return sum

print('\nAnswer :')
print(sum_multiples_below_x_y(1000, 3, 5))

answer = '233168'

