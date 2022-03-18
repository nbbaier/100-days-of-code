import random
from game_data import data
from art import logo, vs
import os

def clear():
    os.system('clear')

## Choose two random numbers

def get_answer(a,b):
  if a > b:
    return "A"
  elif a < b:
    return "B"
    
def check_answer(choice, answer):
  if choice.upper() == answer:
    return 1
  else:
    print(f"Wrong! :(")
    return 0



def game():
    ## set the initial score and the variable tracking the previous annswer
    print(logo)
    score = 0
    result = 1 
    ## if this is the first round, generate random integers 
    while result != 0:
        if score == 0:
            account_a = random.choice(data)
            account_b = random.choice(data)
            while  account_a == account_b:
                account_b = random.choice(data)

        ## if this is not the first round, generate random integers 
        else:
            account_a = account_b 
            account_b = random.choice(data)
          
        ## get the information from the data list
        name_a = account_a['name']
        followers_a = account_a['follower_count']
        description_a = account_a['description']
        country_a = account_a['country']
      
        name_b = account_b['name']
        followers_b = account_b['follower_count']
        description_b = account_b['description']
        country_b = account_b['country']

  
        ## compare a and be and store it in answer
        answer = get_answer(followers_a, followers_b)

        ## print options
        print(f"Compare A: {name_a}, a {description_a} from {country_a}")
        print(vs)
        print(f"Against B: {name_b}, a {description_b} from {country_b}")
      
        ## have the player choose
        choice = input("Who has more followers? Type 'A' or 'B': ")
      
        ## check the answer and store it in the result 
        result = check_answer(choice, answer)
        clear()
        print(logo)
    
        ## if the result is right, add to score, print the score and continue, otherwise break
        if result == 1:
            score += 1
            print(f"You're right! Current score: {score}")
        else: 
          print(f"Sorry, that's wrong. Final score: {score}")
          break 
            
game()
