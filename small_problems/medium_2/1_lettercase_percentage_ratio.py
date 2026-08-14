def letter_percentages(string):
    length = len(string)
    
    def percent(count):
        return f'{(count/length)*100:.2f}' 
    
    def lowers(string):
        count = 0
        for char in string:
            if char.islower():
                count += 1
        
        return count
    
    def uppers(string):
        count = 0
        for char in string:
            if char.isupper():
                count += 1
                
        return count
    
    def neithers(string):
        count = 0
        for char in string:
            if not (char.isupper() or char.islower()):
                count += 1
                
        return count
    
    return {
        'lowercase': percent(lowers(string)),
        'uppercase': percent(uppers(string)),
        'neither': percent(neithers(string)),
    }

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)