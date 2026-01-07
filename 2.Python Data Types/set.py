s1 = set()
s2 = set(['geeks','for','geeks','1'])
s3 = {'geeks','for','geeks'}

print(type(s1))
print(type(s2))
print(type(s3))

print(s3)
for i in s2:
    print(i,end = " ")

print('geeks' in s3)