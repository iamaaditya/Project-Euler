from __future__ import division
from random import randint

def get_kelly_fraction(p, b):
    return (p*(b+1) - 1) / b

def coin_toss(capital, f, p, b):
    """ returns the changed capital based on fair coin toss on capital 
    where only "f" fraction was invested  and b were the odds"""

    toss = randint(0,1)
    if toss:
        return capital + f*capital*b

    else :
        return capital - f*capital


def run_experiment():
    capital = 1
    p = 0.5
    b = 2
    for i in xrange(1000):
        f = get_kelly_fraction(p,b) 
        capital = coin_toss(capital, f, p, b)
        #print capital, f, p, b, toss
    print capital

for i in xrange(10):
    run_experiment()


