class employee:
    def __init__(self):
        self.salary=50000
    
    def get_salary(self):
        return self.salary
    def set_salary(self,amount):
        if amount > 0:
            self.salary = amount
        else:
            print("Invalid salary")

emp = employee()
print(emp.get_salary())
emp.set_salary(60000)
print(emp.get_salary())