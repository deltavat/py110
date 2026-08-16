def triangle(*angles):
    if 0 in angles or sum(angles) != 180:
        return 'invalid'
    
    if 90 in angles:
        return 'right'
    elif all(angle < 90 for angle in angles):
        return 'acute'
    
    return 'obtuse'

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True