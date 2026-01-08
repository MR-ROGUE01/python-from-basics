try:
    res = "100" / 20 # Risky operation: dividing string by number
    
except ArithmeticError :
    print("Arithmetic problem.")
    
except:
    print("Something went wrong!")