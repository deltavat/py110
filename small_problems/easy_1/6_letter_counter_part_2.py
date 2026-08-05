'''
PROBLEM
    INPUT
    • string consisting of zero or more space-separated words
    
    OUTPUT
    • returns a dictionary that shows the number of words of different sizes
    
    RULES
        EXPLICIT
        • words consist of any sequence of non-space characters
        • empty string retunrns an empty dictionary
        • exclude non-letters
        
        IMPLICIT
        • assume input is strictly string with spaces between words as desccribed in the problem, no other edge case tests necessary
        
EXAMPLES
From the problem:
# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})

DATA STRUCTURE
• create clean phrase without any non-letters
• iterate over a list of split words to fill a new dictionary with the word length as key, and occurences as it's value
• account for non-existant keys with .get(key, 0)

ALGORITHM
• initialise cleaned_phrase with string phrase without any non-letters
• list of split words
• initialise empty dictionary
• iterate over words list and populate dictionary with len(word) as keys and no. of occurances as it's values
• return dictionary

'''

def word_sizes(phrase):
#   cleaned_phrase = ''
#   for char in phrase:
#       if char.isspace() or char.isalnum():
#           cleaned_phrase += char
    
    cleaned_phrase = ''.join(char for char in phrase if char.isspace() or char.isalpha())
    
    words = cleaned_phrase.split()
    sizes = {}
    
    for word in words:
        word_size = len(word)
        sizes[word_size] = sizes.get(word_size, 0) + 1
        
    return sizes

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})