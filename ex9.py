print "How old are you?",
#raw input prompts user
age = raw_input()

print "How tall are you?",
height = raw_input()

print "How much do you weight?",
#using int() will automatically convert the string into integer
weight = int(raw_input())

#height will come out as "5'\0" because the user typed in 5'0".
#this way, it keeps the middle apostraphy. Won't show up like that if
#%r is changed to %s.
print "So, you're %r years old, %r tall and %r heavy" % (age, height, weight)
