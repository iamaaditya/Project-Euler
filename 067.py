# -*- coding: utf-8 -*-
"""
Created on Wed Apr 09 21:25:48 2014

@author: aaditya prakash
"""

import utilities
import math
import time

problem_number = '067'
problem_statement = """
Find the maximum total from top to bottom in triangle.txt 
**Same problem as 018 just larger triangle
"""

def MaximumTopBottom(strMatrix):
    lstRows =strMatrix.split('\n')
    
    bigList = []   
    for l in lstRows:
        lstVals = map(int, l.split(' '))
        #map(int, lstVals)
        bigList.append(lstVals)
    #print(bigList)
    maxSum = 0
    
    for i in range(len(bigList)-2,-1,-1):
        for j in range(len(bigList[i])):
            bigList[i][j] += max(bigList[i+1][j], bigList[i+1][j+1])
    
    
    return bigList[0][0]            


timeStart = time.clock()
fileInput = open("triangle.txt", "r")
strMatrix = fileInput.read()
strMatrix = strMatrix[:-1]
print(MaximumTopBottom(strMatrix))
print('Time (sec):' + str(time.clock() - timeStart))
answer = '7273'



