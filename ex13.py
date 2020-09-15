#imports argv libaray from the sys package
from sys import argv

#sets up variables for argv
script, filename = argv

filename = input("What is the file you wish to open? ")
#txt variable to recieve the content of the file
#uses open() because open() is the recieve operation
txt = open(filename)

#filename is just the name of the file
#whereas txt now holds the content of the file

#prints the name of the file
print("Here's your file %r:" % filename)

#opens and prints the content of the file
#can only print content of the file 
print(txt.read())

txt.close()

#prompts user and sets the name equal to file_again variable
#print "Type the file name again: "
#file_again = input("> ")

#sets txt_again to recieve the content of file
#txt_again = open(file_again)

#prints the content of the file
#print txt_again.read()
#txt_again.close()
