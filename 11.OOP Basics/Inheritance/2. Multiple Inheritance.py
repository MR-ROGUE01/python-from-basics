class Animal:
    def __init__(self,name):
        self.name = name
        
    def info(self):
        print("Name:",self.name)

class Dog():       
    def speak(self,sound):
        self.sound = sound
        print("It sounds:",self.sound)
        

class Breed(Animal,Dog):    #Inherited from both Animal and Dog classes
    def breed(self):
        print(self.name,"is a German Sheapard and it",self.sound)

        
dog1 = Breed("Buddy")
dog1.info()     
dog1.speak("Barks")
dog1.breed()