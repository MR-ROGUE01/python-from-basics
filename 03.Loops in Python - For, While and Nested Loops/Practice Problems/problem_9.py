n = int(input("Enter a Number: "))
for i in range(1, n + 1):
    if i % 2 == 0:
        continue
    else:
        print(f"Number : {i}")    
        