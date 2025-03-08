import random

def get_random_python_code():
    operators = ["+", "-", "*", "/"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    code = ""
    for i in range(5):
        op = random.choice(operators)
        num1 = random.choice(numbers)
        num2 = random.choice(numbers)
        code += f"{num1} {op} {num2}"
    return code
