def unique_sequence(integers):
    if not integers:
        return []
    
    uniques = [integers[0]]

    for number in integers[1:]:
        if number != uniques[-1]:
            uniques.append(number)
    
    return uniques

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True

# Non-consecutive duplicates are kept
original = [1, 2, 1, 3]
expected = [1, 2, 1, 3]
print(unique_sequence(original) == expected)      # True