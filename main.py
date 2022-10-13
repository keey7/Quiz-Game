from data import question_data
from question_model import Question
from quiz_brain import QuizzBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank[0].text)
quizz = QuizzBrain(question_bank)
quizz.next_question()
while quizz.still_has_questions():
       quizz.next_question()


print(f"You've completed the quiz. \nYour final score was: {quizz.score}/{quizz.question_number}")



