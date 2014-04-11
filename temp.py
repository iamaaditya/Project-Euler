# -*- coding: utf-8 -*-
"""
Created on Thu Apr 03 22:29:02 2014

@author: owner2
"""
import utilities as uu
import math

import time

timeStart = time.clock()
def pan(n):
	s=0
	for i in xrange(1,int(n/2)+1):
		if n%i==0:
			s+=i
	if s>n:
		return 1
		
a=[]
b=[]
z=range(1,28124)
for i in xrange(1,28124):
	if pan(i)==1:
		a.append(i)

for i in xrange(len(a)):
	for j in xrange(i,len(a)):
		if (a[i]+a[j])<28124:
			b.append(a[i]+a[j])
print sum(list(set(z)-set(b)))


print('Time (sec):' + str(time.clock() - timeStart))
