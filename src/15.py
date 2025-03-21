def calculate_area(shape, dimensions):
    """
    Calculate the area of a geometric shape with given dimensions.
    
    Parameters:
    shape (str): The type of shape ('circle', 'rectangle', 'triangle').
    dimensions (tuple): A tuple containing the length and width or any other dimension(s) of the shape.

    Returns:
    float: The area of the shape.
    """
    if shape == "circle":
        radius = dimensions[0]
        return 3.14 * (radius ** 2)
    elif shape == "rectangle":
        width, height = dimensions
        return width * height
    else:
        raise ValueError("Unsupported shape: {}".format(shape))

# Example usage:
shape_type = input("Enter the type of shape (circle, rectangle, triangle): ")
dimensions = tuple(map(float, input(f"Enter dimensions for {shape_type} (length and width separated by a space): ").strip().split()))

area = calculate_area(shape_type, dimensions)
print(f"The area of the shape is: {area:.2f}")
