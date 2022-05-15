from tkinter import *
root = Tk()

# Create tkinter variables, int since when you check a box the value is either a 1 or a 0.
# 1 = Checked, 0 = not checked
var = IntVar() # can also be string
# Check button
c = Checkbutton(root, text="Check", variable=var) # create a check box
c.pack()
def show():
    myLabel = Label(root, text=var.get()).pack()

my_button = Button(root, text="Selection", command=show).pack() # 1 = Clicked
# Strings underneath
var2 = StringVar()
c1 = Checkbutton(root, text="Check", variable=var2, onvalue="On", offvalue="Off") # on if clicked, no click = off
c1.deselect() # deselect by default
c1.pack()
def sho1w():
    myLabel = Label(root, text=var2.get()).pack()


my_button2 = Button(root, text="Selection", command=sho1w).pack()  # 1 = Clicked


root.mainloop()