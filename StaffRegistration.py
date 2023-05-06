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
root.title("Staff Registration")
root.geometry('760x460')
root.configure(bg="#5dd9c1")


def back():
    root.destroy()
    os.system("python Staff.py")


def func_root():
    staff_number = staff_number_entry.get()
    full_name = full_name_entry.get()
    sex = sex_entry.get()
    dob = dob_entry.get()
    position = position_entry.get()
    salary = salary_entry.get()
    branch_number = branch_number_entry.get()
    supervisor_name = supervisor_name_entry.get()
    manager_start = manager_start_entry.get()
    sql = "INSERT INTO staff VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    val = (staff_number, full_name, position, supervisor_name, sex, dob,  salary,
           branch_number, manager_start,)
    if manager_start is None:
        manager_start = None
    if supervisor_name is None:
        supervisor_name = None
    cursor.execute(sql, val)
    db.commit()
    success_label = tk.Label(root, text="Success")
    success_label.place(x=330, y=400)


staff_onboarding_head_label = Label(root, text="Staff registration Form", font=(
    "Arial", 20, "bold"), bg="#5DD9C1", fg="#36453b")
staff_onboarding_head_label.place(x=255, y=15)

staff_number_label = Label(root, text="Staff Number", bg="#5DD9C1",
                           fg="#36453B", font=("Arial", 13)).place(x=40, y=80)
full_name_label = Label(root, text="Full Name", bg="#5DD9C1",
                        fg="#36453b", font=("Arial", 13)).place(x=40, y=120)
sex_label = Label(root, text="Sex", bg="#5DD9C1", fg="#36453b",
                  font=("Arial", 13)).place(x=40, y=160)
dob_label = Label(root, text="DOB", bg="#5DD9C1", fg="#36453b",
                  font=("Arial", 13)).place(x=165, y=160)

position_label = Label(root, text="Position", bg="#5DD9C1",
                       fg="#36453b", font=("Arial", 13)).place(x=380, y=120)
salary_label = Label(root, text="Salary", bg="#5DD9C1",
                     fg="#36453b", font=("Arial", 13)).place(x=380, y=160)

enter_details_label = Label(root, text="Enter details where applicable",
                            bg="#5DD9C1", fg="#36453b", font=("Arial", 14)).place(x=40, y=280)
supervisor_name_label = Label(root, text="Supervisor No",
                              bg="#5DD9C1", fg="#36453b", font=("Arial", 13)).place(x=40, y=325)
manager_start_date_label = Label(
    root, text="Manager Start Date", bg="#5DD9C1", fg="#36453b", font=("Arial", 13)).place(x=380, y=325)

branch_number_label = Label(root, text="Branch Number", bg="#5DD9C1",
                            fg="#36453b", font=("Arial", 13)).place(x=380, y=80)

staff_number_entry = Entry(root, width=30)
staff_number_entry.place(x=160, y=82)

full_name_entry = Entry(root, width=30)
full_name_entry.place(x=160, y=122)

sex_entry = Entry(root, width=3)
sex_entry.place(x=80, y=162)

dob_entry = Entry(root, width=20)
dob_entry.place(x=220, y=162)

position_entry = Entry(root, width=30)
position_entry.place(x=550, y=122)

salary_entry = Entry(root, width=30)
salary_entry.place(x=550, y=162)

branch_number_entry = Entry(root, width=30)
branch_number_entry.place(x=550, y=82)

supervisor_name_entry = Entry(root, text=None, width=25)
supervisor_name_entry.place(x=190, y=327)

manager_start_entry = Entry(root, text=None, width=30)
manager_start_entry.place(x=550, y=327)

submit_but = Button(root, text="Submit", width=10, bg="#ACFCD9", fg="#36453B", font=(
    "Arial", 12), command=func_root).place(x=60, y=400)
back = Button(root, text="Back", width=10, bg="#ACFCD9", fg="#36453B",
              font=("Arial", 12), command=back).place(x=600, y=400)

root.mainloop()
