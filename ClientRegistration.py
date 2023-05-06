from tkinter import *
import os
import tkinter as tk
import mysql.connector
from datetime import date

db = mysql.connector.Connect(
    host='localhost',
    user='root',
    # password=password,
    database='dreamhome'
)

cursor = db.cursor()

root = Tk()
root.title("Client Registration")
root.geometry('720x460')

window = Canvas(root, width=720, height=460, bg="#5DD9C1")
window.pack()


def back():
    root.destroy()
    os.system("python registration.py")


def func_window():
    clientNo = clientNo_entry.get()
    fName = fName_entry.get()
    property_prefType = prefType_entry.get()
    maxRent = maxRent_entry.get()
    branchNo = branchNo_entry.get()
    staffNo = staffNo_entry.get()
    regDate = regDate_entry.get()

    sql = "insert into client values (%s, %s, %s, %s, %s, %s, %s)"
    val = (clientNo, fName, property_prefType,
           maxRent, branchNo, staffNo, regDate)
    cursor.execute(sql, val)
    success_label = tk.Label(root, text="Success")
    success_label.place(x=330, y=352)
    db.commit()


client_registration_heading_label = Label(window, text="CLIENT REGISTRATION FORM", font=(
    "Arial", 20, "bold"), bg="#5DD9C1", fg="#36453B")
client_registration_heading_label.place(x=160, y=20)

clientNo_label = Label(window, text="Client Number : ",
                       bg="#5DD9C1", fg="#36453B", font=("Arial", 13))
clientNo_label.place(x=40, y=100)

fName_label = Label(window, text="Full Name : ",
                    bg="#5DD9C1", fg="#36453B", font=("Arial", 13))
fName_label.place(x=40, y=140)

property_requirements_label = Label(
    window, text="Enter Property Requirements : ", bg="#5DD9C1", fg="#36453B", font=("Arial", 14))
property_requirements_label.place(x=40, y=195)

prefType_label = Label(window, text="prefType : ",
                       bg="#5DD9C1", fg="#36453B", font=("Arial", 13))
prefType_label.place(x=40, y=250)

maxRent_label = Label(window, text="Max Rent : ",
                      bg="#5DD9C1", fg="#36453B", font=("Arial", 13))
maxRent_label .place(x=40, y=290)

branchNo_label = Label(window, text="Branch Number : ",
                       bg="#5DD9C1", fg="#36453B", font=("Arial", 13))
branchNo_label .place(x=390, y=100)

staffNo_label = Label(window, text="Registered By : ",
                      bg="#5DD9C1", fg="#36453B", font=("Arial", 13))
staffNo_label.place(x=390, y=250)

regDate_label = Label(window, text="Date Registered : ",
                      bg="#5DD9C1", fg="#36453B", font=("Arial", 13))
regDate_label.place(x=390, y=290)

clientNo_entry = Entry(window, width=20, bg='white', fg="#36453B")
clientNo_entry.place(x=160, y=102)

fName_entry = Entry(window, width=20, bg='white', fg="#36453B")
fName_entry.place(x=130, y=142)

prefType_entry = Entry(window, width=20, bg='white', fg="#36453B")
prefType_entry.place(x=140, y=252)

maxRent_entry = Entry(window, width=20, bg='white', fg="#36453B")
maxRent_entry.place(x=140, y=292)

branchNo_entry = Entry(window, width=20, bg='white', fg="#36453B")
branchNo_entry.place(x=520, y=102)

staffNo_entry = Entry(window, width=20, bg='white', fg="#36453B")
staffNo_entry.place(x=520, y=252)

today = date.today().strftime("%Y-%m-%d")

regDate_entry = Entry(window)
regDate_entry.insert(0, today)
regDate_entry.place(x=520, y=292)

Button(window, text="Submit", width=12, height=1, bg="#ACFCD9", fg="#36453B", font=("Arial", 13),
       command=func_window).place(x=40, y=352)
Button(window, text="Back", width=9, bg="#ACFCD9", fg="#36453B",
       font=("Arial", 13), command=back).place(x=603, y=352)
window.mainloop()
