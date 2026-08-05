'''
PROBLEM
    INPUT
    • two lists as arguments
    
    OUTPUT
    • returns a set that contains the union of the values from the two lists
    
    RULES
        EXPLICIT
        • assume that both arguments will always be lists
        
EXAMPLES
print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

DATA STRUCTURE
• convert argument lists into sets and use `|` union operator to return set with union of values

ALGORITHM
• return set(list1) | set(list2)

'''

def union(list1, list2):
    return set(list1) | set(list2)

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True