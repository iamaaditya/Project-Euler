from __future__ import division
from math import floor
from math import sqrt
from utilities import  is_square


def root_fraction(a,b,c):
    m = int(floor( (sqrt(a) + b) / c) )
    a_ = a
    b_ = -1*(b - m*c)
    c_ = a - b_**2
    if c_ % c == 0:
        c_ = c_ / c
    else:
        a *= c
        b *= c

    return a_,b_,c_,m

def get_recurring_decimals(a, total_digits):
    b = int(floor(sqrt(a)))
    c = a - b**2
    ans = []
    for i in xrange(total_digits):
        a,b,c,m =  root_fraction(a,b,c)
        ans.append(m)
    return ans

def find_len_recurring(l, total_digits,rep_count):
    m = l[:]
    for i in xrange(1,int(total_digits/rep_count)):
        s, r = m[:i], m[i:]
        succ_count = rep_count 
        for index in xrange(1,int(len(r)/len(s))):
            index_start = index*len(s)
            index_end = index_start + len(s)
            rl =  r[index_start:index_end]
            #print rl, s
            if s == rl: 
                succ_count -= 1
            else:
                break
            if not succ_count:
                return i

def solve():
    total_count = 0
    for i in xrange(2,10000+1):
        if is_square(i): continue
        decimals = get_recurring_decimals(i, 3000)
        #print decimals[:20]
        res = find_len_recurring(decimals, 3000, 10)
        if res:
            if res % 2 == 1: total_count += 1
    return total_count

print solve()


