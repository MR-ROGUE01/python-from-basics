import os
directory = "raj1"
parent_dir = "D:/Python_codes/13.OS Module in Python"
path = os.path.join(parent_dir , directory)
#os.makedirs(path)
print("Directory '%s' created "%directory)

import os
directory = "raj2"
parent_dir = "D:/Python_codes/13.OS Module in Python"
path = os.path.join(parent_dir , directory)
mode = 0o666
os.makedirs(path, mode)
print("Directory '%s' created "%directory)

