from tkinter import *


def say_hi():
    Label(root, bg="yellow", fg="red", text="Hi User!",
          font=("Times", 50, "bold")).pack()


root = Tk()
root.title("My first button")
root.minsize(200, 100)  # Int variable sets the number of pixels for sizing

# Creating a button object - with call to the function
button1 = Button(root, text="Say hi!", command=say_hi)
button1.pack()

root.mainloop()
