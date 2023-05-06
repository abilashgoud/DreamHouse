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
root.title("Property Registration")
root.geometry('720x460')

window = Canvas(root, width=720, height=460, bg="#5DD9C1")
window.pack()


def back():
    root.destroy()
    os.system("python property.py")


def func_window():
    propertyNo = propertyNo_entry.get()
    property_address = property_address_entry.get()
    property_type = property_type_entry.get()
    property_rent = property_rent_entry.get()
    branch_number = branch_number_entry.get()
    staff_number = staff_number_entry.get()
    city = city_entry.get()
    postcode = postcode_entry.get()
    rooms_req = rooms_req_entry.get()
    owner_number = owner_number_entry.get()

    sql = "INSERT INTO propertyForRent (propertyNo, address, type,rent, branchNo,staffNo,city, postcode, rooms,ownerNo,  currentStatus   ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'Y')"
    val = (propertyNo, property_address, property_type, property_rent, branch_number, staff_number, city,
           postcode, rooms_req, owner_number)
    cursor.execute(sql, val)
    success_label = tk.Label(root, text="Success")
    success_label.place(x=330, y=352)
    db.commit()


client_registration_heading_label = Label(window, text="PROPERTY REGISTRATION FORM", font=(
    "Arial", 20, "bold"), bg="#5DD9C1", fg="#36453B")
client_registration_heading_label.place(x=120, y=20)

property_registration_label = Label(
    window, text="Enter Property Requirements  ", bg="#5DD9C1", fg="#36453B", font=("Arial", 15))
property_registration_label.place(x=80, y=80)

propertyNo_label = Label(window, text="Property Number : ",
                         bg="#5DD9C1", fg="#36453B", font=("Arial", 13))
propertyNo_label.place(x=20, y=120)
propertyNo_entry = Entry(window, width=20, bg="white", fg="#36453B")
propertyNo_entry.place(x=180, y=125)

property_type_label = Label(
    window, text="Property type : ", bg="#5DD9C1", fg="#36453B", font=("Arial", 13))
property_type_label.place(x=20, y=160)
property_type_entry = Entry(window, width=20, bg="white", fg="#36453B")
property_type_entry.place(x=180, y=165)

property_address_label = Label(
    window, text=" Address : ", bg="#5DD9C1", fg="#36453B", font=("Arial", 13))
property_address_label.place(x=20, y=200)
property_address_entry = Entry(window, width=20, bg="white", fg="#36453B")
property_address_entry.place(x=180, y=205)

property_rent_label = Label(
    window, text="Property rent : ", bg="#5DD9C1", fg="#36453B", font=("Arial", 13))
property_rent_label.place(x=20, y=240)
property_rent_entry = Entry(window, width=20, bg="white", fg="#36453B")
property_rent_entry.place(x=180, y=245)

rooms_req_label = Label(window, text="Rooms required : ",
                        bg="#5DD9C1", fg="#36453B", font=("Arial", 13))
rooms_req_label.place(x=20, y=280)
rooms_req_entry = Entry(window, width=20, bg="white", fg="#36453B")
rooms_req_entry.place(x=180, y=285)

postcode_label = Label(window, text="Postcode : ",
                       bg="#5DD9C1", fg="#36453B", font=("Arial", 13))
postcode_label.place(x=20, y=320)
postcode_entry = Entry(window, width=20, bg="white", fg="#36453B")
postcode_entry.place(x=180, y=325)

city_label = Label(window, text="City : ", bg="#5DD9C1",
                   fg="#36453B", font=("Arial", 13))
city_label.place(x=20, y=360)
city_entry = Entry(window, width=20, bg="white", fg="#36453B")
city_entry.place(x=180, y=365)

owner_label = Label(window, text="Owner details  ",
                    bg="#5DD9C1", fg="#36453B", font=("Arial", 15))
owner_label.place(x=450, y=80)

owner_number_label = Label(
    window, text="Owner Number : ", bg="#5DD9C1", fg="#36453B", font=("Arial", 13))
owner_number_label.place(x=360, y=120)
owner_number_entry = Entry(window, width=20, bg="white", fg="#36453B")
owner_number_entry.place(x=495, y=125)

staff_label = Label(window, text="Managed By  ",
                    bg="#5DD9C1", fg="#36453B", font=("Arial", 15))
staff_label.place(x=450, y=175)

staff_number_label = Label(
    window, text="Staff Number : ", bg="#5DD9C1", fg="#36453B", font=("Arial", 13))
staff_number_label.place(x=360, y=215)
staff_number_entry = Entry(window, width=20, bg="white", fg="#36453B")
staff_number_entry.place(x=495, y=220)

registered_label = Label(window, text="Registered at  ",
                         bg="#5DD9C1", fg="#36453B", font=("Arial", 15))
registered_label.place(x=450, y=265)

branch_number_label = Label(
    window, text="Branch Number : ", bg="#5DD9C1", fg="#36453B", font=("Arial", 13))
branch_number_label.place(x=360, y=305)
branch_number_entry = Entry(window, width=20, bg="white", fg="#36453B")
branch_number_entry.place(x=495, y=310)

Button(window, text="Submit", width=15, height=1, bg="#36453B", fg="#ACFCD9", font=("Arial", 13),
       command=func_window).place(x=40, y=410)
Button(window, text="Back", width=9, bg="#36453B", fg="#ACFCD9",
       font=("Arial", 13), command=back).place(x=603, y=410)


window.mainloop()
