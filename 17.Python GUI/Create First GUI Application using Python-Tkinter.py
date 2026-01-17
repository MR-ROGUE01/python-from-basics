# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Adobe Photoshop")
# Set geometry(widthxheight)
root.geometry('1080x1920')

# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar 
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
item.add_command(label='Help')
item.add_command(label='Find')
item.add_command(label='Open')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)


# adding a label to the root window
lbl = Label(root, text = "Are you a Geek?")
lbl.grid(row=5, column=5)

# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column =6, row =5)


# function to display user text when
# button is clicked
def clicked():

    res = "You wrote" + txt.get()
    lbl.configure(text = res)

# button widget with red color text inside
btn = Button(root, text = "Click me" ,
             fg = "red", command=clicked)
# Set Button Grid
btn.grid(column=7, row=5)

# Execute Tkinter
root.mainloop()