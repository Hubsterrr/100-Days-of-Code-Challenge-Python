from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00", fill="white")
    timer_label.config(text="TIMER", fg=GREEN, bg=YELLOW)
    window.config(bg=YELLOW)
    tick_label.config(fg=GREEN, bg=YELLOW)
    canvas.config(bg=YELLOW)
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timer_label.config(text="BREAK", fg=GREEN, bg=RED)
        window.config(bg=RED)
        tick_label.config(fg=GREEN, bg=RED)
        canvas.config(bg=RED)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="BREAK", fg=GREEN, bg=PINK)
        window.config(bg=PINK)
        tick_label.config(fg=GREEN, bg=PINK)
        canvas.config(bg=PINK)
        countdown(short_break_sec)
    else:
        timer_label.config(text="WORK", fg=YELLOW, bg=GREEN)
        window.config(bg=GREEN)
        tick_label.config(fg=YELLOW, bg=GREEN)
        canvas.config(bg=GREEN)
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global reps
    count_min = int(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps == 2:
            tick_label.config(text='✔')
        elif reps == 4:
            tick_label.config(text='✔ ✔')
        elif reps == 6:
            tick_label.config(text='✔ ✔ ✔')


# ---------------------------- UI SETUP ------------------------------- #
# window setup
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=20, bg=YELLOW)

# Start Button
start_button = Button(text="START", width=5, bd=0, fg="black", command=start_timer, font=FONT_NAME, height=2, )
start_button.grid(column=0, row=2)

# Timer Label
timer_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 60, 'bold'))
timer_label.grid(column=1, row=0)

# Tomato
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Tick Label
tick_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, 'bold'))
tick_label.grid(column=1, row=3)

# Reset Button
reset_button = Button(text="RESET", width=5, bd=0, fg="black", command=reset_timer, font=FONT_NAME, height=2, )
reset_button.grid(column=2, row=2)

window.mainloop()
