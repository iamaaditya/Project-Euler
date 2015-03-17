from itertools import combinations
from sys import argv

def solve(l):
    """ solves equal sum for the given list l """
    d = {}
    for j in xrange(len(l)//2):
        for i in combinations(l,j):
            if sum(i) in d:
                if not len(set(i).intersection(set(d[sum(i)]))):
                    return i, d[sum(i)]
            else:
                d[sum(i)] = i
    return False 

def main():
    with open(argv[1]) as f:
        N = f.readline()
        case_count = 0
        for l in f:
            case_count += 1
            vals = map(int, l.split(" ")[1:])
            ans = solve(vals)
            print "Case #" + str(case_count) + ":"
            if ans :
                a1, a2 = ans
                print ' '.join(map(str,a1))
                print ' '.join(map(str,a2))
            else: print "Impossible"

main()
