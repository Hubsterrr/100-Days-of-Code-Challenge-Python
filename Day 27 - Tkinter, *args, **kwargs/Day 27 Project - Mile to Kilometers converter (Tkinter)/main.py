from tkinter import *


def calculate():
    input_miles = float(input_box.get())
    kilometers = round(input_miles * 1.61, 2)
    answer.config(text=kilometers)
    return 0


# Create window
window = Tk()
window.title("My first GUI program")
window.minsize(width=400, height=200)
window.config(padx=70, pady=40)

# Label - is equal to
label_is_equal = Label(text="is equal to", font=("Arial", 20))
label_is_equal.grid(column=0, row=1)

# Entry
input_box = Entry(width=10)
input_box.get()
input_box.grid(column=1, row=0)

# Label - answer
answer = Label(text="0", font=("Arial", 20))
answer.grid(column=1, row=1)

# Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

# Label - Miles
miles = Label(text="Miles", font=("Arial", 20))
miles.grid(column=2, row=0)

# Label - Km
km = Label(text="Km", font=("Arial", 20))
km.grid(column=2, row=1)


window.mainloop()
