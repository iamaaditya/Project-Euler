from __future__ import division
a =100 
b =100 
c =100 


for i in xrange(1,a):
    for j in xrange(1,b):
        for base in xrange(1,c):
            f = i / j
            second = base * f  
            if second - int(second) != 0: continue
            
