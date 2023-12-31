# Create a solution that accepts three integer inputs representing the number of times an employee travels to a job site. Output the total distance traveled to two decimal places given the following miles per employee commute to the job site. Output the total distance traveled to two decimal places given the following miles per employee commute to the job site:
# Employee A: 15.62 miles
# Employee B: 41.85 miles
# Employee C: 32.67 miles
# The solution output should be in the format
# Distance: total_miles_traveled
 
# Sample Input/Output:
# If the input is
# 1
# 2
# 3
# then the expected output is
# Distance: 197.33 miles


employee_distances = {'A':15.62,'B':41.85,'C':32.67}
total_miles_traveled = 0.00

for employee in employee_distances:
    total_miles_traveled += employee_distances[employee] * int(input())

print(f"Distance: {total_miles_traveled:.2f}")