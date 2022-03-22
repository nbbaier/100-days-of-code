import os,html
term_size = os.get_terminal_size()


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    
    def questions_left(self, length):
        return self.question_number < length 
    
    # def randomize_questions(self, length):
    #     current_list = random.sample(self.question_list, length)  
    #     return current_list
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(html.unescape(f"Q.{self.question_number}: {current_question.text} (T/F): "))
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer[0].lower() == correct_answer[0].lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        # print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print('=' * term_size.columns)