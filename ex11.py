#modules is the same as libraries
#importing modules to this script
#argv holds the argument I pass to python
from sys import argv

#unpacks argv and assigns variables 
script, first, second, third, fourth = argv

#can set variables up as raw_input() but would need to make sure
#in terminal, run it as:
#python3 ex11.py first second third fourth
first = input("What is your favorite color? ", )
second = input("What is your favorite ice cream? ", )
third = input("What is your favorite drink? ", )
fourth = input("Who is your hero? ", )

#I can also run raw_input at the end.
print("The script is called:", script)
input("First variable is: ")
input("Second variable is: ")
input("Third variable is: ")
input("Fourth variable is: ")

#Output:

#in terminal, type [python3 ex11.py ___ ___ ___ ___]
#I would pick out the given arguments
#python ex11.py hello Jacy Yang

#The script is called: ex11.py
#First variable is: hello
#Second variable is: Jacy
#Third variable is: Yang

