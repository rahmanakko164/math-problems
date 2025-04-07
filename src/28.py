def calculate_derivative(f, x):
    """Calculates the derivative of a function f at a point x."""
    return (f(x + 0.1) - f(x)) / 0.1

if __name__ == "__main__":
    # Example usage:
    print(calculate_derivative(2*x**3 + 4*x, 1))
