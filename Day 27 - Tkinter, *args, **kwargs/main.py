from tkinter import *


def button_clicked():
    my_label["text"] = input.get()


# Create window
window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a Label", font=("Arial", 30))
my_label["text"] = "New text"
my_label.grid(column=0, row=0)

# Button
button = Button(text="Naciśń", command=button_clicked)
button.grid(column=1, row=1)

# 2 Button
button2 = Button(text="Naciśń", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.get()
input.grid(column=3, row=2)

window.mainloop()
