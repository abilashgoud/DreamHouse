from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
import mysql.connector

db = mysql.connector.Connect(
    host='localhost',
    user='root',
    # password=password,
    database='dreamhome'
)


def back():
    root.destroy()
    os.system("python main.py")


def submit_data():
    cursor = db.cursor()
    branch_number = branch_number_entry.get()

    sql = "select propertyNo,type, rooms,rent,address from propertyforrent where branchNo=%s and currentStatus='Y';"
    val = (branch_number,)
    cursor.execute(sql, val)
    result = cursor.fetchall()
    for row in result:
        table.insert('', 'end', values=row)

    db.commit()


root = Tk()
root.title("Property Listing")
root.geometry('1020x460')
root.configure(bg="#5DD9C1")

view_head_label = Label(root, text="PROPERTY LISTING", font=(
    "Arial", 20, "bold"), bg="#5DD9C1", fg="#36453B")
view_head_label.place(x=420, y=20)

branch_number_label = Label(
    root, text="Branch Number : ", bg="#5DD9C1", fg="#36453B", font=("Arial", 13))
branch_number_label.place(x=10, y=80)

branch_number_entry = Entry(root, width=20, bg="white", fg="#36453B")
branch_number_entry.place(x=150, y=80)

table = ttk.Treeview(root, columns=(
    'Property Number', 'Type', 'Rooms', 'Rent', 'Address'), show='headings')
table.heading('Property Number', text='Property Number')
table.heading('Type', text='Type')
table.heading('Rooms', text='Rooms')
table.heading('Rent', text='Rent')
table.heading('Address', text='Address')
table.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

submit_but = Button(root, text="Submit", width=10,
                    bg="#ACFCD9", fg="#36453B", font=("Arial", 12), command=submit_data)
submit_but.place(x=900, y=420)
back = Button(root, text="Back", width=10, bg="#ACFCD9", fg="#36453B",
              font=("Arial", 12), command=back).place(x=45, y=420)

root.mainloop()
