'''
PROBLEM
    INPUT
    • two lists passed as arguments
    
    OUTPUT
    • returns a new list that contains all elements from both list arguments, with each element taken in alternation
    
    RULES
        EXPLICIT
        • assume that both input lists are non-empty
        • they have the same number of elements.

EXAMPLES
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True

DATA STRUCTURE
• append to a new empty list from a zip object and return it

ALGORITHM
• initialise new empty list
• iterate over zipped list1 & list2 object and append to new list
• return new list with interwoven elements

'''

def interleave(list1, list2):
    woven = []
    for item1, item2 in zip(list1, list2):
        woven += (item1, item2)             # changed from .extend() as += does the same thing
        
    return woven

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True