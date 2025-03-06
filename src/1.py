import random

def get_random_python_code():
    operators = ["+", "-", "*", "/"]
    numbers = [1, 2, 3, 4, 5]
    variables = ["x", "y", "z"]

    code = ""
    for i in range(random.randint(1, 5)):
        operator = random.choice(operators)
        number = random.choice(numbers)
        variable = random.choice(variables)

        code += f"{variable} {operator} {number}\n"

    return code
