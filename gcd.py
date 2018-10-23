import random
def euclid(m, n):
    if n == 0:
      return m
   else:
      return euclid(n, m % n)

first = random.randint(10 ∗∗ 3, 10 ∗∗ 8)
second = random.randint(10 ∗∗ 3, 10 ∗∗ 8)
the gcd = euclid(first , second)
print(”\nThe gcd of %d and %d” % (first , second), \
”is %d” % the gcd)
