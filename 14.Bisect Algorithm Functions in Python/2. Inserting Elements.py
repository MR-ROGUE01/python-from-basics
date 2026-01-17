import bisect
l1 = [1, 3, 4, 4, 4, 6, 7]  
l2 = [1, 3, 4, 4, 4, 6, 7]  
l3 = [1, 3, 4, 4, 4, 6, 7]  

bisect.insort(l1, 5) # right
print(l1) 

bisect.insort_left(l2, 5) # left
print(l2)

bisect.insort_right(l3, 5, 0, 4) # subright
print(l3)