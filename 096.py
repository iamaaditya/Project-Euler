# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 12:35:57 EST 2016

@author: aaditya prakash
"""

from __future__ import division
from math import sqrt
from itertools import product
from time import clock

problem_number = '096'
problem_statement = """ Solve SuDoKu """

def FindEmptyPosition(mat, i, j):
    for row, col in product(xrange(size), xrange(size)):
            if mat[row][col] == 0: return row,col
    return -1, -1 # do not return 0, 0, as it is one of the valid positions



def CheckConstraints(mat, row, col, i):

    # check row
    if i in mat[row] : return False

    # check col
    if i in [c[col] for c in mat] : return False

    # check the block
    BoxX, BoxY = size_rt *(row//size_rt ), size_rt  *(col//size_rt )
    for x,y in product(range(BoxX, BoxX+size_rt ), range(BoxY, BoxY+size_rt )):
            if mat[x][y] == i:
                    return False

    return True

def solve_sudoku(mat, row=0, col=0):
    """ for the given SuDoKu in Numpy Matrix type, returns solved SuDoKu"""
    row, col = FindEmptyPosition(mat, row, col)

    if row == -1: return True # all the positions have been successfully filled !

    for i in xrange(1,size+1): # numbers to fill 
        if (CheckConstraints(mat, row, col, i)) :
            mat[row][col] = i
            if solve_sudoku(mat, row, col) : return True
            mat[row][col] = 0 # fix the position if this step did not lead to success !

    return False


def read_file(file_name, size):
    mats = []
    mat = []
    for line in open(file_name).read().splitlines():
        if line[0] == 'G': 
            mats.append(mat)
            mat = []
            continue

        mat.append(map(int, list(line)))
    mats.append(mat)
    return mats[1:]


def return_top_three_of_sudoku(mat):
    solve_sudoku(mat)
    return 100*mat[0][0] + 10*mat[0][1] + mat[0][2]

timeStart = clock()
size = 9 # this valriable can be changed for other sized sudokus
size_rt = int(sqrt(size))
mats = read_file('./files/p096_sudoku.txt', size)
print sum(map(return_top_three_of_sudoku, mats))

print('Time ():' + str(clock() - timeStart))
answer = '24702'



