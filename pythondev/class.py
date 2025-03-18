class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f'{self.name} makes sound')


class Puppy(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed


my_dog = Puppy("Buddy", "GoldenRetriever")
print(my_dog.species)
print(my_dog.name)
print(my_dog.breed)
my_dog.make_sound()

#activity
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f'{self.name} talks')

Jegan = Person("Jegan", 18)
print(Jegan.name)
print(Jegan.age)
Jegan.talk()

#inheritance
#single

class Parent:
    def show(self):
        print("Parent class method")

class Child(Parent):
    pass

obj = Child()
obj.show()  # Outputs: Parent class method


#Multiple Inheritance
#A child class inherits from more than one parent class.
class Father:
    def show_father(self):
        print("Father class method")

class Mother:
    def show_mother(self):
        print("Mother class method")

class Child(Father, Mother):
    pass

obj = Child()
obj.show_father()  # Outputs: Father class method
obj.show_mother()  # Outputs: Mother class method

#Multilevel Inheritance
#A class is derived from another derived class, creating a chain.

class Grandparent:
    def show_grandparent(self):
        print("Grandparent class method")

class Parent(Grandparent):
    def show_parent(self):
        print("Parent class method")

class Child(Parent):
    pass

obj = Child()
obj.show_grandparent()  # Outputs: Grandparent class method
obj.show_parent()       # Outputs: Parent class method

#. Hierarchical Inheritance
#Multiple child classes inherit from a single parent class.

class Parent:
    def show(self):
        print("Parent class method")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

obj1 = Child1()
obj2 = Child2()

obj1.show()  # Outputs: Parent class method
obj2.show()  # Outputs: Parent class method

#Hybrid Inheritance
#A combination of two or more types of inheritance. It involves multiple inheritance paths.
class Base:
    def show_base(self):
        print("Base class method")

class Child1(Base):
    pass

class Child2(Base):
    pass

class Grandchild(Child1, Child2):
    pass

obj = Grandchild()
obj.show_base()  # Outputs: Base class method
