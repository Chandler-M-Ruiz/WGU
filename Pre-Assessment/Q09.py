# Create a solution that accepts an integer input representing water temperature in degrees Fahrenheit. Output a description of the water state based on the following scale:
 
# If the temperature is below 33° F, the water is “Frozen”.
# If the water is between 33° F and 80° F (including 33), the water is “Cold”.
# If the water is between 80° F and 115° F (including 80), the water is "Warm".
# If the water is between 115° F and 211° (including 115) F, the water is “Hot".
# If the water is greater than or equal to 212° F, the water is “Boiling”.
# Additionally, output a safety comment only during the following circumstances:
# If the water is exactly 212° F, the safety comment is "Caution: Hot!"
# If the water temperature is less than 33° F, the safety comment is "Watch out for ice!"
# The solution output should be in the format
# water_state
# optional_safety_comment
 
# Sample Input/Output:
# If the input is
# 118
# then the expected output is
# Hot
# Alternatively, if the input is
# 32
# then the expected output is
# Frozen
# Watch out for ice!


temp = int(input())
water_state = ''
optional_safety_comment = ''
# If the temperature is below 33° F, the water is “Frozen”.
# If the water temperature is less than 33° F, the safety comment is "Watch out for ice!"
if temp < 33:
    water_state = 'Frozen'
    optional_safety_comment = 'Watch out for ice!'
# If the water is between 33° F and 80° F (including 33), the water is “Cold”.
elif temp >= 33 and temp < 80:
    water_state = 'Cold'
# If the water is between 80° F and 115° F (including 80), the water is "Warm".
elif temp >= 80 and temp < 115:
    water_state = 'Warm'
# If the water is between 115° F and 211° (including 115) F, the water is “Hot".
elif temp >= 115 and temp < 211:
    water_state = 'Hot'
# If the water is exactly 212° F, the safety comment is "Caution: Hot!"
elif temp == 212:
    water_state = 'Boiling'
    optional_safety_comment = 'Caution: Hot!'
# If the water is greater than or equal to 212° F, the water is “Boiling”.
else:
    water_state = 'Boiling'


print(water_state)
if optional_safety_comment != '':
    print(optional_safety_comment)