'''
Most Adjacent Consonants

PROBLEM
    INPUT
    • [strings] A list of strings
    
    OUTPUT
    • List sorted based on highest number of adjacent consonants a string contains

    RULES
        EXPLICIT
        • If two strings contain same higher no. of adjacent consonants, they should retain their original order in relation to each other
        • 'adjacent': considered adjacent if they are next to each other in the same word or if there is a space between two consonants in adjacent words
        
        IMPLICIT
        • Original order needs to be maintained same no. of adjacent consonants, which includes 0.
        • This means only adding successful adjacent consonants (this is obvious, but initially I counted single ones too)
        • Use nested list pairs with sort rank, then sort and re-build final group to get the sorted group.
        
        NOTES
        • group.sort(key=sort them by first element of nested inner list which will be adjacent consonant rank)

EXAMPLES
my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']

DATA STRUCTURE
• I could have nested list pairs with nested_list[0] element being the adjacent consonant scoring rank, and nested_list[1] element being the string itself.
• Sort the list with scoring rank pairs
• Use nested_list[1] to re-build final sorted list that will be returned

ALGORITHM

CODE:
'''

def sort_by_consonant_count(collection):
    consonant_count_list = []
    
    for phrase in collection:
        adj_consonant_count = 0
    
#       if words[0] not in 'aeiou':
#           adj_consonant_count += 1
        
        for index in range(1, len(phrase) + 1):
#           if words[index:index + 1].isspace(): 
#               continue
            
            if index > len(phrase) -1 or phrase[index].isspace(): 
                continue
            
            if (phrase[index - 1:index] not in 'aeiou') and (phrase[index:index + 1] not in 'aeiou'):
                adj_consonant_count += 1
        
        consonant_count_list.append([adj_consonant_count, phrase])
    
    def sorting_rank(inner_list): # possibly overkill, probably more elegant way to do this
        return inner_list[0]
    
    consonant_count_list.sort(key=sorting_rank, reverse=True) 
#   print(consonant_count_list)
    
    return [pair[1] for pair in consonant_count_list]

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']