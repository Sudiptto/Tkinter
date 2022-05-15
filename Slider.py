from tkinter import *
from PIL import *

root = Tk()
root.geometry("400x400")
root.title("Slider ")
# Create a slider
vertical = Scale(root, from_=0, to=200, bg="black", fg="white") # create a vertical slider
vertical.pack()
# use .get() to grab response
def slide(): # set a variable
    my_label = Label(root, text=horizontal.get() ).pack()
    root.geometry(str(horizontal.get()) + "x400")

horizontal = Scale(root, from_=0, to=2000, bg="black", fg="white", orient=HORIZONTAL) # create a vertical slider
horizontal.pack() # use orient=HORIZONTAL to make horizontal

my_button = Button(root, text="Click Me", command=slide).pack()
root.mainloop()