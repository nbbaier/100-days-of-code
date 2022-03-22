import random 
import os
term_size = os.get_terminal_size()


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    
    def questions_left(self):
        return self.question_number < len(self.question_list)
    
    def choose_length(self): 
        length = input("Short (s), medium (m) or long (l) quiz? ")
        if length[0].lower() == "s":
            return 6
        elif length[0].lower() == "m":
            return 9
        elif length[0].lower() == "l":
            return 12
        else: 
            print("Sorry, option not recognized!")
            quit()
            
    
    def randomize_questions(self, length):
        current_list = random.sample(self.question_list, length)  
        return current_list
    
    def next_question(self, current_list):
        current_question = current_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        # print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print('=' * term_size.columns)