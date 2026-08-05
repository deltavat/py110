def integer_to_string(i):
    DIGITS = {
        0: '1',
        1: '2',
        2: '3',
        3: '4',
        4: '5',
        5: '6',
        6: '7',
        7: '8',
        8: '9',
        9: '0',
    }
    
#   value = 0
#   for num in i:
#       value = (10 * value) + DIGITS[char]
    
    # 4321
    
    places = i
    counter = 0
    while places > 0:
        places //= 10
        counter += 1
    
    print(counter) # 4
    
    str_num = ''
    divmod_next = 0
    
    digit_key = i
    
    for num in range((counter -1), -1, -1):
        digit_key = divmod(i, 10**num)[0]
        divmod_next = divmod(i, 10**num)[1]
        str_num += DIGITS[digit_key]
    
    print(str_num)
    
    print(i//1000)
    print(divmod(i, 1000)) # 9, 876
    print(divmod(876, 100))
    print(divmod(87, 10))
    print(divmod(6, 1))
    print(divmod(0, 1))
    

print(integer_to_string(9876))# == "4321")              # True
#print(integer_to_string(4321) == "4321")              # True
#print(integer_to_string(0) == "0")                    # True
#print(integer_to_string(5000) == "5000")              # True
#print(integer_to_string(1234567890) == "1234567890")  # True

print(list(range(3, -1, -1)))

i = 9876

print(i//1000)
print(divmod(i, 1000)) # 9, 876
print(divmod(i, 1000)[1]) # 876
print(divmod(876, 100))
print(divmod(87, 10))
print(divmod(6, 1))
print(divmod(0, 1))

print(10**0)