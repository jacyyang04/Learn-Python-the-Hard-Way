#Gothons from Planet Percel #25

#create class Map
class Map(object):
    #class Maps has an init function that takes self and starting_scene params
    def __init__(self, starting_scene):
        pass
    #class Maps has a next_scene function that takes self and scene_name params
    def next_scene(self, scene_name):
        pass
    #class Maps has an opening_scene function that takes self params
    def opening_scene(self):
        pass
        
#create class Scene
class Scene(object):
    #class Scene has enter function that takes self params
    def enter(self):
        pass

#make a Death class that is an object of Scene class        
class Death(Scene):
    #class Death has an enter function that takes self params
    def enter(self):
        pass
    
#make a CentralCorridor class that is an object of Scene classs
class CentralCorridor(Scene):
    #class CentralCorridor has an enter function that takes self params
    def enter(self):
        pass

#make Weapons class an object of Scene class
class Weapons(Scene):
    #class Weapons has enter function that takes self params
    def enter(self):
        pass

#make Navigations class an object of Scene class     
class Navigation(Scene):
    #class Navigation has an enter function that takes self params
    def enter(self):
        pass

#make Bridge class an object of Scene
class Bridge(Scene):
    #class Bridge has an enter function that takes self params
    def enter(self):
        pass

#make EscapePod class an object of Scene
class EscapePod(Scene):
    #class EscapePod has an enter function that takes self params
    def enter(self):
        pass

#make Medic class an object of Scene
class Medic(Scene):
    #class Medic has an enter function that takes self params
    def enter(self):
        pass


#create class Engine 
class Engine(object):
    
    #Engine class has an __init__ function that takes self and scene_map params
    def __init__(self, scene_map):
        pass
    
    #Engine class has play funtion that takes self params
    def play(self):
        pass


a_map = Map('central_cooridor')

a_game = Engine(a_map)

a_game.play()

