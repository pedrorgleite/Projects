from tkinter import *
from Scrabble_v2 import *

root = Tk()

e = Entry(root, width=50)
e.pack()

def myClick():
    myLabel2 = Label(root, text=e.get())
    myLabel2.pack()


myButton = Button(root, text="Enter Your Name", command=myClick, bg="black", fg="white")
myButton.pack()
# Creating a label widget
myLabel = Label(root, text="Hello World!")
#shoving it onto the screen
myLabel.pack()

root.mainloop()