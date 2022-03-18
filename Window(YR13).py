from tkinter import *

root = Tk()

# Changing the title of the window
# root.title("My first window")

# Window, .geometry - to set size of 500px wide x 200px tall
# root.geometry("600x200")
# root.maxsize(1200, 400)

# greeting = Label(text="Hello, Tkinter")

# greeting.pack()
root.title("Excercise 1")
computer = Label(root, bg="Lime", fg="White", text="Computer",
                 font=("Italic", 50, "bold"))

computer.pack()

science = Label(root, bg="Royal Blue", fg="Yellow", text="Science is",
                font=("Comic sans", 50, "bold"))

science.pack()

awesome = Label(root, bg="Orange", fg="Red", text="awesome!",
                font=("Comic sans", 50, "bold"))

awesome.pack()

root.mainloop()
