class Animal(object):
    def eat(self):
        print("eat")

    def __init__(self):
        print("Animal Constructor")
        self.age = 1

# Animal : Parent, Base
# Mammal : Child, Sub

class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal Constructor")
        self.weight = 2

    def walk(self):
        print("walk")

class Fish(Animal):

    def swim(self):
        print("swim")

class Bird(Animal):
    def fly(self):
        print("fly")

class Chicken(Bird):
    

# DRY don't repeat yourself

m = Mammal()
print(isinstance(m, Animal))
print(isinstance(Mammal, Animal))


print(isinstance(m, object))
o = object()
print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object))

print(m.age)
print(m.weight)