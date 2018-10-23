def rec_exp(a,n):

 if n==0:
     return 1
 else:
     n%2 == 0
     half = rec_exp(a, a//2)
     return half**2
