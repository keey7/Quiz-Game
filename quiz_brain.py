class QuizzBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # crear un nuevo metodo de este objeto
    def still_has_questions(self):
        if self.question_number < len(self.question_list):  #return self...
            return True
        else:
            return False

    # crear un nuevo metodo de este objeto
    def next_question(self):
        # Sumar de uno en uno Q1, Q2, Q3 with currentQues
        current_question = self.question_list[self.question_number]  # =0, =1..
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False):")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You're right")
        else:
            print("Sorry that's wrong")
# print(f"The correct answer was: {correct_answer} \n Your current score is: {self.score}/{self.question_number}")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number} \n")


