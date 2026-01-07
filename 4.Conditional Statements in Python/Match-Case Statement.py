number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")
        
#example 2
marks = 78

match marks:
    case m if m >= 90:
        print("Grade A")
    case m if m >= 75:
        print("Grade B")
    case m if m >= 50:
        print("Grade C")
    case _:
        print("Fail")
