from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
import os,requests,json,html

term_size = os.get_terminal_size()

print('=' * term_size.columns)

## Get the quiz length/diff set up 

def choose_difficulty():
    level =  input('''Choose your difficulty! easy (e), medium (m), or hard (h): ''')
    if level[0].lower() == "e":
        return "easy"
    elif level[0].lower() == "m":
        return "medium"
    elif level[0].lower() == "h":
        return "hard"
    else: 
        print("Sorry, option not recognized! Bye.")
        quit()

def choose_length(): 
    length = input('''Choose your quiz length! 
Short (s) = 6 questions
Medium (m) = 9 questions
Long (l) = 12 questions: ''')
    if length[0].lower() == "s":
        return 6
    elif length[0].lower() == "m":
        return 9
    elif length[0].lower() == "l":
        return 12
    else: 
        print("Sorry, option not recognized! Bye.")
        quit()

level = choose_difficulty()
length = choose_length()


# Get the list of questions
response = requests.get(f"https://opentdb.com/api.php?amount={length}&difficulty={level}&type=boolean")

# print(response.json()) 

## Construct the question bank 
question_bank = [Question(q["question"], q["correct_answer"]) for q in response.json()["results"]]

# num = 0
# for question in question_bank:
#     num += 1
#     print(html.unescape(f"Q{num}:{question.text}"))

quiz = QuizBrain(question_bank)
      
print('=' * term_size.columns)

while quiz.questions_left(length): 
    quiz.next_question()

print(f"Your final score was {quiz.score}/{quiz.question_number}")