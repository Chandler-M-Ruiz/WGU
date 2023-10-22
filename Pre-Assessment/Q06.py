# Create a solution that accepts an integer input representing a 9-digit unformatted student identification number. Output the identification number as a string with no spaces.
# The solution output should be in the format
# 111-22-3333
 
# Sample Input/Output:
# If the input is
# 154175430
# then the expected output is
# 154-17-5430


id_input = str(input())
raw_id = []
first_three = ''
middle_two = ''
last_four = ''

for ch in id_input:
    raw_id.append(ch)

for ch in raw_id[0:3]:
    first_three += str(ch)

for ch in raw_id[3:5]:
    middle_two += str(ch)

for ch in raw_id[5:]:
    last_four += str(ch)

print(f"{first_three}-{middle_two}-{last_four}")