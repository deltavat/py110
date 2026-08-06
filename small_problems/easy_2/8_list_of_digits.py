'''
PROBLEM
    INPUT
    • one argument, a positive integer
    
    OUTPUT
    • returns a list of the digits in the number
    
EXAMPLES
print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True

DATA STRUCTURE
• return list of numbers iterating over string version of input numbers, converting them to int using list comprehension

ALGORITHM
•     return [int(num) for num in str(number)]

'''

def digit_list(number):
    return [int(num) for num in str(number)]

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True