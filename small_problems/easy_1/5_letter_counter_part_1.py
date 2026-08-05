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
        
        IMPLICIT
        • assume input is strictly string space separated phrases as desccribed in the proble, no other edge case tests necessary
        
EXAMPLES
From the problem:
# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})

DATA STRUCTURE
• iterate over a list of words split at space to fill a new dictionary with the word length as key, and occurences as it's value
• account for non-existant keys with .get(key, 0)

ALGORITHM
• list of split phrase at ' ' chars
• initialise empty dictionary
• iterate over words list and populate dictionary with len(word) as keys and no. of occurances as it's values
• return dictionary

'''

def word_sizes(phrase):
    words = phrase.split()
    sizes = {}
    
    for word in words:
        word_size = len(word)
        sizes[word_size] = sizes.get(word_size, 0) + 1
    
    return sizes

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})