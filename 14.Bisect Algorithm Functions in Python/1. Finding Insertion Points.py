import bisect
li = [1, 3, 4, 4, 4, 6, 7] 

print(bisect.bisect(li, 4)) # right
print(bisect.bisect_left(li, 4)) # left
print(bisect.bisect_right(li, 4, 0, 4)) # subright