# Create a solution that accepts an integer input to compare against the following list:
predef_list = [4, -27, 15, 33, -10]
# Output a Boolean value indicating whether the input value is greater than the maximum value from predef_list
# The solution output should be in the format
# Greater Than Max? Boolean_value
 
# Sample Input/Output:
# If the input is
# 20
# then the expected output is
# Greater Than Max? False


Boolean_value = True
user_input = int(input())

for num in predef_list:
    if num >= user_input:
        Boolean_value = False

print(f"Greater Than Max? {Boolean_value}")