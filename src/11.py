import random

def get_random_math_problem(numbers=5):
    num1 = random.randint(0, numbers)
    num2 = random.randint(0, numbers)
    operator = random.choice(['+', '-', '*', '/'])
    problem = f'{num1} {operator} {num2}'
    return problem
