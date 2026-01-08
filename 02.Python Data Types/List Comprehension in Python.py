a = [2,3,4,5]
res = [val ** 2 for val in a]
print(res)

#using for loop
a = [1, 2, 3, 4, 5]
res = []
for val in a:
    res.append(val * 2)
print(res)

#using list comprehension
a = [1, 2, 3, 4, 5]
res = [val * 2 for val in a]
print(res)

a = [1, 2, 3, 4, 5]
res = [val for val in a if val % 2 == 0]
print(res)

a = [i for i in range(10)]
print(a)