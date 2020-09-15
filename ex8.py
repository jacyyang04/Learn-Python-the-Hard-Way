tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
hello_cat = "\ahellooo"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(hello_cat)

#prints item in the list and rotates until user decides to go to new line.
#I haven't figured out how to exit it.
#When you take away \r, it floods the terminal with the items in list
#while True:
#    for i in ["/", "-", "|", "\\", "|"]:
#        print("%s\r" % i)
#    False



#not sure when I would use the double quotes over the
#single quotes when it prints out the same.
new_cat = '''
I'm the new cat. MEOW.
'''

print(new_cat)

