# This is just an example, you can modify it as per your needs.
# For instance, if you want to solve quadratic equations, you can use this code.

import math

def solve_quadratic(a, b, c):
    d = (b**2) - (4*a*c)
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    return root1, root2
