try:
    with open("raj.txt","r") as file:
        content = file.read()
        print(content)
finally:
    file.close()