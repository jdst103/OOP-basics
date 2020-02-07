# following seperation of concerns & abstraction
from animal_class import Animal
from reptile_class import Reptile

#Creating Instances of class
animal_nemo = Animal('Nemo', 10)
animal_ringo = Reptile('ringo', '4')


#calling animal methods
print(animal_nemo.eat())

#calling reptile methods
print(type(animal_ringo))
print(animal_ringo.eat())
print(animal_ringo.eat())

# print(animal_nemo.lay_eggs) --> wont work as this animal dont have that method/attrbiute (behaviour)