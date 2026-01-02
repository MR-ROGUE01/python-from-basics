dict = {
    1:{'Name' : 'Raj', "Age" : '21', 'Roll' : 66},
    2:{'Name' : 'Anu', "Age" : '22', 'Roll' : 67} }
print("Dictionary Items: ", dict)
print(dict[1])
print(dict.get(2))
print(dict[1]['Name'])
print(dict.get(2).get('Age'))