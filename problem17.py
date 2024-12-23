c = "hundred"
m = "one thousand"
numbers = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen",
           "fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
numbers10 = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

def char(number):
    total = 0
    if number < 20: 
        total += len(numbers[number-1])
    elif number < 100: 
        q,r = divmod(number,10)
        total += len(numbers10[q-2])
        if r > 0:
            total += char(r)
    elif number<1000: 
        q,r = divmod(number,100)
        total += char(q)
        total += len(c)
        if r > 0:
            total += 3
            total += char(r)
    elif number == 1000:
        total += len(m)-1
    return total 

print(sum(char(i) for i in range(1,1001)))