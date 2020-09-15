#set x equal to sentence
x = 'There are %d types of people.' % 10

#set binary variable equal to string binary
binary = 'binary'

#set do_not equal to don't
do_not = "don't"

#set y equal to a sentence with binary and do_not variables
y = 'Those who know %s and those who %s.' % (binary, do_not)

#printing x and y
print(x)
print(y)

#pringint x and y variables within format character
print("I said: %r." % x)
print("I also said: '%s'." %y)

#set hilarious varible to false
hilarious = False

#set joke eval variable to string sentence with a format character
joke_eval = "Isn't that joke funny? %r"
 
#print joke_eval with hlarious as the format character
print(joke_eval % hilarious)
 
#set w and e variables to string
w = 'This is the left side of...'
e = 'a string with a right side.'

#print variables w and e 
print(w + e)
