def next_featured(number):
    def is_multiple_7(number):
        return number % 7 == 0
    
    def is_odd(number):
        return number % 2 != 0
    
    def has_unique(number):
        digits = str(number)
        return len(set(digits)) == len(digits)
    
    max_possible = 9876543201
    count = number + 1
    
    while count <= max_possible:
        if is_multiple_7(count) and is_odd(count) and has_unique(count):
            return count
            
        count += 1
    
    return 'There is no possible number that fulfills those requirements.'

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
    "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True