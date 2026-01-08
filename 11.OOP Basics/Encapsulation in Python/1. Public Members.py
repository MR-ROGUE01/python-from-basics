class employee:
    def __init__(self,name,age):
        self.name=name  #public attribute
        self.age=age    #public attribute
        
    def display(self):  #public method
        print("Name:",self.name)
        print("Age:",self.age)
        
emp1=employee("Raj",21)
emp1.display()
print("Name:",emp1.name)
print("Age:",emp1.age)
        