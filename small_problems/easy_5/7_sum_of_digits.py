def sum_digits(integer):
    return sum(
        int(number) for number in str(integer)
    )

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True