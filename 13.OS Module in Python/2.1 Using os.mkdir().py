import os 
directory = "mrrogue01"
parent_dir = "D:/Python_codes/13.OS Module in Python"
path = os.path.join(parent_dir, directory)
#os.mkdir(path)
print("Directory '%s' created" % directory)
directory = "raj"
parent_dir = "D:/Python_codes/13.OS Module in Python"
mode = 0o666
path = os.path.join(parent_dir, directory)
#os.mkdir(path, mode)
print("Directory '%s' created" % directory)

