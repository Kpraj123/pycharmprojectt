logo = """
  _   _                 _                                           _                 
 | \ | |               | |                                         (_)                
 |  \| |_   _ _ __ ___ | |__   ___ _ __    __ _ _   _  ___  ___ ___ _ _ __   __ _     
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|  / _` | | | |/ _ \/ __/ __| | '_ \ / _` |    
 | |\  | |_| | | | | | | |_) |  __/ |    | (_| | |_| |  __/\__ \__ \ | | | | (_| |_ _ 
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \__, |\__,_|\___||___/___/_|_| |_|\__, (_|_)
                                           __/ |                             __/ |    
                                          |___/                             |___/     
"""
print(logo)
print("Welcome To THe NUmber Guessing game!!!!")
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_ans(guess,answer):
    if guess > answer:
        print("To high")
    elif guess < answer:
        print("Too low")
    else:
        print(f"YOu got it right!! The answer is : {answer}")        

# defining a function to set dificulty

def set_dificulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return  HARD_LEVEL_TURNS    
        
# Choosing a random number between 1 and 100
print("I'm thinking of a number between 1 and 100.")
answer = randint(1,100)
print(f"ssst the answer is {answer}")


# Let the user make guesses
turns = set_dificulty()
print(f"You have {turns} attempts remaining to guess the number")
guess = int(input("Make a guess"))


# Function to check the users guess against actual answer





# track the users number of guesses

# Repear the quessionaly functionally if they get it wrong

