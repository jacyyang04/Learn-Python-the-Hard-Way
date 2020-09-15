#copying files

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

#set equal to content
in_file = open(from_file)
#read content operator 
indata = in_file.read()

print("The input file is %d bytes long!" % len(indata))

#exists function will return true if file exists.
print("Does the output file exist? %r" % exists(to_file))

#prompts user for readiness
print("Ready? Hit RETURN to conintue.  CTRL-C to abort.")
input(">" )

#create new variable and set equal to new file with writing abilities
out_file = open(to_file, 'w')

#write in indata variable, which is equal to contents in from_file
out_file.write(indata)

print("Alright, done.")


out_file.close()
in_file.close()

#trying to write this in fewer lines
