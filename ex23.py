#While Loops

numbers = []

def add(x):
    i = 0
    while i < x:
        print "Starting i at %d" % i
        numbers.append(i)
        
        new_add = int(raw_input("Give me a number to add. "))
        
        i = i + new_add
        print "We have these numbers in our list: ", numbers
        print "The current number we are at is %d" %i
    
    print "The number: "

    for num in numbers:
        print num
        
add(15)
