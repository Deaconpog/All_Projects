# 08_label stack2.py

from tkinter import *

root = Tk()

root.title("Excercise 1")

computer = Label(root, bg="lime", fg="white", text="Computer",
                 font=("Times", 50, "italic"))
computer.pack(fill=X)

science = Label(root, bg="blue", fg="yellow", text="Science is",
                font=("Comic sans MS", 50, "bold"))
science.pack(fill=X)

awesome = Label(root, bg="orange", fg="red", text="Awesome",
                font=("Arial black", 50))
awesome.pack(fill=X)

root.mainloop()
