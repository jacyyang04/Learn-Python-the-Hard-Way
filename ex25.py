#Doing things in Lists

ten_things = "Apples Oranges Birds Phones Light Sugar"

print("Wait, there's not 10 things in that list. Let's fix that.")

#splits when there is a space
stuff = ten_things.split(' ')
print(stuff)
#list
more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print('Adding..', next_one)
    stuff.append(next_one)
    print("There's %d items now" % len(stuff))
    
print("There we go: ", stuff)

print("Let's do some things with stuff.")

#prints the second item in the list
print(stuff[1])

#prints last item in list
print(stuff[-1])

#removes item
print(stuff.pop())

#joins stuff with ' ' between them
print(' '.join(stuff))

#joins # between items 4 and 5 in list stuff
print('#'.join(stuff[3:5]))
