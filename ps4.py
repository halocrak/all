from random import *
M=["5.05","5.07","6.72","7.02","7.05","7.50","7.51","7.55"]
for o in range (100000):
    mrx = str(randint(0,9999999))
    halo =(choice(M)+mrx)
    print(halo +":"+ halo)
