# Project Euler problem 61
from itertools import product
from sys import argv
from itertools import cycle

def make_polygon(sides):
    n = 1
    while True:
        if sides == 3:
            yield n * (n + 1) / 2
        elif sides == 4:
            yield n * n 
        elif sides == 5:
            yield n * (3*n - 1) / 2
        elif sides == 6:
            yield n * (2*n - 1)
        elif sides == 7:
            yield n * (5*n - 3) / 2
        elif sides == 8:
            yield n * (3*n - 2)
        else:
            raise Exception("Incorrect sides entered")
        n += 1


polygon = [make_polygon(i) for i in xrange(3,9)]
values, first_two , last_two = {}, {}, {}

for index, i in enumerate(polygon):
    #first_two[index] = []
    #last_two[index] = []
    values[index] = []

for j in xrange(1000):
    for index, i in enumerate( polygon ):
            v  = i.next()
            if v > 999 and v < 10000: 
                #first_two[index].append(v // 100) # first two digits
                #last_two[index].append(v % 100) # last  two digits
                values[index].append((v//100, v%100))

#for k in first_two:
    #print k, first_two[k], last_two[k]

#print values[0][0][~0]
depth = range(0,len(polygon))

def rec_find(d, p, ori):
    """ recursively find the if part of element is in another dict """
    global depth
    global ans
    try:
        depth.remove(d)
        #print "removing ... " , d
    except ValueError:
        #print "-"*200
        #print depth
        return
        pass

    #print "*>>>", d, p, ori
    if not depth:
        #print "returning"
        return  
    for k in depth:
        #if k == d : continue
        found = False
        for v in values[k]:
            if ori == v[1]: 
                rec_find(k, 0, v[0])
                
                ans.append( (ori, k, v))
                #print p
                #print ori, k, v
                #return str(k) + str(v) + "*" + str(rec_find(k, p, v[p]))
                    
            #else:
                #return 0
k = 0
#rec_find(k,p,82)
#print values[2][0][0]
for i in values:

    for v in values[i]:
        #p = 0
        depth = range(0,len(polygon))
        ans = []
        #p = 0 if p else 1
        rec_find(i,0,v[0])
        #print ans
        #p = 0 if p else 1
        if len(ans) >= 5 : #and v[p] == ans[0][2][p] :
            all_poly = []
            unique_vals = set()
            all_poly.append(i)
            for item in ans: 
                all_poly.append(item[1])
                unique_vals.add(item[2])
            if len(unique_vals) < len(ans):
                continue
            #print all_poly
            
            #if len(all_poly) == len(range(6)): 
            if set(all_poly) == set(range(len(polygon))): 
                #print all_poly
                #print "i:" , i, "v:", v
                #if v[1] == ans[4][2][0]:
                    #print "FOUND **** "
                for a in ans:
                    d = ""
                    for vi in values[a[1]]:
                        #print ":", vi
                        if vi[0] == v[1]:
                            d = str(vi)
                        #pass
                        #break
                    print a[2], a[1], "****" if a[2][0] == v[1] else "!", d
                print v, i
                print "-"*200
    #break
        #rec_find(k,1,v[1])

#print values[0]

