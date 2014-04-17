# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 16:28:54 2014

@author: aaditya prakash
"""

import utilities
import math
import time

problem_number = '041'
problem_statement = """
Using words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?
if sum of digits of a word == part of the series tn = n*(n+1)/2 it's called 
triangle number
"""

def Count_Triangle_Words(fileName):
    """ Returns the count of the words in the file 'fileName'
    which are triangle words"""
    
    triLL = [int(i*(i+1)/2) for i in xrange(30)]    
    fIn = file(fileName, "r")
    strLL = fIn.read().split(",")
    count =0
    for word in strLL:
        
        cleanWord = word.strip('"')
        wordVal = sum([ord(i) for i in cleanWord]) - 64*len(cleanWord)
        if(wordVal in triLL): count += 1
    return count

timeStart = time.clock()
print(Count_Triangle_Words('words.txt'))
print('Time (sec):' + str(time.clock() - timeStart))
answer = '162'



