#classes and objects

#make class named Animal that is-a object
class Animal(object):
    pass
    
#make a Dog class that is-an Animal
class Dog(Animal):
    #class Dog has-a __init__ that takes self and name params
    def __init__(self, name):
        #from self get name attribute and set it to name
        self.name = name    
        
# make Cat class that is-an Animal
class Cat(Animal):
    #class Cat has-a __init__ that takes self and name params
    def __init__(self, name):
        #from self get name attribute and set it to name
        self.name = name
        
#make Person class that is-a object
class Person(object):
    #class Person has-a __init__ that takes self and name as params
    def __init__(self, name):
        #from self get name attribute and set to name
        self.name = name
        #Person has-a pet of some kind
        self.pet = None
    
#make class named Employee that is-a Person
class Employee(Person):
    #class Employee has-a __init__ that takes self, name and salary params
    def __init__(self, name, salary)
    #from 
    super(Employee, self).__init__(name)
