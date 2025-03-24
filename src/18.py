import math

def find_min_max(numbers):
    """
    Find the minimum and maximum values in a list of numbers.
    
    Parameters:
    numbers (list): A list of numbers.
    
    Returns:
    tuple: A tuple containing the minimum and maximum values.
    """
    min_value = max_value = float('-inf')
    for num in numbers:
        if num > max_value:
            max_value = num
        elif num < min_value:
            min_value = num
    return (min_value, max_value)

# Example usage
numbers_list = [10, 23, -5, 78, 4]
result = find_min_max(numbers_list)
print("Minimum value:", result[0], "Maximum value:", result[1])
