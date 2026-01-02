number = 1
if number:
    print("This will print because 7 is truthy.")

number = 0
if number:
    print("This will NOT print because 0 is falsy.")


#examples2 of truthy values
if [1, 2]:
    print("Non-empty list is truthy")

if -1:
    print("-4 is truthy")

#examples of falsy values
if not 0:
    print("0 is falsy")

if not []:
    print("Empty list is falsy")

if not "":
    print("Empty string is falsy")