import sympy as sp

def simple_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += 1 / (i * (i + 1))
    return total

simple_sum(5)
