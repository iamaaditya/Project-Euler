# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 00:04:34 EST 2016

@author: aaditya prakash
"""

from __future__ import division
from time import clock

problem_number = '102'
problem_statement = """
find the number of triangles for which the interior contains the origin.
"""

# point inside triangle using same side approach as described here
# http://www.blackpawn.com/texts/pointinpoly/
# Uses 3D co-ordinate system

def cross_product(a,b):
    return (a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0])

def dot_product(a,b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def minus_points(a,b):
    return (a[0]-b[0], a[1]-b[1], a[2]-b[2])

def same_side(p1, p2, a, b):
    cp1 = cross_product(minus_points(b,a), minus_points(p1,a))
    cp2 = cross_product(minus_points(b,a), minus_points(p2,a))

    if dot_product(cp1, cp2) >= 0: return True

    return False


def solve(points):
    origin = (0,0,0)
    a,b,c = points
    if same_side(origin, a,b,c) and same_side(origin,b, a, c) and same_side(origin, c, a, b): return True

    return False

def readfile(fileName):

    points = []
    for line in open(fileName).readlines():
        values =  map(int, line.split(','))
        a = values[0], values[1], 0
        b = values[2], values[3], 0
        c = values[4], values[5], 0
        points.append((a,b,c)) 
    return points



timeStart = clock()
print len(filter(solve, readfile('./files/p102_triangles.txt')))
print('Time (sec):' + str(clock() - timeStart))
answer = '228'



