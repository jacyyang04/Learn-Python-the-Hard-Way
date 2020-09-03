from sys import exit

def gold_room():
    print "This room is full of gold. Mow much do you take?"
    
    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)    
    else:
        dead("You need to enter a number.")
        gold_room()

    if how_much < 50:
        print "Nice, you're not greedy. You win!"
        exit(0)
    else:
        dead("You're a greedy person. Tsk tsk tsk.")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    
    bear_moved = False
    
    while True:
        next = raw_input(">")
        
        if next == "take honey":
            dead("The bear gets angry and chases you out the room.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved. You can get through now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets angry and chases you out of the room.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "Please try again."
            

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and it starts to get weird."
    print "Do you flee for your life or let it eat your head?"
    
    next = raw_input("> ")
    
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty.")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)


def start():
    print "You are in a dark room."
    print "There is a door to your right and a door to your left."
    print "Which one will you take?"
    
    next = raw_input("> ")
    
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumbled around this room for hours and eventually die")
       
       
        
start()





