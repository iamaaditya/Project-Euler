import time
import itertools
from utilities import isPrime



n=7
dx,dy = 1,0            # Starting increments
x,y = 0,0              # Starting location
myarray = [[None]* n for j in range(n)]
for i in range(n**2, 0, -1):
    myarray[x][y] = i
    nx,ny = x+dx, y+dy
    if 0<=nx<n and 0<=ny<n and myarray[nx][ny] == None:
        x,y = nx,ny
    else:
        dx,dy = -dy,dx
        x,y = x+dx, y+dy

print(myarray)