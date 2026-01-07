from collections import Counter
# Create a list of items
num = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Use Counter to count occurrences
cnt = Counter(num)
print(cnt)


#creating a counter

ctr1 = Counter([1, 2, 2, 3, 3, 3]) # From a list
ctr2 = Counter({1: 2, 2: 3, 3: 1}) # From a dictionary
ctr3 = Counter('hello') # From a string

print(ctr1)
print(ctr2)
print(ctr3)



ctr = Counter([1, 2, 2, 3, 3, 3])

# Accessing count of an element
print(ctr[1])  
print(ctr[2])  
print(ctr[3])  
print(ctr[4])  # (element not present)
print(ctr)
ctr.update([2, 3, 3, 4])  # Updating counts
print(ctr)
ctr.update({2:3,4:110})
print(ctr)
print(list(ctr.elements()))  # Getting all elements
print(ctr.total())  # Total count of all elements
print(ctr.most_common())  # Two most common elements




ctr1 = Counter([1, 2, 2, 3])
ctr2 = Counter([2, 3, 3, 4])

print(ctr1 + ctr2)   # Addition
print(ctr1 - ctr2)   # Subtraction 
print(ctr1 & ctr2)   # Intersection
print(ctr1 | ctr2)   # Union