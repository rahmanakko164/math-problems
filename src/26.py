import sympy as sp

def solve_quadratic(a, b, c):
    """
    Solve the quadratic equation ax^2 + bx + c = 0.
    
    Args:
        a (float): Coefficient of x^2.
        b (float): Coefficient of x.
        c (float): Constant term.
        
    Returns:
        float: The root of the quadratic equation.
    """
    # Solve the quadratic equation
    solutions = sp.solve(a*sp.Symbol('x')**2 + b*sp.Symbol('x') + c, sp.Symbol('x'))
    return solutions[0]

# Example usage and output
a = 1.0
b = -3.0
c = 2.0

print(f"The root of the quadratic equation {a}x^2 + {b}x + {c} = 0 is: {solve_quadratic(a, b, c)}")
