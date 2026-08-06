'''
PROBLEM
    INPUT
    • a list of positive integers
    
    OUTPUT
    • a string representation of the multiplicative average rounded to three decimal places
    
    RULES
        EXPLICIT
        • multiplies all of the integers together, divides the result by the number of entries in the list, and returns the result as a string with the value rounded to three decimal places
        
EXAMPLES
# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")

DATA STRUCTURE
• iterate and *= over int elements of the input and return avg .3f

ALGORITHM
• initialise a multiplier, and *= it while iterating on input list
• return avg .3f

'''

def multiplicative_average(numbers):
    multiplied = 1
    for num in numbers:
        multiplied *= num
    
    avg = (multiplied / len(numbers))
    return f'{avg:.3f}'

# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")