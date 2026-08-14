def triangle(side_1, side_2, side_3):
    side_list = sorted([side_1, side_2, side_3])
    first, second, third = side_list
    
    if first <= 0:
        return 'invalid'
        
    if third >= (first + second):
        return 'invalid'
    
    if first == second == third:
        return 'equilateral'
    elif (first == second) or (second == third):
        return 'isosceles'
    
    return 'scalene'

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True