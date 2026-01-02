distance = int(input("Enter the distance:"))

if distance <= 2:
    print("You can walk")
elif distance <= 10:
    print("you can use Bicycle")
elif distance >= 10 and distance <= 100:
    print("you can use car or bike")
else:
    print("you can use train or plane")
    