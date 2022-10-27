class QuizBrain:

    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").capitalize()
        self.check_answer(user, current_question.answer)

    def check_answer(self, user, answer):
        if user == answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def get_score(self):
        return f"End of questions!! Your final score is: {self.score}/{self.question_number}"




