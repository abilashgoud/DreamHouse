from tkinter import *
import os

root = Tk()
root.title = ("Staff")
root.geometry('720x460')
window = Canvas(root, width=770, height=430, bg="#5dd9c1")
img = PhotoImage(file="construction-illustration-city-skyline.png")
resize_img = img.subsample(5)
image_label = Label(window, image=img).place(x=0, y=0)
window.pack()


def move_to_staff_registration():
    root.destroy()
    os.system("python StaffRegistration.py")


def move_to_staff_listing():
    root.destroy()
    os.system("python StaffListing.py")


def move_to_main():
    root.destroy()
    os.system("python main.py")


title_label = Label(window, text="DreamHome - Staff", font=(
    "Arial", 30, "bold"), fg="#36453b")
title_label.place(x=170, y=100)

home = Button(root, text="Go Back To Home", bg="#36453B", fg="#ACFCD9",
              height="1", width=15, font=("Arial", 12), command=move_to_main).place(x=550, y=10)

staffRegistration = Button(root, text="Staff Registration", bg="#36453B", fg="#ACFCD9",
                           height="2", width=20, font=("Arial", 12), command=move_to_staff_registration).place(x=100, y=280)

staffListing = Button(root, text="Staff Listing", bg="#36453B", fg="#ACFCD9",
                      height="2", width=20, font=("Arial", 12), command=move_to_staff_listing).place(x=400, y=280)


window.mainloop()
