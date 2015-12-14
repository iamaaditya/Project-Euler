# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 21:16:53 EDT 2015
Updated on Sun Dec 13 12:38:42 EST 2015
@author: aaditya prakash
"""

from time import clock
from itertools import permutations
from itertools import combinations

problem_numbes = '068'
problem_statement = """
Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?
See the website for the figure of the 3-gon ring
"""

def magic_gon_ring(n=5):
    """ solves the magic gon ring problem for "n" polygon"""


    # iterator to store the integers part of ring
    numbers = xrange(1,2*n+1)
    
    # select the inner ring (n) elements
    solution_set = set()
    for inner_elements in combinations(numbers, n):
        remaining_elements = list(set(numbers ) - set(inner_elements))
        for inner_permute in permutations(inner_elements):
            for outside_elements in permutations(remaining_elements):
                check, _, solution_form = Is_Valid_Magic_Ring(inner_permute, outside_elements)
                if check: 
                    start_index = solution_form.index(min(solution_form)) # because we need to start with the smallest value e.g 4
                    required_solution_form = solution_form[start_index:] + solution_form[:start_index]
                    solution_string = ''.join([str(elem) for item in required_solution_form for elem in item])
                    solution_set.add(solution_string)

    # it needs to be checked if the max solution is 16 or 17 digit, but skipping that, as it turns out it is 16 
    print max(solution_set) # not a great idea to store all these values, where we only need the max !
        
        
def Is_Valid_Magic_Ring(inner_elements, outside_elements):
    all_sum = set()
    inner_elements_extended = list(inner_elements) + [inner_elements[0]]     # because it is a cycle !
    solution_form = []
    for i in xrange(len(inner_elements_extended)-1):
        current = inner_elements_extended[i]
        next = inner_elements_extended[i+1]
        all_sum.add(outside_elements[i] + current + next)
        solution_form.append((outside_elements[i],current,next))

    return len(all_sum) == 1, all_sum, (solution_form)

timeStart = clock()
print(magic_gon_ring())
print('Time (sec):' + str(clock() - timeStart))
answer = '6531031914842725'



