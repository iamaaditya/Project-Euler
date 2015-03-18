from fractions import Fraction
from utilities import SumDigits

def frac(term, v):
    return Fraction(1, term + v)

def fra(list_terms):
    f = Fraction(list_terms[-1],1)
    for i in list_terms[:-1][::-1]:
        f = i + Fraction(1,f)
    return f

def solve_e_convergent():
    l = []
    for i in xrange(1,200):
        l.extend([1,2*i,1])
    result =  Fraction(2 + Fraction(1,fra(l[:99])))
    print SumDigits(result.numerator)

def solve_sqrt_2_convergent():
    l = [2 for i in xrange(1000)]
    fg = Fraction(1,2)
    for i in xrange(20):
        print i-1, l[i-1], 1 + fg, fg
        fg = frac(fg,l[i]) 

solve_e_convergent()
#solve_sqrt_2_convergent()

