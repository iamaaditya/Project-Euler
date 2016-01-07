# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 23:27:29 EST 2016

@author: aaditya prakash
"""

from time import clock
from numpy import zeros
from numpy import ndarray
from numpy import size

problem_number = '082'
problem_statement = """
Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the left column to the right column.
"""

sols = {}
def sum_path(mat):
    """ Finds the path with the minimal sum in a given matrix, where movement is only right and below"""
    global sols    

    if size(mat) == 0:
        return 0
    if size(mat) == 1:
        return mat[0,0]
    if min(mat.shape[0],mat.shape[1]) == 1:
        return sum(ndarray.flatten(mat))
    if mat.shape in sols:
        return sols[mat.shape]

    ans = mat[-1,-1] + min(sum_path(mat[:,:-1]), sum_path(mat[:-1,:]))
    sols[mat.shape] = ans
    return ans


def read_data(filename):
    """ reads the matrix from a text file 'filename' and stores it into a list of lists """
    mat= []
    with open(filename) as f:
        for line in f:
            mat.append( map(int, line.strip().split(',')))
    
    # this is because numpy matrix requires predefined size
    m = zeros((len(mat),len(mat[0])))
    for i,l in enumerate(mat):
        m[i,:] = l
    return m

timeStart = clock()
# print(sum_path(read_data('testfile')))
print read_data('testfile')
# print(sum_path(read_data('./files/p082_matrix.txt')))
print('Time (sec):' + str(clock() - timeStart))
answer = ''



