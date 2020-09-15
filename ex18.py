#putting it all together

print("Let's practice everythingggggggggg")

print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
canoot disern \nthe needs of love
nor comprehend passion from intuition
and requires explaination
\n\twhere there is none.
"""

print("---------------")
print(poem)
print("---------------")

five = 10-2+3-6
print("This should be five: %s" %five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
    
startpoint = 10000
#assign variables to the return values from secret_formula
beans, jars, crates = secret_formula(startpoint)
 
print("With a starting point of: %d" %startpoint)
print("We'd have %d beans, %d jars and %d crates." % (beans, jars, crates))
 
startpoint = startpoint/10
 
print("We can also do it this way:")
#returns the value into the statement
print("We'd have %d beans, %d jars and %d crates." % secret_formula(startpoint))
