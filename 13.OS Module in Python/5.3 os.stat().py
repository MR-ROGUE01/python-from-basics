import os

stats = os.stat("raj.txt")

print("Size:", stats.st_size, "bytes")
print("Last modified:", stats.st_mtime)
print("Permissions:", oct(stats.st_mode)[-3:])

print(os.name)