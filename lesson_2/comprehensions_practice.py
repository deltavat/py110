# Practice Problem 1

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

expected_1 = 444

# ordinary loop
#ages = []
ages = 0

for details in munsters.values():
    if details['gender'] == 'male':
#       ages.append(details['age'])
        ages += details['age']

#print(sum(ages))
print(ages == expected_1)

# comprehension

print(
    sum(
        details['age'] for details in munsters.values() if details['gender'] == 'male'
    )
    == expected_1)

# ----------------------------------------------------------------------------------------------------

# Practice Problem 2
# return a new list with the same structure, but with the values in each sublist ordered in ascending orde

lst2 = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
expected_2 = [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]

print(
    [sorted(sublist) for sublist in lst2]
    == expected_2)

# ----------------------------------------------------------------------------------------------------

# Practice Problem 3
# return a new list with the same structure, but with the values in each sublist ordered in ascending order as strings (that is, the numbers should be treated as strings)

lst3 = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
expected_3 = [['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]

print(
    [sorted(sublist, key=str) for sublist in lst3]
    == expected_3)

# ----------------------------------------------------------------------------------------------------

# Practice Problem 4
# write some code that uses comprehensions to define a dictionary where the key is the first item in each sublist, and the value is the second

lst4 = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

# Pretty printed for clarity
expected_4 = {
        'a': 1,
        'b': 'two',
        'sea': {'c': 3},
        'D': ['a', 'b', 'c']
    }

print(
    {item[0]: item[1] for item in lst4}
    == expected_4)

# ----------------------------------------------------------------------------------------------------

# Practice Problem 5
# sort the list so that the sub-lists are ordered based on the sum of the odd numbers that they contain. You shouldn't mutate the original list.

lst5 = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]
expected_5 = [[1, 8, 3], [1, 6, 7], [1, 5, 3]]

#def odd_sum(lst):
#   return sum(
#       [num for num in lst if num %2 == 1]
#   )

sorted_list = sorted(lst5, key=lambda lst: sum(num for num in lst if num % 2 == 1))
print(sorted_list == expected_5)

# ----------------------------------------------------------------------------------------------------

# Practice Problem 6
# return a new list identical in structure to the original, but with each number incremented by 1. Do not modify the original data structure. Use a comprehension.

lst6 = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]
expected_6 = [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]

#lst6_copy = lst6.copy()

#for dic in lst6_copy:
#   for key in dic:
#       dic[key] += 1
#
#print(lst6_copy == expected_6)


print(
    [
        {
            key: value + 1 for key, value in dic.items()
        } for dic in lst6
    ]
    == expected_6)

# alternative with helper function:

#def increment_values(dictionary):
#   return {key: value + 1 for key, value in dictionary.items()}
#
#new_list = [increment_values(value) for value in lst]
#
#print(new_list, lst, sep='\n')


# ----------------------------------------------------------------------------------------------------

# Practice Problem 7
# return a new list identical in structure to the original, but containing only the numbers that are multiples of 3

lst7 = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]
expected_7 = [[], [3, 12], [9], [15, 18]]

print(
    [[
        num for num in list if num %3 == 0
    ]for list in lst7]
    == expected_7)

# ----------------------------------------------------------------------------------------------------

# Practice Problem 8
#  return a list that contains the colors of the fruits and the sizes of the vegetables. The sizes should be uppercase, and the colors should be capitalized.

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

expected_8 = [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]

#big dictionary
#   ↓
#food dictionary
#   ↓
#colors list
#   ↓
#individual color

print(
    [
        [color.capitalize() for color in food["colors"]]
        if food["type"] == "fruit"
        else food["size"].upper()
        
        for food in dict1.values()
    ]
    == expected_8)

# official solution:
#def transform_item(item):
#   if item['type'] == 'fruit':
#       return [color.capitalize() for color in item['colors']]
#   else:
#       return item['size'].upper()
#   
#result = [transform_item(item) for item in dict1.values()]
#print(result)

# ----------------------------------------------------------------------------------------------------

# Practice Problem 9
# write some code to return a list that contains only the dictionaries where all the numbers are even.

lst9 = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

expected_9 = [{'e': [8], 'f': [6, 10]}]

def are_even(dictionary):
    for value in dictionary.values():
        for num in value:
            if num % 2 != 0:
                return False
    
    return True

print(
    [dic for dic in lst9 if are_even(dic)]
    == expected_9)

# ----------------------------------------------------------------------------------------------------

# Practice Problem 10
# function that takes no arguments and returns a string that contains a UUID.

hexadecimal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']

import random

def generate_uuid():
    def eight():
        return ''.join([str(random.choice(hexadecimal)) for _ in range(8)])
    
    def four():
        return ''.join([str(random.choice(hexadecimal)) for _ in range(4)])
    
    def twelve():
        return ''.join([str(random.choice(hexadecimal)) for _ in range(12)])
    
    return f'{eight()}-{four()}-{four()}-{four()}-{twelve()}'

print(generate_uuid())

# ----------------------------------------------------------------------------------------------------

# Practice Problem 11
# some code to create a list of every vowel (a, e, i, o, u) that appears in the contained strings, then print it.

dict11 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

expected_11 = ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']

list_of_vowels = []

for value in dict11.values():
    for word in value:
        for char in word:
            if char in 'aeiou':
                list_of_vowels.append(char)

print(list_of_vowels == expected_11)

# extra challenge:
print(
    [
        char
        for value in dict11.values()    # for key in dict11
        for word in value               # for word in dict11[key]
        for char in word
        if char in 'aeiou'
    ]
    == expected_11)