def rotator(num):
    chars = list(str(num))
    first, *rest = chars
    return ''.join([*rest, first])

def max_rotation(number):
    passes = len(str(number)) - 1
    constructor = str(number)
    
    for i in range(passes):
        constructor = constructor[:i] + rotator(constructor[i:])
    
    return int(constructor)

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True