import math

def power(x, y):
    result = 1
    base = x
    exponent = y
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    return result

print(power(2, 3)) # Output: 8
