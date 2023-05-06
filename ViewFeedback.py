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
root.title("View Comments")
root.geometry('970x500')
root.configure(bg="#5dd9c1")


def go_back():
    root.destroy()
    os.system("python PropertyViewing.py")


def populate_table():
    cursor = db.cursor()
    property_no = property_no_entry.get()
    sql = "select * from viewing where propertyNo=%s"
    val = (property_no,)
    cursor.execute(sql, val)
    rows = cursor.fetchall()
    for data in rows:
        table.insert('', 'end', values=data)
    db.commit()


property_head_label = Label(root, text="View Feedback", font=(
    "Arial", 20, "bold"), bg="#5DD9C1", fg="#36453b")
property_head_label.pack(side=TOP, pady=20)

property_no_label = Label(root, text="Property No",
                          bg="#5DD9C1", fg="#36453b", font=("Arial", 13))
property_no_label.place(x=105, y=120)

property_no_entry = Entry(root, width=30)
property_no_entry.place(x=205, y=122)

# Create the ttk.Treeview widget
table = ttk.Treeview(root, columns=(
    'Client Number', 'Property Number', 'Date', 'Comment'), show='headings')
table.heading('Client Number', text='Client Number')
table.heading('Property Number', text='Property Number')
table.heading('Date', text='Date')
table.heading('Comment', text='Comment')

# Insert sample data into the ttk.Treeview widget

table.place(x=75, y=200)

submit_but = Button(root, text="Submit", width=10, bg="#36453b",
                    fg="white", font=("Arial", 12), command=populate_table)
submit_but.place(x=700, y=120)


back_button = Button(root, text="Back", width=10, bg="#36453b",
                     fg="white", font=("Arial", 12), command=go_back)
back_button.pack(side=BOTTOM, pady=20)

root.mainloop()
