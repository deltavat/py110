'''
PROBLEM
    INPUT
    • list of numbers
    
    OUTPUT
    • list with the same number of elements, but with each element's value being the running total from the original list
    
    RULES
        EXPLICIT
        • return [] if [] is passed
        
        IMPLICIT
        • assuming list will be int as problem states list of numbers, so no guards needed
        • early return guard for empty lists
        
        
EXAMPLES
From the problem:
print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
    == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True

DATA STRUCTURE
• input is a list of numbers
• output will be a new list of numbers
• use a variable to track the running total as we iterate through the input list.


ALGORITHM
empty list guard that returns empty list

create new list and append first element of original number list
for loop that starts from index 1 and adds the previous element to current index
return new list

'''

def running_total(collection):
    if not collection:
        return []
    
    totals = []
    totals.append(collection[0])
    
    for index in range(1, len(collection)):
        totals.append(collection[index] + totals[-1])
        
#   alternate version:
#   totals = []
#   total = 0
#   
#   for number in collection:
#       total += number
#       totals.append(total)
    
    return totals

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
    == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True