import random

def generate_random_code(length):
    """Generate a random string of letters and digits"""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    return "".join(random.choice(characters) for _ in range(length))