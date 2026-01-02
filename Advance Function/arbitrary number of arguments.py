def add(*a):
    return sum(a)

print(add(1, 2, 3,4,7,8,5,3,2,4,6,5))  





def show(**a):
    for i, val in a.items():
        print(i, val)

show(a=10, b=20, c=30)


