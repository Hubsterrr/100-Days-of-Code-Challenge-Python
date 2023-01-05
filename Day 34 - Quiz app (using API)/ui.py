from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "arial"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score label
        self.score = Label(text="0", bg=THEME_COLOR, font=(FONT_NAME, 40, 'bold'))
        self.score.grid(column=1, row=0)

        # Question canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, width=280, text="question", fill=THEME_COLOR, font=(FONT_NAME, 20, "bold"))
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=40)

        # Wrong button
        self.cross_image = PhotoImage(file="images/false.png")
        self.wrong = Button(image=self.cross_image, highlightbackground=THEME_COLOR, command=self.answer_false)
        self.wrong.grid(column=0, row=2)

        # Correct button
        self.tick_image = PhotoImage(file="images/true.png")
        self.correct = Button(image=self.tick_image, highlightbackground=THEME_COLOR, command=self.answer_true)
        self.correct.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
            self.score.config(text=self.quiz.score)
        else:
            self.canvas.itemconfig(self.question, text="You have answered all questions fot this session")
            self.correct.config(state="disabled")
            self.wrong.config(state="disabled")

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)

