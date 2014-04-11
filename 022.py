# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 14:48:26 2014

@author: aaditya prakash
"""

import utilities
import math
import time

problem_number = '022'
problem_statement = """
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

def Total_Name_Scores(strList):
    """ Returns the total of all the name scores of the given list 
    Name score = rank * sum(letters)
    """
    strList.sort()
    totalSum = 0
    for i in range(len(strList)):
        strList[i] = strList[i].replace('"','')
        totalSum += (i+1)*sum([x - 64 for x in map(ord, strList[i])])
    return totalSum

timeStart = time.clock()
fileInput = open("names.txt", "r")
print(Total_Name_Scores(fileInput.read().split(",")))
print('Time (sec):' + str(time.clock() - timeStart))
answer = '871198282'



