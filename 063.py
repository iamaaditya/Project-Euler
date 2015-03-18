from itertools import product
from itertools import combinations
from itertools import permutations

ans = set()
for i,j in product(xrange(1,10),xrange(1,500)):
    nth = i**j
    if len(str(nth)) == j:
        ans.add(nth)

print len(ans)
