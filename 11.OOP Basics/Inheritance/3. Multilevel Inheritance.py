class Animal:
    def __init__(self,name):
        self.name = name
        
    def info(self):
        print("Name:",self.name)

class Dog(Animal):       # Inherited method from Animal class
    def speak(self):
        print(self.name,"Barks")
        

class puppy(Dog):      # Inherited method from Dog class
    def weep(self):
        print(self.name,"Weeps")
        
        
dog1 = puppy("Buddy")
dog1.info()     
dog1.speak()
dog1.weep()