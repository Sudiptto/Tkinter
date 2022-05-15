from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox # use for messageboxes

root = Tk()
root.title("Message")
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesorno , all the different types of options
def popup():
    #messagebox.showinfo("Hello World!")
    #messagebox.showwarning("Yo")
    response = messagebox.askquestion("What is math") # has yes or no,
    # if else statement
    if response == 'yes':
        Label(root, text="You clicked Yes!" ).pack()
    else:
        Label(root, text="You clicked No!").pack()

Button(root, text="Popup", command=popup).pack()


root.mainloop()