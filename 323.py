print sum([i * ((1 - 0.5**i)**32 - (1 - 0.5**(i-1))**32) for i in xrange(100)])

