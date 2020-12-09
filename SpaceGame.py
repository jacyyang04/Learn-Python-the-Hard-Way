#Gothons from Planet Percel #25

#class for Maps
class Map(object):
    #class Maps has an init function that takes self and starting_scene params
    def __init__(self, starting_scene):
        pass
    #class Maps has a next_scene function that takes self and scene_name params
    def next_scene(self, scene_name):
        pass
    #class Maps has an opening_scene function that takes self
    def opening_scene(self):
        pass
        
#class for Scenes
class Scene(object):
    #class Scene has enter function that takes self
    def enter(self):
        pass

#make a Death class that is a Scene class        
class Death(Scene):
    #
    def enter(self):
        pass
    
class CentralCorridor(Scene):
    def enter(self):
        pass

class Weapons(Scene):
    def enter(self):
        pass
        
class Navigation(Scene):
    def enter(self):
        pass

class Bridge(Scene):
    def enter(self):
        pass

class EscapePod(Scene):
    def enter(self):
        pass
        
class Medic(Scene):
    def enter(self):
        pass


#class for Engine
class Engine(object):
    
    def __init__(self, scene_map):
        pass
    
    def play(self):
        pass


a_map = Map('central_cooridor')

a_game = Engine(a_map)

a_game.play()

