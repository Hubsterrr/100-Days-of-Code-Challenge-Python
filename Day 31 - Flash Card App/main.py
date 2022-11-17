from tkinter import *
from tkinter import messagebox
import random
import pandas as pd


global current_card
BACKGROUND_COLOR = "#B1DDC6"


try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")


def random_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    if len(to_learn) <= 0:
        messagebox.showinfo(message="You have learned all the words!")
        window.destroy()
    else:
        current_card = random.choice(to_learn)
        # French side
        french = current_card["French"]
        canvas.itemconfig(card_image, image=card_front)
        canvas.itemconfig(language_text, fill="black", text="French")
        canvas.itemconfig(answer_text, fill="black", text=french)
        window.after(3000, flip_card)


def flip_card():
    english = current_card["English"]
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(language_text, fill="white", text="English")
    canvas.itemconfig(answer_text, fill="white", text=english)


def card_learned():
    to_learn.remove(current_card)
    words_to_learn = pd.DataFrame(to_learn)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    random_card()


# ---------------------------- UI SETUP ------------------------------- #

# Window setup
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Canvas setup (Card)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)
language_text = canvas.create_text(400, 150, text="Language", fill="black", font=("Ariel", 40, "italic"))
answer_text = canvas.create_text(400, 263, text="Answer", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Wrong button
cross_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=cross_image, highlightbackground=BACKGROUND_COLOR, command=random_card)
wrong.grid(column=0, row=1)

# Correct button
tick_image = PhotoImage(file="images/right.png")
correct = Button(image=tick_image, highlightbackground=BACKGROUND_COLOR, command=card_learned)
correct.grid(column=1, row=1)

random_card()

window.mainloop()
