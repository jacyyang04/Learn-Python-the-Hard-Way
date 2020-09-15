from sys import argv

#python3 ex17.py sample15.txt
#asking python to run ex17.py and uses sample15.txt as the input_file
script, input_file = argv

def print_all(f):
    print(f.read())

#rewind function puts the reading place at which you set it at seek(0)
#seek(0) sets the reading place back to the beginning
def rewind(f):
    f.seek(0)

#prints each line with the line count
def print_line(line_count, f):
    print(line_count, f.readline())
    

current_file = open(input_file)
#prints entire content
print("First, let's print the entire file: \n")
print_all(current_file)

#dont know what this does
print("Now let's rewind, kind of like a tape.")
rewind(current_file)

#prints each line individually
print("Now let's print three lines.")
#set up variable for line_count
current_line = 1
print_line(current_line, current_file)
print_line(current_line + 1, current_file)
print_line(current_line + 2, current_file)

current_file.close()
