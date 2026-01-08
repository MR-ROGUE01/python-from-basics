marks = int(input("Enter a number: "))
match marks:
    case m if m<=40:
        print("Fail")
    case m if m<=50:
        primnt("Grade D")
    case M if m<=60:
        print("Grade C")
    case m if m<=70:
        print("Grade B")   
    case m if m<=80:
        print("Grade A")
    case m if m<=90 and m<=100:
        print("Grade A+")
    case m if m >= 90 and m<=100:
        print("Grade A++")
    case _:
        print("Invalid Marks")