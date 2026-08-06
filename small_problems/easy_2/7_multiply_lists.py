'''
PROBLEM
    INPUT
    • two list arguments, each containing a list of numbers
    
    OUTPUT
    • returns a new list that contains the product of each pair of numbers from the arguments that have the same index
    
    RULES
        EXPLICIT
        • assume that the arguments contain the same number of elements
        
EXAMPLES
list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True

DATA STRUCTURE
• return list with multiplied items iterating over zipped object using comprehension

ALGORITHM
• return [list comprehension multiplying both elements from both lists, iterating over zipped object]

'''

def multiply_list(list1, list2):
    return [num1 * num2 for num1, num2 in zip(list1, list2)]

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True