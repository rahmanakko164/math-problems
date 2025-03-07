import random

def get_random_math_problem():
    # Generate a random number between 1 and 10
    num1 = random.randint(1, 10)
    # Generate another random number between 1 and 10
    num2 = random.randint(1, 10)
    # Choose a random operation (+, -, *, /)
    op = random.choice(['+', '-', '*', '/'])
    # Return the problem in string format
    return f"{num1} {op} {num2}"
