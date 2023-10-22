# Create a solution that accepts five integer inputs. Output the sum of the five inputs three times, converting the inputs to the requested data type prior to finding the sum.
 
# First output: sum of five inputs maintained as integer values
# Second output: sum of five inputs converted to float values
# Third output: sum of five inputs converted to string values (concatenate)
# The solution output should be in the format
# Integer: integer_sum_value Float: float_sum_value String: string_sum_value
 
# Sample Input/Output:
# If the input is
# 1
# 3
# 6
# 2
# 7
# then the expected output is
# Integer: 19
# Float: 19.0
# String: 13627


input_count = 5
input_list = []
integer_sum_value = 0
float_sum_value = 0.00
string_sum_value = ''

for x in range(input_count):
    input_list.append(str(input()))

for x in input_list:
    integer_sum_value += int(x)

for x in input_list:
    float_sum_value += float(x)

for x in input_list:
    string_sum_value += str(x)

print(f"Integer: {integer_sum_value}")
print(f"Float: {float_sum_value}")
print(f"String: {string_sum_value}")