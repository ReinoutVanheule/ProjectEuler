from math import gcd
start = 2520
for i in range(11,21):
    if start % i != 0:
        start *= i//gcd(start,i)
        