from math import ceil,sqrt 

def is_prime(n):
    m = ceil(sqrt(n))
    for i in range(2,m+1):
        if n%i == 0:
            return False
    return True

total = 1
i = 3
while True:
    if is_prime(i):
        total += 1
    if total == 10001:
        print(i)
        break
    i += 1