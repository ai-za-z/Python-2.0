def calculate_circumference(radius):
    # Formula: Circumference = 2 * π * radius
    pi = 3.14159
    circumference = 2 * pi * radius
    return circumference

# Example usage
radius = float(input("Enter the radius of the circle: "))
result = calculate_circumference(radius)
print(f"The circumference of the circle with radius {radius} is: {result}")
