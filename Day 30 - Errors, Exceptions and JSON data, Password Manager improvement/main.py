from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
FONT_NAME = "Courier"

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("saved_password.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showerror(message="No details for the website exists")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = [choice(letters) for _ in range(randint(5, 15))]
    password += [choice(numbers) for _ in range(randint(3, 5))]
    password += [choice(symbols) for _ in range(randint(2, 6))]

    shuffle(password)
    password_entry.delete(0, END)
    password_entry.insert(END, "".join(password))
    pyperclip.copy("".join(password))

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 and len(password) == 0:
        messagebox.showerror(message="Please do not leave fields empty!")
    else:
        try:
            with open("saved_password.json", mode="r") as file:
                #read old data
                data = json.load(file)
        except FileNotFoundError:
            with open("saved_password.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # update old dat with new data
            data.update(new_data)

            with open("saved_password.json", mode="w") as file:
                # save updated data
                json.dump(data, file, indent=4)
        finally:
            password_entry.delete(0, END)
            website_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Window setup
window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=70)

# Canvas setup
canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(75, 100, image=image)
canvas.grid(column=1, row=0)


# Website label
website_label = Label(text="Website:", font=(FONT_NAME, 20, 'bold'))
website_label.grid(column=0, row=1, )

# Website entry box
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1, pady=5)

# Search button
generate_pass = Button(text="Search", width=11, command=find_password)
generate_pass.grid(sticky=W, column=2, row=1)


# Email/ Username label
email_label = Label(text="Email/Username:", font=(FONT_NAME, 20, 'bold'))
email_label.grid(column=0, row=2)

# Email/ Username entry box
email_entry = Entry(width=36)
email_entry.insert(END, string="hubert.luszczyszyn@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, pady=5)


# Password label
password_label = Label(text="Password:", font=(FONT_NAME, 20, 'bold'))
password_label.grid(column=0, row=3)

# Password entry box
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, pady=5)

# Password button
generate_pass = Button(text="Generate Password", width=11, command=generate_password)
generate_pass.grid(sticky=W, column=2, row=3)


# Add button
add = Button(text="ADD", width=34, command=save_data)
add.grid(column=1, row=4, columnspan=2, pady=5)

window.mainloop()
