import sympy as sp
from sympy import symbols, solve, diff

# Define the variable
x = symbols('x')

# Define the function
f = x**3 + 2*x**2 - 5*x + 1

# Find the first derivative of the function
f_prime = diff(f, x)

# Simplify the first derivative
f_prime_simplified = sp.simplify(f_prime)
