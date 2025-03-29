import random

def generate_random_sequence(length):
    sequence = [random.randint(1, 10) for _ in range(length)]
    return sequence

sequence = generate_random_sequence(5)
print(sequence)
