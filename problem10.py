from math import ceil,sqrt 

def is_prime(n):
    m = ceil(sqrt(n))
    for i in range(2,m+1):
        if n%i == 0:
            return False
    return True

print(2+sum(i for i in range(3,2000000) if is_prime(i)))

        