from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    # password=password,
    database='dreamhome'
)

root = Tk()
root.title("Staff Listing")
root.geometry('720x460')
root.configure(bg="#5DD9C1")


def back():
    root.destroy()
    os.system("python Staff.py")
    # insert the code to go back to the previous page here


def populate_table():
    cursor = db.cursor()
    branch_no = branch_no_entry.get()
    sql = "select * from staff where branchNo= %s"
    val = (branch_no,)
    cursor.execute(sql, val)
    result = cursor.fetchall()
    for row in result:
        table.insert('', 'end', values=row)
    db.commit()
    # insert the code to populate the table with data here


Staff_list_head_label = Label(root, text="Staff Listing", font=(
    "Arial", 20, "bold"), bg="#5DD9C1", fg="#36453b")
Staff_list_head_label.place(x=295, y=20)

branch_no_label = Label(root, text="Branch No",
                        bg="#5DD9C1", fg="#36453b", font=("Arial", 13))
branch_no_label.place(x=45, y=80)

branch_no_entry = Entry(root, width=30)
branch_no_entry.place(x=145, y=82)

table = ttk.Treeview(root, columns=(
    'Staff Number', 'Name', 'Position'), show='headings')
table.heading('Staff Number', text='Staff Number')
table.heading('Name', text='Name')
table.heading('Position', text='Position')

table.place(x=45, y=200)

submit_but = Button(root, text="Submit", width=10, bg="#36453b",
                    fg="white", font=("Arial", 12), command=populate_table)
submit_but.place(x=47, y=130)

back_button = Button(root, text="Back", width=10, bg="#36453b",
                     fg="white", font=("Arial", 12), command=back)
back_button.place(x=605, y=30)

root.mainloop()
