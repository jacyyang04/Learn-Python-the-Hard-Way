#classes and objects


##my notes##

#mystuff.apples() is a function like .capitalize()
#mystuff.tangerine can is a variable and can be printed with
#           print(mystuff.tangerine)
#as long as I imported the mystuff library/module

#create class Song
class Song(object):
    #create initial function
    #actually, it looks like a function but inside a class, with self as a parameter, it is a method
    #self refers to object
    #__init__ is a constructor, need self to every function
    def __init__(self, lyrics):
        self.lyrics = lyrics
    #create method that prints lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
    
#class is capitalized to differentiate between variables/objects
#I created two objects--happy_bday and bulls_on_parade with a LIST of string variables

#create a new object with class Song
happy_bday = Song(["Happy birthday to you",
                   "Alright, alright.",
                   "Okay. This is where we stop." ])
                   
bulls_on_parade = Song(["They rally around the famile",
                        "Wih pockets full of shells."])
                        


#accessing a function inside class Song for these Song objects
#happy_bday.sing_me_a_song()

#bulls_on_parade.sing_me_a_song()

#doowop is the object
#I am passing the lyrics to Song as an attribute to doowop
#think of attribute as a characteristic of the object
#I can look at specifically the attributes with the sing_me_a_song function
#                               doowop.sing_me_a_song()
doowop = Song(["Guys you know you'd better watch out",
               "Some girls, some girls are only about"])



