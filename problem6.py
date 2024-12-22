sum_squared = sum(i**2 for i in range(101))
squared_sum = sum(i for i in range(101))**2
print(squared_sum-sum_squared)