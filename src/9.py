import random

def get_random_math_problem():
    numbers = [1, 2, 3, 4, 5]
    operators = ["+", "-", "*", "/"]
    problem = ""
    for i in range(3):
        index = random.randint(0, len(numbers) - 1)
        number = numbers[index]
        del numbers[index]
        index = random.randint(0, len(operators) - 1)
        operator = operators[index]
        del operators[index]
        problem += str(number) + " " + operator + " "
    return problem[:-1] + "=?"
