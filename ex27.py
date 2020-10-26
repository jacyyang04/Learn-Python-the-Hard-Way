#classes and objects

#create class Song with object
class Song(object):
    #create variable
    def __init__(self, lyrics):
        self.lyrics = lyrics
    #create function
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


#Happy bday object as a class Song
#class is capitalized to differentiate between variables/objects
happy_bday = Song(["Happy birthday to you",
                   "Alright, alright.",
                   "Okay. This is where we stop." ])
                   
bulls_on_parade = Song(["They rally around the famile",
                        "Wih pockets full of shells."])
                        

happy_bday.sing_me_a_song()


bulls_on_parade.sing_me_a_song()
