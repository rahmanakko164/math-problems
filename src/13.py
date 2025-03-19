from random import randint

def get_random_code():
    numbers = []
    for i in range(10):
        numbers.append(randint(1, 10))
    
    operators = ['+', '-', '*', '/']
    operator = operators[randint(0, len(operators) - 1)]
    
    return f'{numbers[0]} {operator} {numbers[1]} = ?'
