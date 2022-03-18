# 09 label side pack.py

from tkinter import *

root = Tk()

root.title("Excercise 1")

computer = Label(root, bg="lime", fg="white", text="Computer",
                 font=("Times", 50, "italic"))
computer.pack(fill=Y, side=LEFT)

science = Label(root, bg="blue", fg="yellow", text="Science is",
                font=("Comic sans MS", 50, "bold"))
science.pack(fill=Y, side=RIGHT)

awesome = Label(root, bg="orange", fg="red", text="Awesome",
                font=("Arial black", 50))
awesome.pack()

root.mainloop()
