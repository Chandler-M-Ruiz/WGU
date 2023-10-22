# Create a solution that accepts an input identifying the name of a CSV file, for example, "input1.csv". Each file contains two rows of comma-separated values. Import the built-in module csv and use its open() function and reader() method to create a dictionary of key:value pairs for each row of comma-separated values in the specified file. Output the file contents as two dictionaries.
# The solution output should be in the format
# {key:value,key:value,key:value}
# {key:value,key:value,key:value}
 
# Sample Input/Output:
# If the file content is
# input1.csv
# then the expected output is
# {a:100,b:200,c:300}
# {bananas:1.85,steak:19.99,cookies:4.52}
# Alternatively, if the file content is
# input2.csv
# then the expected output is
# {d:400,e:500,f:600}
# {celery:2.81,milk:4.34,bread:5.63}

#I'll be honest, this is the question I struggle with most and don't even know where to begin beyond importing the files. Which is easy.
import csv

file_path = str(input())
dictionary1 = {}
dictionary2 = {}

with open(file_path,'r') as csv_file:
    csv_reader = csv.reader(csv_file)

#I understand that I can iterate through the item in the csv, and add them a singled dictionary, but I don't understand how to seperate them into TWO list?!
    for line in csv_reader:
        dictionary1[line[0]]=str(line[1])
print(dictionary1)