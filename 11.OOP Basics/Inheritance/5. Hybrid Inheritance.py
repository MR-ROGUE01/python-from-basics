class Animal:
    def __init__(self,name):
        self.name = name
        
    def info(self):
        print("Name:",self.name)

class Dog(Animal):       # Inherited method from Animal class
    def speak(self):
        print(self.name,"Barks")
        
class Cat(Animal):       # Inherited method from Animal class
    def meow(self):
        print(self.name,"Meows")
        
class Age(Dog,Cat):
    def age(self,age):
        self.age=age
        print(self.name,"is",self.age,"years old")


dog1 = Dog("Buddy")
dog1.info()     
dog1.speak()


cat1 = Cat("Kitty")
cat1.info()
cat1.meow()

age1 = Age("Tommy")
age1.info()
age1.speak()
age1.age(3)