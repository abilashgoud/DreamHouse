from tkinter import *
import tkinter as tk
import os
from PIL import Image, ImageTk

root = tk.Tk()
root.title = ("Main")
root.geometry('720x460')


window = Canvas(root, width=720, height=460, bg="#5DD9C1")
img = PhotoImage(file="construction-illustration-city-skyline.png")
resize_img = img.subsample(5)
image_label = Label(window, image=img).place(x=0, y=0)
window.pack()


def move_to_registration():
    root.destroy()
    os.system("python registration.py")


def move_to_property():
    root.destroy()
    os.system("python property.py")


title_label = Label(window, text="DreamHome", font=(
    "Arial", 30, "bold"), fg="#36453b")
title_label.place(x=250, y=100)

registration = tk.Button(root, text="Register", bg="#36453B", fg="#ACFCD9",
                         height="2", width=20, font=("Arial", 12), command=move_to_registration).place(x=100, y=280)

property = tk.Button(root, text="Property", bg="#36453B", fg="#ACFCD9",
                     height="2", width=20, font=("Arial", 12), command=move_to_property).place(x=400, y=280)


window.mainloop()
