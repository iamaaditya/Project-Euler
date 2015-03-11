from scipy.misc import comb
from string import lowercase

def count_lexico_simple(n):
    """ Project Euler # 158 """

    count = 0
    remaining_chars = n - 2  # -2 for the inclined line (/) 

    for i in xrange(remaining_chars+1): 
        before, after = i, remaining_chars-i
        for i,f in enumerate(lowercase):
            for j, s in enumerate(lowercase[i+1:]):
                term = 0
                if before and after:
                    term = (lowercase.index(s) - lowercase.index(f) -1 )
                num_of_chars_greater_than_f = 25 - lowercase.index(f)- 1 # -1 for the second char count, 25 because these index start from 0
                num_of_chars_smaller_than_s = lowercase.index(s)-1 # -1 for the first char count
                count += comb(num_of_chars_greater_than_f, before) * comb(num_of_chars_smaller_than_s, after) - term

    return count
        
answers= []
for i in xrange(27):
    ans = count_lexico_simple(i)
    print(i, ans)
    answers.append(ans)
print(max(answers))
