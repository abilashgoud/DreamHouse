from tkinter import *
import os

root = Tk()
root.title = ("Property Viewing")
root.geometry('720x460')
window = Canvas(root, width=720, height=460, bg="#5dd9c1")
img = PhotoImage(file="construction-illustration-city-skyline.png")
resize_img = img.subsample(5)
image_label = Label(window, image=img).place(x=0, y=0)
window.pack()


def move_to_main():
    root.destroy()
    os.system("python main.py")


def move_to_give_feedback():
    root.destroy()
    os.system("python GiveFeedback.py")


def move_to_view_feedback():
    root.destroy()
    os.system("python ViewFeedback.py")


title_label = Label(window, text="DreamHome - Feedback", font=(
    "Arial", 30, "bold"), fg="#36453b")
title_label.place(x=140, y=100)

home = Button(root, text="Go Back To Home", bg="#36453B", fg="#ACFCD9",
              height="1", width=15, font=("Arial", 12), command=move_to_main).place(x=550, y=10)

viewFeedback = Button(root, text="View Feedback", bg="#36453B", fg="#ACFCD9",
                      height="2", width=20, font=("Arial", 12), command=move_to_view_feedback).place(x=100, y=280)

giveFeedback = Button(root, text="Give Feedback", bg="#36453B", fg="#ACFCD9",
                      height="2", width=20, font=("Arial", 12), command=move_to_give_feedback).place(x=400, y=280)

window.mainloop()
