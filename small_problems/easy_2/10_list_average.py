'''
PROBLEM
    INPUT
    • one argument, a list of integers
    
    OUTPUT
    • returns the average of all the integers in the list, rounded down to the integer component of the average
    
    RULES
        EXPLICIT
        • list will never be empty
        • numbers will always be positive integers

EXAMPLES
print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True

DATA STRUCTURE
• use the input list directly; compute the sum and divide by the list length using floor division

ALGORITHM
• return sum(number_list) // len(number_list)

'''

def average(number_list):
    return sum(number_list) // len(number_list)

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True