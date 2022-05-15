from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Open File Dialog")
# Open a file
# First tell the program what directory you want it to open (use initialdir= /GUI/Images
# Second use a filetype() which can show the specific files, ex show the PNG files or all of them ,etc (use filetypes="png files"
# Three - specify all files and the * represents the anyname, *.* = any name , any extension
root.filename = filedialog.askopenfilename(initialdir="/GUI/Images", title="Select A file", filetypes=(("png files", "*.png"),("all files", "*.*")))
# Can also set as a button
my_label = Label(root, text=root.filename).pack() # will return the image of the location
# open the image, it contains the location
my_image = ImageTk.PhotoImage(Image.open(root.filename))
my_image_label = Label(image=my_image).pack()


root.mainloop()
