print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "You open the door and see a giant bear eating a cheese cake. What do you do?"
    print "1. You steal the cake."
    print "2. You fight the bear."
    
    bear = raw_input("> ")
    
    if bear == "1":
        print "As you attempt to steal the cake, the bear turns around and sees you coming up from behind."
        print "The bear grabs you by the neck and eats your head. Good luck. Try again."
    elif bear == "2":
        print "You see a wooden club by the door and run up behind the bear."
        print "The bear turns around and grabs you by the arm and eats your leg off. Good luck. Try again."
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear
        
elif door == "2":
    print "You stare endlessly in the abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespin."
    print "3. Understanding revolvers yelling melodies."
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives powered of a mind jello. Good job!"
    else:
        print "The insanity rots in your eyes into a pool of muck. Try again later."
    
else:
    print "You stumble and fall into a pool. Try again."
