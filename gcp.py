# gcd

import random

def euclid(m, n):
    if n == 0:
       return m
    else :
        euclid(n, m%n)

    first = random.randint(10 ** 3, 10 **8)
    second = random.randint(10 ** 3, 10 **8)

    the_gcd = euclid(first, second)
    
    print("\n The GCD of %d and %d" %(first, second), "is %d" % the_gcd )
    
    
    
