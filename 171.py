from utilities import *
squares = []
for i in xrange(2401):
    squares.append(i*i)

for i in xrange(1, 2050):
    k = list(str(i))
    sum = 0
    for digit in k:
        sum = sum + int(digit)**2
    if sum in squares:
        print sum,
