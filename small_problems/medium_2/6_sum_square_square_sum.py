def sum_square_difference(number):
    numbers = list(range(1, number + 1))
    
    def square_of_sum():
        return sum(numbers)**2
    
    def sum_of_squares():
        return sum(num**2 for num in numbers)

    return square_of_sum() - sum_of_squares()

#   return sum(list(range(1, number + 1)))**2 - sum(num**2 for num in list(range(1, number + 1)))

print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True