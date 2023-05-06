from tkinter import *
import os
import tkinter as tk
import mysql.connector

db = mysql.connector.Connect(
    host='localhost',
    user='root',
    # password=password,
    database='dreamhome'
)

cursor = db.cursor()

root = Tk()
root.title("Owner Registration")
root.geometry('720x460')

window = Canvas(root, width=720, height=460, bg="#5DD9C1")
window.pack()


def back():
    root.destroy()
    os.system("python registration.py")


def func_window():
    ownerNo = ownerNo_entry.get()
    fName = fName_entry.get()
    address = address_entry.get()
    telNo = tel_no_entry.get()
    email = email_entry.get()
    sql = "insert into privateowner values (%s,%s,%s,%s,%s)"
    val = (ownerNo, fName, address, telNo, email)
    cursor.execute(sql, val)
    success_label = tk.Label(root, text="Success")
    success_label.place(x=330, y=352)
    db.commit()


owner_registration_heading_label = Label(window, text="OWNER REGISTRATION FORM", font=(
    "Arial", 20, "bold"), bg="#5DD9C1", fg="#36453B")
owner_registration_heading_label.place(x=160, y=20)

ownerNo_label = Label(window, text="Owner Number : ",
                      bg="#5DD9C1", fg="#36453B", font=("Arial", 13))
ownerNo_label.place(x=40, y=100)

ownerNo_entry = Entry(window, width=20, bg='white', fg="#36453B")
ownerNo_entry.place(x=170, y=102)

fName_label = Label(window, text="Full Name : ",
                    bg="#5DD9C1", fg="#36453B", font=("Arial", 13))
fName_label.place(x=40, y=140)

fName_entry = Entry(window, width=20, bg='white', fg="#36453B")
fName_entry.place(x=170, y=142)

address_label = Label(window, text="Address : ",
                      bg="#5DD9C1", fg="#36453B", font=("Arial", 13))
address_label.place(x=40, y=180)

address_entry = Entry(window, width=20, bg='white', fg="#36453B")
address_entry.place(x=170, y=182)

tel_no_label = Label(window, text="Tel No : ",
                     bg="#5DD9C1", fg="#36453B", font=("Arial", 13))
tel_no_label .place(x=40, y=220)

tel_no_entry = Entry(window, width=20, bg='white', fg="#36453B")
tel_no_entry.place(x=170, y=222)

email_label = Label(window, text="Email : ",
                    bg="#5DD9C1", fg="#36453B", font=("Arial", 13))
email_label .place(x=40, y=260)

email_entry = Entry(window, width=20, bg='white', fg="#36453B")
email_entry.place(x=170, y=262)

Button(window, text="Submit", width=12, height=1, bg="#ACFCD9", fg="#36453B", font=("Arial", 13),
       command=func_window).place(x=40, y=352)
Button(window, text="Back", width=9, bg="#ACFCD9", fg="#36453B",
       font=("Arial", 13), command=back).place(x=603, y=352)

window.mainloop()
