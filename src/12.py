import random

def get_random_number(min_val, max_val):
    return random.randint(min_val, max_val)

def solve_math_problem(problem, answer):
    if problem == "addition":
        result = get_random_number(1, 10) + get_random_number(1, 10)
    elif problem == "subtraction":
        result = get_random_number(1, 10) - get_random_number(1, 10)
    elif problem == "multiplication":
        result = get_random_number(1, 10) * get_random_number(1, 10)
    elif problem == "division":
        result = get_random_number(1, 10) / get_random_number(1, 10)
    else:
        return "Invalid problem"
    
    if result == answer:
        return "Correct!"
    else:
        return "Incorrect. The correct answer is {}. Try again.".format(result)

problem = input("Enter a math problem (addition, subtraction, multiplication, division): ")
answer = int(input("Enter the answer: "))

print(solve_math_problem(problem, answer))