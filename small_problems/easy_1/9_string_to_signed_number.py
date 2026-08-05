'''
PROBLEM
    INPUT
    • a string of digits
    • string may have a leading + or - sign
    • 
    
    OUTPUT
    • returns the appropriate number as an integer
    
    RULES
        EXPLICIT
        • may not use any of the standard conversion functions available in Python, such as `int`
        • may use the string_to_integer function from the previous exercise
        • function should calculate the result by using the characters in the string.
        • if the first character is a +, your function should return a positive number
        • if it is a -, your function should return a negative number
        • if there is no sign, return a positive number
        
        IMPLICIT
        • string will always contain a valid number
        • assume all characters are numeric
        
EXAMPLES
print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True

DATA STRUCTURE


ALGORITHM


'''
# my original version:

#def string_to_signed_integer(s):
#   DIGITS = {
#       '0': 0,
#       '1': 1,
#       '2': 2,
#       '3': 3,
#       '4': 4,
#       '5': 5,
#       '6': 6,
#       '7': 7,
#       '8': 8,
#       '9': 9,
#   }
#   
#   clean_s = s.replace('+', '').replace('-', '')
#   
#   value = 0
#   for char in clean_s:
#       value = (10 * value) + DIGITS[char]
#   
#   if s[0] == '-':
#       return value * -1
#   
#   return value

def string_to_integer(s):
    DIGITS = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }
    
    value = 0
    for char in s:
        value = (10 * value) + DIGITS[char]
        
    return value

def string_to_signed_integer(s):                # practising using second function with the first
    if s[0] == '-':
        return -string_to_integer(s[1:])
    elif s[0] == '+':
        return string_to_integer(s[1:])
    else:
        return string_to_integer(s)

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True