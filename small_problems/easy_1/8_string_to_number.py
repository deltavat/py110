'''
PROBLEM
    INPUT
    • a string of digits
    
    OUTPUT
    • returns the appropriate number as an integer
    
    RULES
        EXPLICIT
        • may not use any of the standard conversion functions available in Python, such as `int`
        • function should calculate the result by using the characters in the string.
        
        IMPLICIT
        • string will always contain a valid number
        • assume all characters are numeric
        
EXAMPLES
print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

DATA STRUCTURE
• import string (exploring import string instead of making a simple `int` lookup dictionary with `str` numbers)
• enumerate with reversed string, using char index lookup and 10**index before adding sum to return final value

ALGORITHM
• import string
• enumerate on reverse string & multiply with 10**index
• return sum using a generator

'''

import string

#print(string.digits)                  # 0123456789
#print(string.digits.index('4'))       # returns int
#print(type(string.digits.index('4'))) # returns int

def string_to_integer(str_num):
#   num_list = []
#
#   for index, char in enumerate(reversed(str_num)): # '1234'
#       num = string.digits.index(char) * (10**index)
#       num_list.append(num)
#
#
#   return sum(num_list)
    
    return sum(string.digits.index(char) * (10**index) for index, char in enumerate(reversed(str_num)))


print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True