from math import sqrt, ceil

def is_prime(n):
    m = ceil(sqrt(n))
    for i in range(2,m):
        if n%i == 0:
            return i
    return 0
    
n = 600851475143
while True:
    q = is_prime(n)
    if q == 0:
        print(n)
        break
    else: 
        print(q)
        n//=q

