from tkinter import *
import sqlite3
from turtle import width

root = Tk()
root.title("Data Base")
root.geometry("900x900")

# Create a database or connect to one database
conn = sqlite3.connect('address_book.db') # doesn't exist so it will create it, will save it in the GUI directory

# Create cursor instance
c = conn.cursor() # execute command

# Create table (always use cursor), use SQL commands in the c.execute()
# do CREATE TABLE name ()   text, int, real (decimals), null (not exist), blob(image files, video) - All of SQL Lite Database
# for SQL to create a table, do: name, text
'''c.execute("""CREATE TABLE addresses (
    first_name text, 
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
)
    
""")''' # use """ twice in order to make the code easier, tables are big so these are neccesary
# ^ created a database, address_book.db - created
# Create function to delete a record
def edit():

    new_label = Label(root, text="Enter Password Below").grid(row=10,column=0)
    password = Entry(root)
    password.grid(row=11,column=0)
    def check():
        if password.get() == "YoWassup24":
            nope = Label(root, text="Owner").grid(row=13, column=0)
            delete_box_label = Label(root, text="ID number")
            delete_box_label.grid(row=1, column=3)
            delete_box = Entry(root, width=30)
            delete_box.grid(row=2, column=3)

            def delete1():
                conn = sqlite3.connect('address_book.db')
                c = conn.cursor()
                # to delete you need to concatenate the .get() afterward
                c.execute("DELETE FROM addresses WHERE oid= " + delete_box.get()) # do + delete_box at the end

                conn.commit()
                conn.close()
    # update record
            def update():
                editor = Tk()
                editor.title("Update Record")
                editor.geometry("700x700")
                # connect to data base each time we
                conn = sqlite3.connect('address_book.db')
                c = conn.cursor()
                # create a record id
                record_id = delete_box.get()
                # Query database, oid = original idea, primary key. Creates an unique idea
                # * - means everything
                c.execute("SELECT * FROM addresses where oid = " + record_id)
                # fetch all record
                records = c.fetchall()

                print_records = ''
                for record in records:
                    # "\t" will tab it over
                    # str(record[6]) is the unique ID number
                    print_records += str(record[0]) + " " + str(record[1]) + "  " + str(
                        record[6]) + " " + "\t" + "\n"  # \n = line break


                # Add data , create text boxes
                f_name_editor = Entry(editor, width=30)
                f_name_editor.grid(row=0, column=1, padx=20)
                l_name_editor = Entry(editor, width=30)
                l_name_editor.grid(row=1, column=1, padx=20)
                address_editor = Entry(editor, width=30)
                address_editor.grid(row=2, column=1, padx=20)
                city_editor = Entry(editor, width=30)
                city_editor.grid(row=3, column=1, padx=20)
                state_editor = Entry(editor, width=30)
                state_editor.grid(row=4, column=1, padx=20)
                zipcode_editor = Entry(editor, width=30)
                zipcode_editor.grid(row=5, column=1, padx=20)

                # create text box labels
                f_name_label = Label(editor, text="First Name")
                f_name_label.grid(row=0, column=0, pady=(10, 0))  # ten to top and 0 at bottom
                l_name_label = Label(editor, text="Last Name")
                l_name_label.grid(row=1, column=0, pady=(10, 0))
                address_label = Label(editor, text="Address")
                address_label.grid(row=2, column=0, pady=(10, 0))
                city_label = Label(editor, text="City")
                city_label.grid(row=3, column=0, pady=(10, 0))
                state_label = Label(editor, text="State")
                state_label.grid(row=4, column=0, pady=(10, 0))
                zipcode_label = Label(editor, text="Zip-Code")
                zipcode_label.grid(row=5, column=0, pady=(10, 0))

                # loop thru results
                for record in records:
                    f_name_editor.insert(0, record[0])
                    l_name_editor.insert(0, record[1])
                    address_editor.insert(0, record[2])
                    city_editor.insert(0, record[3])
                    state_editor.insert(0, record[4])
                    zipcode_editor.insert(0, record[5])


                edit_btn = Button(editor, text="Save Record", fg="white", bg="dark blue")
                edit_btn.grid(row=9,column=0, columnspan=2, pady=10, padx=10, ipadx=137)

            de_btn = Button(root, text="Delete Record", command=delete1, bg="black", fg="white")
            de_btn.grid(row=3, column=3, columnspan=2, pady=10, padx=10, ipadx=137)
            update_btn = Button(root, text="Update Record", command=update, bg="black", fg="white")
            update_btn.grid(row=4, column=3, columnspan=2, padx=10, ipadx=137, pady=10)

        else:
            nope = Label(root, text="Not Owner").grid(row=13,column=0)


    d_btn = Button(root, text="Submit", fg="black", bg="yellow", command=check)
    d_btn.grid(row=12,column=0)


# Create submit functions for Database creation
def submit():
    # create code to submit stuff
    # Create a database or connect to one database
    conn = sqlite3.connect('address_book.db')  # doesn't exist so it will create it, will save it in the GUI directory
    # Create cursor instance
    c = conn.cursor()  # execute command

    # Insert into Table
    # use placeholder variables , start with colon.
    # Create python dictionary, the key is the dummy variables made on the c.execute() line while the value is the user response
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()

              })


    # Commit changes
    conn.commit()
    # Close Connection
    conn.close()


    # Clear Textboxes , everytime we want the textboxes to clear to type in more Data
    f_name.delete(0, END) # delete 0 to end
    l_name.delete(0, END) # clear entry
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create query function
def query():
    # connect to data base each time we
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    # Query database, oid = original idea, primary key. Creates an unique idea
    c.execute("SELECT *, oid FROM addresses")
    # fetch all record
    records = c.fetchall()
    print_records = ''
    for record in records:
        # "\t" will tab it over
        # str(record[6]) is the unique ID number
        print_records += str(record[0]) + " " + str(record[1]) + "  " +str(record[6]) +" " +"\t" + "\n" # \n = line break
    query_label = Label(root, text=print_records) # print first and last name
    query_label.grid(row=8,column=0,columnspan=2) # each data set has a unique ID

    #print(records)
    conn.commit()
    conn.close()

# Add data , create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0,column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1,column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2,column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3,column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4,column=1, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5,column=1, padx=20)

#create text box labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0,column=0,pady=(10,0)) # ten to top and 0 at bottom
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1,column=0,pady=(10,0))
address_label = Label(root, text="Address")
address_label.grid(row=2,column=0,pady=(10,0))
city_label = Label(root, text="City")
city_label.grid(row=3,column=0,pady=(10,0))
state_label = Label(root, text="State")
state_label.grid(row=4,column=0,pady=(10,0))
zipcode_label = Label(root, text="Zip-Code")
zipcode_label.grid(row=5,column=0,pady=(10,0))


# Create Submit buttons
submit_btn = Button(root, text="Add Record to Database", command=submit, bg="black", fg="white") # submit function above text boxes
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query, bg="black", fg="white")
query_btn.grid(row=7,column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# create edit button
edit_btn = Button(root, text="Delete/Update Record (Only for Owner)", command=edit, bg="black", fg="white")
edit_btn.grid(row=9,column=0, columnspan=2, pady=10, padx=10, ipadx=137)
# Commit changes
conn.commit()
# Close Connection
conn.close()


root.mainloop()
