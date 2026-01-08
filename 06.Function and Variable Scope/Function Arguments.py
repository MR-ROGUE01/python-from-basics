def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))

# Default Arguments
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(10)

#2. Keyword Arguments
def students(fname,lname):
    print(fname,lname)
    
students(fname = "raj" , lname = "satyam")
students(lname = "satyam" , fname = "raj")


#3. Positional Arguments
def details(name, age):
    print(f"Name:{name}  Age:{age}")
          
          
details("raj",21)
details("satyam",23)

#4. Arbitrary Arguments
def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

# Function call with both types of arguments
myFun('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')