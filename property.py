from tkinter import *
import os

root = Tk()
root.title = ("Property")
root.geometry('720x460')
window = Canvas(root, width=770, height=430, bg="#5dd9c1")
img = PhotoImage(file="construction-illustration-city-skyline.png")
resize_img = img.subsample(5)
image_label = Label(window, image=img).place(x=0, y=0)
window.pack()


def move_to_property_registration():
    root.destroy()
    os.system("python PropertyRegistration.py")


def move_to_show_property():
    root.destroy()
    os.system("python PropertyListing.py")


def move_to_property_viewing():
    root.destroy()
    os.system("python PropertyViewing.py")


def move_to_lease_form():
    root.destroy()
    os.system("python LeaseForm.py")


def move_to_main():
    root.destroy()
    os.system("python main.py")


title_label = Label(window, text="DreamHome - Property", font=(
    "Arial", 30, "bold"), fg="#36453b")
title_label.place(x=140, y=100)

home = Button(root, text="Go Back To Home", bg="#36453B", fg="#ACFCD9",
              height="1", width=15, font=("Arial", 12), command=move_to_main).place(x=550, y=10)

propertyRegistration = Button(root, text="Property Registration", bg="#36453B", fg="#ACFCD9",
                              height="2", width=20, font=("Arial", 12), command=move_to_property_registration).place(x=100, y=240)

showProperty = Button(root, text="Show Properties", bg="#36453B", fg="#ACFCD9",
                      height="2", width=20, font=("Arial", 12), command=move_to_show_property).place(x=400, y=240)

viewing = Button(root, text="Feedback", bg="#36453B", fg="#ACFCD9",
                 height="2", width=20, font=("Arial", 12), command=move_to_property_viewing).place(x=100, y=320)

leaseForm = Button(root, text="Lease Form", bg="#36453B", fg="#ACFCD9",
                   height="2", width=20, font=("Arial", 12), command=move_to_lease_form).place(x=400, y=320)


window.mainloop()
