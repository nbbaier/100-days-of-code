from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
import os#, random 
term_size = os.get_terminal_size()

question_bank = [Question(q["text"], q["answer"]) for q in question_data]

quiz = QuizBrain(question_bank)
      
print('=' * term_size.columns)

length = quiz.choose_length()
the_questions = quiz.randomize_questions(length)

print('=' * term_size.columns)


while quiz.questions_left(): 
    quiz.next_question(the_questions)

print(f"Your final score was {quiz.score}/{quiz.question_number}")