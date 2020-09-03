#modules is the same as libraries
#importing modules to this script
#argv holds the argument I pass to python
from sys import argv

#unpacks argv and assigns variables 
script, first, second, third, fourth = argv

#can set variables up as raw_input() but would need to make sure
#in terminal, run it as:
#python ex11.py first second third fourth
#first = raw_input("What is your favorite color? ", )
#second = raw_input("What is your favorite ice cream? ", )
#third = raw_input("What is your favorite drink? ", )
#fourth = raw_input("Who is your hero? ", )

#I can also run raw_input at the end.
print "The script is called:", script
raw_input("First variable is: ")
raw_input("Second variable is: ")
raw_input("Third variable is: ")
raw_input("Fourth variable is: ")

#Output:

#in terminal, type [python ex11.py ___ ___ ___ ___]
#I would pick out the given arguments
#python ex11.py hello Jacy Yang

#The script is called: ex11.py
#First variable is: hello
#Second variable is: Jacy
#Third variable is: Yang

