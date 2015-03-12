from scipy.misc import comb
from string import ascii_lowercase as lowercase
from math import factorial as fact
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
    for i in range(remaining_chars+1): 
        before, after = i, remaining_chars-i
        #print before, after
        
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


def choose_nkp(n,k,p):
    if n-k-p < 0: return 0
    return fact(n) / ( fact(n-k-p)*fact(k)*fact(p) )  

def count_lexico_simple(n):
    """ Project Euler # 158 """

    count = 0
    remaining_chars = n - 2  # -2 for the inclined line (/) 

    for i in range(remaining_chars+1): 
        before, after = i, remaining_chars-i
        #if not before : before = -1
        #if not after  : after  = -1
        #print before, after 

        k = 0
        for i,f in enumerate(lowercase):
            for j, s in enumerate(lowercase[i+1:]):
                #print f,s 
                #num_of_chars_greater_than_f = 25 - lowercase.index(f)- 1 # -1 for the second char count, 25 because these index start from 0
                #num_of_chars_smaller_than_s = lowercase.index(s)-1 # -1 for the first char count
                term = 0
                num_of_chars_greater_than_f = 25 - lowercase.index(s)- 1 # -1 for the second char count, 25 because these index start from 0
                num_of_chars_smaller_than_s = lowercase.index(f)-1 # -1 for the first char count
                if before and after:
                    term = (lowercase.index(s) - lowercase.index(f) -1 )
                    #print "*", (lowercase.index(s) - lowercase.index(f)  )
                    count += choose_nkp(num_of_chars_greater_than_f, after, before) * choose_nkp(num_of_chars_smaller_than_s, before, after)
                    pass
                else:
                    pass
                    #term += before*after*comb((lowercase.index(s) - lowercase.index(f) -1 ),before)
                #count += comb(num_of_chars_greater_than_f, after) * comb(num_of_chars_smaller_than_s, before) - term
                count += comb(num_of_chars_greater_than_f, before) * comb(num_of_chars_smaller_than_s, after) 
                #k += comb(num_of_chars_greater_than_f, before) * comb(num_of_chars_smaller_than_s, after) #- (lowercase.index(s) - lowercase.index(f) -1 )
        #print "k ", k, before, after
    return count
        
#print count_lexico_simple(4)
answers= []
for i in range(4,6):
    ans = count_lexico_simple(i)
    print(i, ans)
    answers.append(ans)
print(max(answers))
