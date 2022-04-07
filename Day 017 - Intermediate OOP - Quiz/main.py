from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for questions in question_data:
    question_bank.append(Question(questions["question"], questions["correct_answer"]))

new_quiz = QuizBrain(question_bank)
new_quiz.next_question()

while new_quiz.still_has_q():
    new_quiz.next_question()

if new_quiz.question_number == len(question_bank):
    print(f"You have Completed the Quiz!! Your Score is {new_quiz.score}/{new_quiz.question_number}")
