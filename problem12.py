divisors = lambda n: len(list(i for i in range(1,n+1) if n%i ==0))

number = 1
while True:
    if number % 2== 0 :
        if divisors(number//2)*divisors(number+1) > 500:
            break
    else:
        if divisors(number)*divisors((number+1)//2) > 500:
            break
    number += 1
print(number*(number+1)//2)