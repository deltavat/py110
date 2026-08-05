'''
PROBLEM
    INPUT
    • a list as an argument
    
    OUTPUT
    • a list that contains two elements, both of which are lists
    
    RULES
        EXPLICIT
        • put the first half of the original list elements in the first element of the return value and put the second half in the second element
        • if the original list contains an odd number of elements, place the middle element in the first half list
        
EXAMPLES
# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])

DATA STRUCTURE
• use floor division to differenciate between odd and even len(list), adding 1 for odd lengths before returning wit divided nested lists

ALGORITHM
• if even:
    index is len(list) // 2 + 1
• else:
    index is len(list) // 2

return [halved nested lists]

'''

def halvsies(lst):
#   if len(lst) %2 == 1:
#       index = len(lst) // 2 + 1
#   else:
#       index = len(lst) // 2

    index = len(lst) // 2 + 1 if len(lst) %2 == 1 else len(lst) // 2

    return [lst[:index], lst[index:]]

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])