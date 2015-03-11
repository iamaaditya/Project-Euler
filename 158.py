from scipy.misc import comb

def combinations(n):
    ans = 0
    for i in xrange(1,n+1):
        ans += comb(n,i)-1
    return ans

answers = []
for i in xrange(27):
    total_combinations = combinations(i)*comb(26,i)
    print i, total_combinations
    answers.append(total_combinations)

print "final answer", max(answers)
