"""
Created on 4/24/14 2:56 PM

@author: aaditya prakash

"""

import utilities as u
import time

#import numpy as np
#import scipy as sc

problem_number = '0'

problem_statement = """

"""


def Spiral_Primes():
    n = 9
    dlN = []
    dlN.append(n**2)
    prevdy = 0
    while True:
        n += 2
        dx,dy = 1,0            # Starting increments
        x,y = 0,0              # Starting location
        mydic = {}
        #myarray = [[None]* n for j in range(n)]
        for i in range(n**2, 0, -1):
            #myarray[x][y] = i
            mydic[(x,y)] = i
            nx,ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and (nx,ny) not in mydic: #myarray[nx][ny] == None:
                x,y = nx,ny
            else:
                dx,dy = -dy,dx
                x,y = x+dx, y+dy
            if(prevdy != dy):
                if(prevdy == -1):
                    dlN.append(i-1)
                else:
                    dlN.append(i)
                #print(i, x, y, dx, dy, nx, ny)
            prevdy = dy

        #a = np.matrix(myarray)
        #e = np.fliplr(a)

        #diae = np.concatenate((np.diag(a), np.diag(e)))
        totalLen = len(dlN)-1

        prLen = len(list(filter(u.isPrimeFast, dlN)))

        #print(n, prLen, totalLen, prLen/totalLen)
        if(10*prLen < totalLen):
            print(prLen, totalLen, prLen/totalLen)
            break

    return n

timeStart = time.clock()
print(Spiral_Primes())
print('Time (sec):' + str(time.clock() - timeStart))
answer = ''


