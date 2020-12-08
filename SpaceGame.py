#Gothons from Planet Percel #25

#class for Maps
class Map(object):

    def __init__(self, starting_scene):
        pass
    
    def next_scene(self, scene_name):
        pass
    
    def opening_scene(self):
        pass
        
#class for Scenes
class Scene(object):

    def enter(self):
        pass
        
class Death(Scene):

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
