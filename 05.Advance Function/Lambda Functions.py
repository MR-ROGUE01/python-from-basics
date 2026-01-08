s1 = 'GeeksforGeeks'
s2 = lambda func: func.upper()
print(s2(s1))


n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(n(5))   
print(n(-3))  
print(n(0))