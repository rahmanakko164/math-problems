import random

def get_random_math_problem(n):
    numbers = list(range(1, n+1))
    number1 = random.choice(numbers)
    number2 = random.choice(numbers)
    operator = random.choice(["+", "-", "*", "/"])
    if operator == "+":
        return f"{number1} + {number2}"
    elif operator == "-":
        return f"{number1} - {number2}"
    elif operator == "*":
        return f"{number1} * {number2}"
    else:
        return f"{number1} / {number2}"
