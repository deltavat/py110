def sum_of_sums(number_list):
#   sums = []
#   
#   for index in range(len(number_list)):
#       sums.extend(number_list[:index + 1])
#   
#   return sum(sums)
    
    return sum(
        number for index in range(len(number_list))
        for number in number_list[:index + 1]
    )

print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True