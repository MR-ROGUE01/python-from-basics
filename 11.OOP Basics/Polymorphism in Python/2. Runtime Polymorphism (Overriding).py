class Animal:
    def sound(self):
        return "some generic sound"
class Dog(Animal):
    def sound(self):
        return "Bark"
class Cat(Animal):
    def sound(self):
        return "meow"
    
animals = [Cat(), Dog(), Animal()]
for animal in animals:
    print(animal.sound())