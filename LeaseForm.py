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
root.title("Lease Form")
root.geometry('810x450')

window = Canvas(root, width=810, height=450, bg="#5DD9C1")
window.pack()


def back():
    root.destroy()
    os.system("python property.py")


def func_root():
    client_number = client_number_entry.get()
    branch_number = branch_number_entry.get()
    monthly_rent = monthly_rent_entry.get()
    payment_method = payment_method_entry.get()
    property_number = property_number_entry.get()
    staff_number = staff_number_entry.get()
    rent_start = rent_start_entry.get()
    duration = duration_entry.get()

    sql = "insert into registration values (%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (client_number, property_number, branch_number, staff_number,
           rent_start, duration, monthly_rent, payment_method)
    cursor.execute(sql, val)
    db.commit()
    sql2 = "update propertyForRent set currentStatus='N' where propertyNo=%s"
    val2 = (property_number,)
    cursor.execute(sql2, val2)
    db.commit()
    sql1 = "select r.clientNo,c.fName,r.propertyNo,concat(p.address,', ',p.city) as propertyAddress,r.rentPaid, r.dateJoined,r.rentalPeriod,r.paymentMethod,(select date_add(r.dateJoined,interval r.rentalPeriod month)) as expiryDate from registration r,client c,propertyforrent p where r.clientNo=c.clientNo and p.propertyNo=r.propertyNo and r.clientNo=%s"
    val1 = (client_number,)
    cursor.execute(sql1, val1)

    # Fetch all rows from the query result
    rows = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    db.close()

    # Create a new Tkinter window to display the data
    data_window = tk.Toplevel(root)
    data_window.title("Data")

    # Create a Tkinter Text widget to display the data
    data_text = tk.Text(data_window, font=("Arial", 14),
                        padx=10, pady=10, spacing1=10, spacing2=5)
    data_text.pack()

    # Add some styling to the Text widget
    data_text.tag_configure("title", font=("Arial", 18, "bold"), spacing1=20)
    data_text.tag_configure("label", font=("Arial", 14, "bold"), spacing1=10)
    data_text.tag_configure("value", font=("Arial", 14), spacing1=10)

    # Display the data in the Text widget
    data_text.insert(tk.END, f"Data\n", "title")
    for row in rows:
        data_text.insert(tk.END, "Client ID: ", "label")
        data_text.insert(tk.END, f"{row[0]}\n", "value")
        data_text.insert(tk.END, "Client Name: ", "label")
        data_text.insert(tk.END, f"{row[1]}\n", "value")
        data_text.insert(tk.END, "Property Number: ", "label")
        data_text.insert(tk.END, f"{row[2]}\n", "value")
        data_text.insert(tk.END, "Property Address: ", "label")
        data_text.insert(tk.END, f"{row[3]}\n", "value")
        data_text.insert(tk.END, "Rent Paid: ", "label")
        data_text.insert(tk.END, f"{row[4]}\n", "value")
        data_text.insert(tk.END, "Joining Date: ", "label")
        data_text.insert(tk.END, f"{row[5]}\n", "value")
        data_text.insert(tk.END, "Rental Period: ", "label")
        data_text.insert(tk.END, f"{row[6]}\n", "value")
        data_text.insert(tk.END, "Payment Method: ", "label")
        data_text.insert(tk.END, f"{row[7]}\n", "value")
        data_text.insert(tk.END, "Expiry Date: ", "label")
        data_text.insert(tk.END, f"{row[8]}\n", "value")


lease_form_head_label = Label(root, text="Lease Form", font=(
    "Arial", 20, "bold"), bg="#5dd9c1", fg="#36453b").place(x=310, y=15)

client_number_label = Label(root, text="Client Number", bg="#5dd9c1",
                            fg="#36453b", font=("Arial", 13)).place(x=40, y=80)
branch_number_label = Label(root, text="Branch Number", bg="#5dd9c1",
                            fg="#36453b", font=("Arial", 13)).place(x=40, y=120)

property_number_label = Label(root, text="Property Number",
                              bg="#5dd9c1", fg="#36453b", font=("Arial", 13)).place(x=425, y=80)
staff_number_label = Label(root, text="Staff Number",
                           bg="#5dd9c1", fg="#36453b", font=("Arial", 13)).place(x=425, y=120)

payment_details_label = Label(root, text="Enter payment details",
                              bg="#5dd9c1", fg="#36453b", font=("Arial", 14)).place(x=40, y=180)

monthly_rent_label = Label(root, text="Monthly Rent", bg="#5dd9c1",
                           fg="#36453b", font=("Arial", 13)).place(x=40, y=230)
payment_method_label = Label(root, text="Payment Method", bg="#5dd9c1",
                             fg="#36453b", font=("Arial", 13)).place(x=40, y=270)

rent_start_label = Label(root, text="Rent Start", bg="#5dd9c1",
                         fg="#36453b", font=("Arial", 13)).place(x=455, y=230)
duration_label = Label(root, text="Duration", bg="#5dd9c1",
                       fg="#36453b", font=("Arial", 13)).place(x=455, y=270)

client_number_entry = Entry(root, width=30)
client_number_entry.place(x=165, y=82)

branch_number_entry = Entry(root, width=30)
branch_number_entry.place(x=165, y=122)

monthly_rent_entry = Entry(root, width=25)
monthly_rent_entry.place(x=190, y=232)

payment_method_entry = Entry(root, width=25)
payment_method_entry.place(x=190, y=272)

property_number_entry = Entry(root, width=30)
property_number_entry.place(x=575, y=82)

staff_number_entry = Entry(root, width=30)
staff_number_entry.place(x=575, y=122)

rent_start_entry = Entry(root, width=30)
rent_start_entry.place(x=575, y=232)

duration_entry = Entry(root, width=30)
duration_entry.place(x=575, y=272)

submit_but = Button(root, text="Submit", width=10, bg="#ACFCD9", fg="#36453B", font=(
    "Arial", 12), command=func_root).place(x=41, y=370)
back = Button(root, text="Back", width=10, bg="#ACFCD9", fg="#36453B",
              font=("Arial", 12), command=back).place(x=660, y=370)


window.mainloop()
