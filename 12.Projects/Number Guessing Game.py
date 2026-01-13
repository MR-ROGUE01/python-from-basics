def guessnumber(startrange,endrange):
    if startrange > endrange:
        return True
    
    mid = (startrange + endrange) // 2
    
    print(f"Is Your Number {mid} :",end="")
    user = input().strip()
    
    if user in ("Y","y"):
        print("Yay! I guessed your number.")
        return True
    
    elif user in ("N","n"):
        print(f"Is the actual number is greater than {mid} :",end ="")
        
        user = input().strip()
        
        if user in ("Y","y"):
            return guessnumber(mid+1,endrange)
        elif user in ("N","n"):
            return guessnumber(startrange,mid-1)
        else:
            print("Invalid Input! Please enter Y or N.")
            return guessnumber(startrange,endrange)
        
    else:
        print("Invalid Input! Please enter Y or N.")
        return guessnumber(startrange,endrange)
    
print("Number Guessing Game in Python!")
startrange = int(input("Enter the starting range: "))
endrange = int(input("Enter the ending range: "))

out = guessnumber(startrange,endrange)
if out:
    print("Game Over!")
    
    
    
    