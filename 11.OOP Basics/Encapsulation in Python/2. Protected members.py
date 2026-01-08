class employee:
    def __init__(self,name,age):
        self.name=name  #public attribute
        self._age=age  #protected attribute
        

class subemployee(employee):
    def showage(self):
        print("Age:",self._age)
    def showname(self):
        print("Name:",self.name)
        
emp = subemployee("Raj",21)
emp.showname()
emp.showage()
print("Name:",emp.name)
print("Age:",emp._age)