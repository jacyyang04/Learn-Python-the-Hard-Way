from sys import argv

script, user_name, food = argv
prompt = "> "

print "Hi %s, I'm the %s script." %(user_name, script)
print "I 'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
live = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

food = raw_input("What is your favorite food? ")

print "Perfect, I have found %r %r restuarants in %s" % (16, food, live)

print """
Alright, you said %r about liking me.
You live in %r. Not sure where that is.
And you have an %r computer. Nice.
""" % (likes, live, computer)
