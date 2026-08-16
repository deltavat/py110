def bubble_sort(sort_these):
    while True:
        no_swaps = True
        
        for i in range(len(sort_these) - 1):
            first, second = sort_these[i], sort_these[i + 1]
            if first > second:
                sort_these[i], sort_these[i + 1] = second, first
                no_swaps = False
                
        if no_swaps:
            break

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
    'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
    "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True