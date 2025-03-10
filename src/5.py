import random

def get_random_math_problem(difficulty):
    if difficulty == "easy":
        number1 = random.randint(1, 10)
        number2 = random.randint(1, 10)
        operator = random.choice(["+", "-", "*", "/"])
        solution = eval(f"{number1} {operator} {number2}")
        return f"What is {number1} {operator} {number2}?"
    elif difficulty == "medium":
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        operator = random.choice(["+", "-", "*", "/"])
        solution = eval(f"{number1} {operator} {number2}")
        return f"What is {number1} {operator} {number2}?"
    else:
        number1 = random.randint(1, 1000)
        number2 = random.randint(1, 1000)
        operator = random.choice(["+", "-", "*", "/"])
        solution = eval(f"{number1} {operator} {number2}")
        return f"What is {number1} {operator} {number2}?"