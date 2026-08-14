def fibonacci(number):
    if number < 3:
        return 1

    fibs = [1, 1]
    for i in range(2, number):
        fibs.append(fibs[i - 1] + fibs[i - 2])
        
    return fibs[-1]

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True