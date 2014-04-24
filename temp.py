# -*- coding: utf-8 -*-
"""
Created on Thu Apr 03 22:29:02 2014

@author: owner2
"""
import utilities as uu
import EXTUtilities as ex
import math

import time

import utilities as u

import time



#import numpy as np

#print(1 + Fraction(1,2 + Fraction(1,2+Fraction(1,2))))

n =5521

dx,dy = 1,0            # Starting increments
x,y = 0,0              # Starting location
#myarray = [[None]* n for j in range(n)]
mydic = {}
dl = [49,25, 9, 1,5, 17, 37, 31, 13,3,1,7, 21, 43]
dlN = []
dlN.append(n**2)
prevdy = 0
for i in range(n**2, 0, -1):

    #myarray[x][y] = i
    mydic[(x,y)] = i
    nx,ny = x+dx, y+dy
    if 0<=nx<n and 0<=ny<n and (nx,ny) not in mydic: #myarray[nx][ny] == None:
        x,y = nx,ny
    else:
        #print('**************', i, x, y, dx, dy, nx, ny)
        dx,dy = -dy,dx
        x,y = x+dx, y+dy
    #if(i in dl): print('*', end="")
    #print(i, x, y, dx, dy, nx, ny)
    if(prevdy != dy):
        if(prevdy == -1):
            dlN.append(i-1)
        else:
            dlN.append(i)
        #print(i, x, y, dx, dy, nx, ny)
    prevdy = dy


#print(myarray)


#a = np.matrix(myarray)
#e = np.fliplr(a)
#print(a)
#diae = np.concatenate((np.diag(a), np.diag(e)))

diae = dlN

totalLen = len(diae)-1

pr = filter(uu.isPrimeFast, diae)

#print(sorted(diae))
#print(sorted(dlN))
#print(sorted(diae)==sorted(dlN))
prLen = len(list(pr))

print(float(prLen)/totalLen, n )



