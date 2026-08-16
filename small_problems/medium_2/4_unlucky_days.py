from datetime import date

FRIDAY = 4

def friday_the_13ths(year):
    return sum(
        1 for month in range(1, 13) if date(year, month, 13).weekday() == FRIDAY
    )

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True