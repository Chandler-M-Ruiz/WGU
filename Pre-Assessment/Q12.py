# Create a solution that opens a file and combines the words on each line into a sentence. Write the sentence string to the end of the text file "WordTextFile1.txt" on a new line. Output the new contents of "WordTextFile1.txt". Use the open() function and write(), read() methods to interact with the text file.
# The solution output should be in the format
# WordTextFile1.txt_contents
# sentence
 
# Sample Input/Output:
# If the file content is
# WordTextFile1.txt
# then the expected output is
# cat
# chases
# dog
# cat chases dog

word_list = []
sentence = ''

with open("path/to/file/WordTextFile1.txt", 'r') as line_file:
    line_reader = line_file.readlines()
    for line in line_reader:
        word_list.append(line.strip())

#HOW THE QUESTION/ROBOT WANTS THE ANSWER. Why go through all the work of creating a useless string? It's an extra step and breaks the for loop out of the with open.
for word in word_list:
    if word != word_list[-1]:
        sentence += str(word)
        sentence += " "
    else:
        sentence += word

with open("path/to/file/WordTextFile1.txt", 'a') as write_file:
    write_file.write("\n")
    write_file.write(sentence)

#MY PREFFERED WAY OF HANDLING THIS TASK. NO NEED FOR 'SENTENCE' CRAP. Everything is together and makes sense and saves two lines of code. Which saves trees. Probably.
# with open("path/to/file/WordTextFile1.txt", 'a') as write_file:
#     write_file.write("\n")
#     for word in word_list:
#         if word != word_list[-1]:
#             write_file.write(word)
#             write_file.write(" ")
#         else:
#             write_file.write(word)

with open("path/to/file/WordTextFile1.txt", 'r') as read_file:
    file_reader = read_file.read()
    print(file_reader)