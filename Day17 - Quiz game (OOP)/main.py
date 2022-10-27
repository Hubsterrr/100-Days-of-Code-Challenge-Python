from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    q = question["question"]
    a = question["correct_answer"]
    new_question = Question(text=q, answer=a)
    question_bank.append(new_question)

game = QuizBrain(question_bank)

game.next_question()

while game.still_has_questions():
    game.next_question()
print("You've completed the quiz")
print(f"Your final score was: {game.score}/{len(question_bank)}")


