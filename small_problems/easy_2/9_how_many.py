'''
PROBLEM
    INPUT
    • list
    
    OUTPUT
    • each element alongside the number of occurrences:

    RULES
        EXPLICIT
        • words are case sensitive e.g. ("suv" != "SUV")

EXAMPLES
vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
        'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

# your output sequence may appear in a different sequence
car => 4
truck => 3
SUV => 1
motorcycle => 2

DATA STRUCTURE
• iterate over list set so only unique elements exist, and print counts using the original input list

ALGORITHM
for every element in set(collection):
    print element ==> occurance

'''

def count_occurrences(collection):
    for element in set(collection):
        print(f'{element} => {collection.count(element)}')

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
        'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)