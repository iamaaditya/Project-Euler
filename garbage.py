import ctypes as c
from random import randint

count_list = []
for i in xrange(1000000000):
    x = 0
    count = 0
    #print ""
    while True:
        x = x | randint(0,2**32)
        count += 1
        #print count,
        #print x
        if x == 2**32-1: break
    count_list.append(count)

print sum(count_list),len(count_list)
#print count_list

