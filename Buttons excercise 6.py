# 12 counting buttons.py

from tkinter import *


def count_up():
    global number
    number += 1
    print(number)


def count_down():
    global number
    number -= 1
    print(number)


root = Tk()
number = 0
root.title("Counting program")
root.minsize(300, 50)

# Creating button objects
button1 = Button(root, text="Increase by 1", command=count_up())
button1.pack()

button2 = Button(root, text="Decrease by 1", command=count_down())
button2.pack()

root.mainloop()
