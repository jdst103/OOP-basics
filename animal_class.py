    # class Animal():
    #     # characterstics
    #     def __init__(self, name, legs, eyes, claws, tasty):  # if we dont follow order, use dictionary to define.
    #         self.name = name
    #         self.legs = legs
    #         self.eyes = eyes
    #         self.claws = claws
    #         self.tasty = tasty

class Animal():
    # characterstics
    def __init__(self, name, legs):     #if we dont follow order, use dictionary to define.
        self.name = name
        self.legs = legs

    # behaviours - methods
    # methods - which are like functions that belong to a class
    # what it would be called

    def eat(self, food=''): # makes the arguement optional
        return 'nom' * 3 + food

    def sleep(self):
        return 'zzzz'

    def potty(self):
        return 'O_0 ...... HUMMMM!!!! ---- O_o ---- SPLOSH!'

    def hunt(self):
        return 'ATTACK'


# Let us create an instance of an Animal object, (also lets assign it to a variable)

animal_1 = Animal('Randy Marsh', 10, )
animal_2 = Animal('Cartman', 8, )

#checking attributes
# print(animal_1)              #when run the instance changes every time (look at the number) # cant do much with it
# print(type(animal_1))
#
# print(animal_1.legs)   #how tasty it is
# print(animal_2.legs)

# call methods on object of class Animal:
# print(animal_1.eat('chicken and salad'))
# print(animal_1.eat('dunno'))
# print(animal_1.sleep())
# print(animal_1.hunt())
# print(animal_1.potty())