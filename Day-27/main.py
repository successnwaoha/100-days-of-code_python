from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label["text"] = new_text


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column = 0, row = 0)

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column = 1, row = 1)

#New Button
new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column = 2, row = 0)

#Entry
input = Entry(width=10)
input.grid(column = 3, row = 2)


window.mainloop()