'''
PROBLEM
    INPUT
    • a string of words separated by spaces
    
    OUTPUT
    • string that swaps the first and last letters of every word
    
    RULES
        EXPLICIT
        • assume that every word contains at least one letter
        • the string will always contain at least one word
        • each string contains nothing but words and spaces
        • there are no leading, trailing, or repeated spaces
        
        IMPLICIT
        • case remains the same
        
EXAMPLES
From the problem:
print(swap('Oh what a wonderful day it is')
    == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True

DATA STRUCTURE
• append reversed words into empty list, joined at returm to form a phrase
• use [::-1] and tuple unpacking for reversing words before joining for return phrase

ALGORITHM
• initialise a list of words split from the input phrase
• initialise empty list of swapped words
• reverse words shorter than 3 chars with [::-1], longer ones with tuple unpacking before appending to swapped word list
• join swapped word list into a string phrase and return

'''

def swap(phrase):
    words = phrase.split()
    swapped = []
    
    for word in words:
        if len(word) < 3:
            swapped.append(word[::-1])
        else:
            first, *mid, last = word
            swapped.append(last + ''.join(mid) + first) #could be cleaner with helper function
    
    return ' '.join(swapped)

print(swap('Oh what a wonderful day it is')
    == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True