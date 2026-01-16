#Rock, Paper, Scissors Game
import random

#Variables principales
MOVEMENTS = ['rock', 'paper', 'scissors']
WIN_RULES = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
MAX_ATTEMPTS = 5


print("-----Welcome to Rock, Paper, Scissors Game!-----")

#Function to play a single round

def play_round():
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    
    if user_choice not in MOVEMENTS:
        print("Invalid choice. Please try again.")
        return None
    
    computer_choice = random.choice(MOVEMENTS)
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        return "tie"
    elif WIN_RULES[user_choice] == computer_choice:
        return "user"
    else:
        return "computer"
    
#Main game loop
user_score = 0
computer_score = 0
attempts = 0

while attempts < MAX_ATTEMPTS:
    result = play_round()
    
    if result is None:
        continue
    
    if result == "user":
        user_score += 1
        print("You win this round!")
    elif result == "computer":
        computer_score += 1
        print("Computer wins this round!")
    else:
        print("This round is a tie!")
        
        
    attempts += 1
    print(f"Attempts: {attempts}/{MAX_ATTEMPTS}")

#Final results
print("\n-----Game Over-----")
print(f"Final Scores - You: {user_score}, Computer: {computer_score}")

money = 0

if user_score > computer_score:
    money += 10
    print(f"Congratulations! You won the game and earned ${money}.")
    
elif computer_score > user_score:
    print("Computer won the game. Better luck next time!")
else:
    print("The game ended in a tie! You earn $5 for your effort.")
    money += 5
    
    

