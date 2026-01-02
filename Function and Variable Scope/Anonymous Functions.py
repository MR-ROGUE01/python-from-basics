def cube(x): print("Cube:", x*x*x)    # without lambda
cube_l = lambda x : print("Cube:",x*x*x)   # with lambda

cube(111)
cube_l(111)