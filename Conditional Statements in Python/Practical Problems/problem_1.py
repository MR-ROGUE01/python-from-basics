'''Problem 1: Check if user is eligible to vote
This program checks if a person is eligible to vote based on their age. 
It takes the user's age as input and uses an if statement to determine if the age is 18 or above,
which is the legal voting age in many countries.'''

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")