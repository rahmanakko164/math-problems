def calculate_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

sum_result = calculate_sum(1, 2, 3, 4)
print("The sum is:", sum_result)
