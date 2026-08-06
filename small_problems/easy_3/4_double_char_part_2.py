def double_consonants(phrase):
    return ''.join([
        char*2 if char.isalpha() and char not in 'aeiouAEIOU' else char for char in phrase
    ])

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")