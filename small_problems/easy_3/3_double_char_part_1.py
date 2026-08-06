def repeater(phrase):
    constructor = ''
    for char in phrase:
        constructor += char*2
    
    return constructor

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True