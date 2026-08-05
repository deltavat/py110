'''
PROBLEM
    INPUT
    • string phrase

    OUTPUT
    • Return `True` if palindrome, else `False`
    
    RULES
        EXPLICIT
        • Case matters
        • ALl chars matter
        
        IMPLICIT
        • Problem states input will be 'strings passed'so no guard clause necessary
        
EXAMPLES
From the problem:
# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)

DATA STRUCTURE
Check if string matches inverted string

ALGORITHM
Compare string with reversed version of string
Return True if they match, False otherwise.

CODE
function:
return string == string[::-1]
'''

def is_palindrome(phrase):
    return phrase == phrase[::-1]

# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)