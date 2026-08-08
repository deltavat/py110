def remove_vowels(slist):
#   consonants = []
#   
#   for phrase in slist:
#       no_wovels = ''
#       
#       for char in phrase:
#           if char not in 'aeiouAEIOU':
#               no_wovels += char
#       
#       consonants.append(no_wovels)
#   
#   return consonants
    
    return [
        ''.join(
            char 
            for char in phrase 
            if char not in 'aeiouAEIOU')
        for phrase in slist
    ]

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True