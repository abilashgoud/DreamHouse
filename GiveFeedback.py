from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
import mysql.connector
from datetime import date
db = mysql.connector.connect(
    host='localhost',
    user='root',
    # password=password,
    database='dreamhome'
)

root = Tk()
root.title("Give Comments")
root.geometry('720x460')
root.configure(bg="#5dd9c1")


def go_back():
    root.destroy()
    os.system("python PropertyViewing.py")


def move_to_view_feedback():
    root.destroy()
    os.system("python ViewFeedback.py")


def insert_into_table():
    cursor = db.cursor()
    client_no = client_no_entry.get()
    property_no = property_no_entry.get()
    view_date = view_date_entry.get()
    feedback = feedback_entry.get()
    sql = "insert into viewing (clientNo, propertyNo, viewDate, comment) values (%s,%s,%s,%s)"
    val = (client_no, property_no, view_date, feedback,)
    cursor.execute(sql, val)
    success_label = tk.Label(root, text="Success!")
    success_label.pack()
    db.commit()


property_head_label = Label(root, text="Give Feedback", font=(
    "Arial", 20, "bold"), bg="#5DD9C1", fg="#36453b")
property_head_label.pack(side=TOP, pady=20)

client_no_label = Label(root, text="Client No",
                        bg="#5DD9C1", fg="#36453b", font=("Arial", 13))
client_no_label.place(x=65, y=120)

client_no_entry = Entry(root, width=30)
client_no_entry.place(x=165, y=122)

property_no_label = Label(root, text="Property No",
                          bg="#5DD9C1", fg="#36453b", font=("Arial", 13))
property_no_label.place(x=65, y=160)

property_no_entry = Entry(root, width=30)
property_no_entry.place(x=165, y=162)

view_date_label = Label(root, text="Visit Date",
                        bg="#5DD9C1", fg="#36453b", font=("Arial", 13))
view_date_label.place(x=65, y=200)

today = date.today().strftime("%Y-%m-%d")

view_date_entry = Entry(root)
view_date_entry.insert(0, today)
view_date_entry.place(x=165, y=202)

feedback_label = Label(root, text="Feedback", bg="#5DD9C1",
                       fg="#36453b", font=("Arial", 13))
feedback_label.place(x=65, y=240)

feedback_entry = Entry(root, width=50)
feedback_entry.place(x=165, y=242)

submit_but = Button(root, text="Submit", width=13, bg="#36453b",
                    fg="white", font=("Arial", 12), command=insert_into_table)
submit_but.place(x=150, y=320)

view_feedback_but = Button(root, text="View Feedback", width=13, bg="#36453b",
                           fg="white", font=("Arial", 12), command=move_to_view_feedback)
view_feedback_but.place(x=450, y=320)


back_button = Button(root, text="Back", width=10, bg="#36453b",
                     fg="white", font=("Arial", 12), command=go_back)
back_button.pack(side=BOTTOM, pady=20)

root.mainloop()
