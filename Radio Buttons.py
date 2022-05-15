from tkinter import *
#from PIL import ImageTk,Image

root = Tk()
root.title('Radio Button')

"""r = IntVar() # allows for changes
r.set(2) # will set 2
# create tuples for radio buttons """
MODES = [
    ("P","P"),
    ("C","C"),
    ("D","D"), # d is text and the d to the left is MODE
    ("X","X"),
]
pizza = StringVar()
pizza.set("P")

for text,mode in MODES: # loop
    Radiobutton(root, text=text, variable=pizza, value=mode).pack()
def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()
# Radio Button Widget
# assign variable to each of the button and this variable can be used in the future
#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(pizza.get())).pack() # value=1, means option 1, need to define the variable
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()  # will keep on going

myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()
myLabel = Label(root, text=pizza.get())
myLabel.pack() # pack in screen
root.mainloop()