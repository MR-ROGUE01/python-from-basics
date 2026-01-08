file = open("raj.txt","w+") 
file.write("This is Raj's file.\nHe is learning Python file handling.")
file.seek(0)
content = file.read()
print(content)
file.close()


