class Animal:
    def __init__(self,name):
        self.name = name
        
    def info(self):
        print("Name:",self.name)

class Dog(Animal):       # Inherited method from Animal class
    def speak(self):
        print(self.name,"Barks")
        
        
dog1 = Dog("Buddy")
dog1.info()     
dog1.speak()