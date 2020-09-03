#Lists and Loops

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'peaches']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loops goes through a list
for numbers in the_count:
    print "This is count %d." % numbers

for fruit in fruits:
    print "A type of fruit: %s" % fruit
    
for i in change:
    print "I got %r." % i
    

#how to build lists
#create an empty list
elements = []

for i in range(0,6):
    print "Adding %d to the list." % i
    #append (add) to the list
    elements.append(i)
    print "Element added was %d." % i
