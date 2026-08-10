# Practice Problems: Nested Data Structures

# Practice Problem 1
# For each object shown below, demonstrate how you would access the letter g.

lst1 = ['a', 'b', ['c', ['d', 'e', 'f', 'g']]]

print(
    lst1[2][1][3]
)

lst2 = [
    {
        'first': ['a', 'b', 'c'],
        'second': ['d', 'e', 'f']
    },
    {
        'third': ['g', 'h', 'i']
    }
]

print(
    lst2[1]['third'][0]
)

lst3 = [['abc'], ['def'], {'third': ['ghi']}]

print(
    lst3[2]['third'][0][0]
)


dict1 = {'a': ['d', 'e'], 'b': ['f', 'g'], 'c': ['h', 'i']}

print(
    dict1['b'][1]
)


# This one is much more challenging than it looks! Try it, but don't
# stress about it. If you don't solve it in 10 minutes, you can look
# at the answer.
dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, 'f': 1}, '3rd': {'g': 0}}

print(
    list(dict2['3rd'])[0]       # or list(dict2['3rd'].keys())[0]
)


# Practice Problem 2

# For each of these collection objects, demonstrate how you would change the value 3 to 4.

lst2_1 = [1, [2, 3], 4]
lst2_1[1][1] = 4
print(lst2_1[1][1], lst2_1)

lst2_2 = [{'a': 1}, {'b': 2, 'c': [7, 6, 5], 'd': 4}, 3]
lst2_2[2] = 4
print(lst2_2[2], lst2_2)

dict2_1 = {'first': [1, 2, [3]]}
dict2_1['first'][2][0] = 4
print(dict2_1['first'][2][0], dict2_1)

dict2_2 = {'a': {'a': ['1', 'two', 3], 'b': 4}, 'b': 5}
dict2_2['a']['a'][2] = 4
print(dict2_2['a']['a'][2], dict2_2)


# Practice Problem 3

a = 2
b = [5, 8]
lst = [a, b]

lst[0] += 2
lst[1][0] -= a

# what will the final values of a and b be
# kst = [4, [3, 8]]
# a = 2, b = [3, 8]


# Practice Problem 4
# print the name, age, and gender of each family member
# (name) is a (age)-year-old (male or female).
#Herman is a 32-year-old male.
#Lily is a 30-year-old female.
#Grandpa is a 402-year-old male.
#Eddie is a 10-year-old male.
#Marilyn is a 23-year-old female.

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

for name, detail in munsters.items():
    print(f'{name} is a {detail['age']}-year-old {detail['gender']}.')