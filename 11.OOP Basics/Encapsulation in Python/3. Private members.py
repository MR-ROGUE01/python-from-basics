class employee:
    def __init__(self,name,age):
        self.name=name  #public attribute
        self.__age=age  #private attribute
    
    def display(self):
        print("Age:",self.__age)
        
        
emp = employee("Raj",21)
print("Name:",emp.name)
emp.display()          # Accessing private correctly