class dog:
    species = "german shepherd" 
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        
dog1 = dog("sujal",2)
print(dog1.name)
print(dog1.age)
print(dog1.species)