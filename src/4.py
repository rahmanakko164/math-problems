def get_random_math_problem(n):
    # Generate a random number between 1 and n
    num1 = random.randint(1, n)
    num2 = random.randint(1, n)

    # Choose an operator at random
    operators = ['+', '-', '*', '/']
    operator = random.choice(operators)

    # Return the math problem and solution
    return f"{num1} {operator} {num2} = ?"
