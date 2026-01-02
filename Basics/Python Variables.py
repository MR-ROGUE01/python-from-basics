x = 5
name = "Samantha"  
print(x)
print(name)

#valid variable names   
age = 21
_colour = "lilac"
total_score = 90

#invalid variable names
'''
1name = "Error"  # Starts with a digit
class = 10       # 'class' is a reserved keyword
user-name = "Doe"  # Contains a hyphen
'''

#Dynamic Typing
x = 10
x = "Now a string"
print(x)   #outputs: Now a string

#Assigning the Same Value
a = b = c = 100
print(a,b,c)


#Assigning Different Values
x, y, z = 1, 2.5, "Python"
print(x, y, z)

#Basic Casting Functions
x = 200
y=float(x)
print(type(y))

z="200"
print(type(a))
a=int(z)
print(type(a))

#Delete a Variable Using del Keyword
x = 10
print(x) 
del x
# Trying to print x after deletion will raise an error
# print(x)  # Uncommenting this line will raise NameError: name 'x' is not defined
