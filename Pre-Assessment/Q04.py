# Create a solution that accepts any three integer inputs representing the base (b1, b2) and height (h) measurements of a trapezoid in meters. Output the exact area of the trapezoid in square meters as a float value. The exact area of a trapezoid can be calculated by finding the average of the two base measurements, then multiplying by the height measurement.
# Trapezoid Area Formula:
# A = [(b1 + b2) / 2] * h
# The solution output should be in the format
# Trapezoid area: area_value square meters
 
# Sample Input/Output:
# If the input is
# 3
# 4
# 5
# then the expected output is
# Trapezoid area: 17.5 square meters
# Alternatively, if the input is
# 3
# 5
# 7
# then the expected output is
# Trapezoid area: 28.0 square meters


# A = [(b1 + b2) / 2] * h
b1 = float(input())
b2 = float(input())
h = float(input())

area_value = float(((b1 + b2) / 2) * h)

print(f"Trapezoid area: {area_value} square meters")