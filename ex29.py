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
    def __init__(self, name, salary):
    #call super function with Employee and self params, call __init__(name) function
    super(Employee, self).__init__(name)
    #from self, set salary attribute to salary
    self.salary = salary
    
#make Fish class that is-a object
class Fish(object):
    pass
    
#make Salmon class that is-a Fish
class Salmon(Fish):
    pass
    
#make Halibut class that is-a fish
class Halibut(Fish)
    pass
    
#rover is-a Dog
rover = Dog("Rover")

#satan is-a Cat
satan = Cat("Satan")

#mary is-a Person
mary = Person("Mary")

#from mary set pet attribute to satan
mary.pet = satan

#frank is-a Employee with Frank and 120000 params
frank = Employee("Frank", 120000)

#from frank set pet attribute to rover
frank.pet = rover

#set flipper as an instance of Fish
flipper = Fish()

#set crouse as an instance of Salmon
crouse = Salmon()

#set harry as an instance of Halibut
harry = Halibut()














