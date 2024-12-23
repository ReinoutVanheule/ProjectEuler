def collatz(number):
    length = 0
    while True:
        if number % 2== 0:
            number = number//2
        else:
            number = 3*number + 1
        if number == 1:
            return length
        length += 1
        
max_length = 0
max_pick = 0
for i in range(1,1000000):
    length = collatz(i)
    if length > max_length:
        max_length = length
        max_pick = i
        
print(max_pick)