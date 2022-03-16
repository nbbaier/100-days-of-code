
import random

## Set the target number

## Set the diffulculty 
def set_dif():
  choice = input("Choose a difficulty. Type 'easy' or 'hard':  ")
  if choice == "easy":
    return 10
  elif choice == "hard":
    return 5

## Compare the target to the guess
def compare(guess, answer, turns):
  if answer > guess:
    print('Too low. Guess again.')
    return turns - 1
  elif answer < guess:
    print('Too high. Guess again.')
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}")

def game():
  print("Guess the number!")
  answer = random.randint(1,100)
  #print(f"the number is {answer}")

  turns = set_dif()
  print(f"You have {turns} attempts remaining to guess the number.")
  
  guess = 0
  while guess != answer:
    guess = int(input('Make a guess: '))
    turns = compare(guess, answer, turns)
    if turns == None:
      break 
    elif turns == 0:
      print("You lose :(")
    else:
      print(f"You have {turns} attempts remaining to guess the number.")
      continue


    
game()


