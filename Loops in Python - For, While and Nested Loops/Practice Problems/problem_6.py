n = int(input("Enter a Number: "))
for i in range(1, n + 1):
    for j in range(1,n+1):
        if j == i:
            print("1",end = " ")
        else:
            print("0",end = " ")
    print()