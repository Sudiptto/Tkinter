from tkinter import *
from PIL import Image, ImageTk
root = Tk()
my_img = ImageTk.PhotoImage(Image.open("Images/tkinter1.png")) # works since same file  , can add them to anything
# Key note: do /images/tkinter1 (have a file of images), in image folder
my_img1 = ImageTk.PhotoImage(Image.open("Images/ImageViewApp1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("Images/ImageViewApp2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("Images/ImageViewApp3.png"))

# use a list
image_list = [my_img1, my_img2, my_img3]
status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E, bg="black", fg="white")
my_label = Label(image=my_img3)
my_label.grid(row=0, column=0, columnspan=3)
# set up method
def forward(image_numbers):
    # use global so it can be used outside
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget() # function that can get rid of the label
    my_label = Label(image=image_list[image_numbers-1]) # add the new image , current image -1 since lists start at 0
    my_label.grid(row=0, column=0, columnspan=3) # put it on screen
    button_forward = Button(root, text=">>", command=lambda: forward(image_numbers+1)) # next image will pop up
    button_back = Button(root, text="<<", command=lambda: back(image_numbers-1)) # subtract one

    # prevent the list from going outsideof range
    if image_numbers == len(image_list):
        button_forward = Button(root, text=">>", state=DISABLED) # will stop once it hits the max
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status = Label(root, text="Image "+ str(image_numbers) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E, bg="black",
                   fg="white")
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)
def back(image_numbers):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()  # function that can get rid of the label
    my_label = Label(image=image_list[image_numbers - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_numbers + 1))  # next image will pop up
    button_back = Button(root, text="<<", command=lambda: back(image_numbers - 1))  # subtract one

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    # update status bar
    status = Label(root, text="Image " + str(image_numbers) + " of " + str(len(image_list)), bd=1, relief=SUNKEN,
                   anchor=E, bg="black",
                   fg="white")
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)
    if image_numbers == 0:
        button_back = Button(root, text="<<", state=DISABLED) # will stop once it hits the max
# set up buttons
button_back = Button(root, text= "<<", command=back, state=DISABLED) # don't need to pass anything back
button_exit = Button(root, text= "EXIT PROGRAM", command=root.quit)
button_forward = Button(root, text= ">>", command=lambda: forward(2))
# positions below
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2,column=0, columnspan=3, sticky=W+E)
root.mainloop()
