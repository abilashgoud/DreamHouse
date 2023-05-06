from tkinter import *
import os

root = Tk()
root.title = ("Registration")
root.geometry('720x460')
window = Canvas(root, width=770, height=430, bg="#5dd9c1")
img = PhotoImage(file="construction-illustration-city-skyline.png")
resize_img = img.subsample(5)
image_label = Label(window, image=img).place(x=0, y=0)
window.pack()


def move_to_client_registration():
    root.destroy()
    os.system("python ClientRegistration.py")


def move_to_owner_registration():
    root.destroy()
    os.system("python OwnerRegistration.py")


def move_to_staff():
    root.destroy()
    os.system("python Staff.py")


def move_to_main():
    root.destroy()
    os.system("python main.py")


title_label = Label(window, text="DreamHome - Register", font=(
    "Arial", 30, "bold"), fg="#36453b")
title_label.place(x=170, y=100)

home = Button(root, text="Go Back To Home", bg="#36453B", fg="#ACFCD9",
              height="1", width=15, font=("Arial", 12), command=move_to_main).place(x=550, y=10)

clientRegistration = Button(root, text="Client Registration", bg="#36453B", fg="#ACFCD9",
                            height="2", width=20, font=("Arial", 12), command=move_to_client_registration).place(x=75, y=280)

ownerRegistration = Button(root, text="Owner Registration", bg="#36453B", fg="#ACFCD9",
                           height="2", width=20, font=("Arial", 12), command=move_to_owner_registration).place(x=275, y=280)

staff = Button(root, text="Staff", bg="#36453B", fg="#ACFCD9",
               height="2", width=20, font=("Arial", 12), command=move_to_staff).place(x=475, y=280)

window.mainloop()
