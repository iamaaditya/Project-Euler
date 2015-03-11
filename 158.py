from scipy.misc import comb
from string import lowercase

# f = first, s = second , t = third
def count_3():
    for f in lowercase[:-1]: 
        for j, s in enumerate(lowercase):

            # case /\
            if s > f:
                if f == 'a': continue # if 'a' is starting point there is no char for third place, as it has to be smaller than second char
                count +=  j # j = number of chars smaller than char b 
            # case \/
            if s < f:
                #if 
                count += (25-j) # 25-j = number of characters larger than b (25 becuase index starts from 0)

def count_lexico(n):
    """ Project Euler # 158 """

    count = 0
    remaining_chars = n -3  # -3 for the triangle 
    for i in xrange(remaining_chars+1): 
        before, after = i, remaining_chars-i
        print before, after
        
        # case /\
        for i,f in enumerate(lowercase): 
            for j,s in enumerate(lowercase[i+1:]):
                num_of_chars_smaller_than_s = lowercase.index(s)-1 # -1 for the first char count
                count += num_of_chars_smaller_than_s 

        # case \/
        reversed_case = list(reversed(lowercase))
        for i,f in enumerate(reversed_case):
            for j,s in enumerate(reversed_case[i+1:]):
                num_of_chars_greater_than_s = 25 - lowercase.index(s)- 1 # -1 for the first char count, 25 because these index start from 0
                count += num_of_chars_greater_than_s 


count_lexico(3)
