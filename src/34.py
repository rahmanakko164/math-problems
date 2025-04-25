import sympy as sp
from sympy import *
f = symbols('x')
g = symbols('y')
H = 5  # unknown

def solve_inequality(f, g, H):
    solution = solve((1/3)*f + (2/3)*g - H, [f, g])
    return solution

solution = solve_inequality(f, g, H)
print("Solutions:", solution)
