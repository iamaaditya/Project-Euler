from utilities import Prime

p  = Prime()
prod = 1
while True:
    pn = p.next()
    if prod*pn > 1000000:
        print prod
        break
    prod *= pn

