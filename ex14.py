from sys import argv

script, filename = argv

#in terminal, it is typed in as
#python ex14.py (and then the name of the file)

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you DO want that, hit return.")

#CTRL-C creates this:
#Traceback (most recent call last):
#  File "ex14.py", line 12, in <module>
#    raw_input("?")
#KeyboardInterrupt

input("Do you want to continue?")

print("Opening the file...")

target = open(filename, "w")

#truncate deletes the content of the file
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines..")

#sets up new variables for user input
line1 = input("Line1: ")
line2 = input("Line2: ")
line3 = input("Line3: ")


print("Now I will add these lines to the file.")

#adds the line to the file
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

#adds the lines to the file, but on one line.
#can also write as:
#target.writelines([line1, line2, line3])
target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print("And finally, we close it.")
target.close()
