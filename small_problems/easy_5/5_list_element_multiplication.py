def multiply_items(a, b):
    return [num_a * num_b for num_a, num_b in zip(a, b)]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True