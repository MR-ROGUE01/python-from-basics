from collections import OrderedDict
print("This is a dict:\n")
d = {}
d['a'] = 1
d['b'] = 2              
d['c'] = 3
d['d'] = 4

for key,values in d.items ():
    print(key,values)

print("\nThis is an OrderedDict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2 
od['c'] = 3
od['d'] = 4

for key,values in od.items():
    print (key,values)