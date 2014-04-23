import time
import itertools
from utilities import isPrime

def repPrime(d):
    if not '*' in d:
        return 1 if isPrime(int(d)) else 0
    else:
        c=0
        for i in [str(i) for i in range(1 if d[0]=='*' else 0,10)]:
            if isPrime(int(d.replace('*',str(i)))):
                c+=1
    return c

def pr51(n):
    for i in range(n):
        for p in itertools.product(['*']+[str(k) for k in range(10)],repeat=i+1):
            print(p)
            if p[0]=='0':
                continue
            for j in [1,3,7,9]:
                s=''.join(p)+str(j)
                c=repPrime(s)
                if c>=8:
                    return s

time1=time.clock()
print(pr51(5))
print("time = {:f} sec".format(time.clock()-time1))