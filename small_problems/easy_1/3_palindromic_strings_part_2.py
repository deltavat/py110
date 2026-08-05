'''
PROBLEM
    INPUT
    • string phrase
    
    OUTPUT
    • `True` if string phrase is a palindrome, `False` otherwise
    
    RULES
        EXPLICIT
        • case-insensitive
        • ignore all non-alphanumeric chars
        
        IMPLICIT
        • no guard clauses necessary assuming inputs are string phrases as stated in the problem
        
EXAMPLES
From the question:
print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True

DATA STRUCTURE
• generator expression all chars that pass a .isalnum() check, lowercase them and join them for a raw string
• check if raw string is a palindrome against reversed raw string
• return True/False 

ALGORITHM
make clean string with a generator expression collecting all allnum chras from original phrase, lowercase & join them
check clean string against clean string[::-1]
return check as True/False

CODE
'''

def is_real_palindrome(phrase):
    cleaned_phrase = ''.join(char.casefold() for char in phrase if char.isalnum())

    return cleaned_phrase == cleaned_phrase[::-1]

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True