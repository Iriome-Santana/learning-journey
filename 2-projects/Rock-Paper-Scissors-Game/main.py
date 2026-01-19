#Rock, Paper, Scissors Game
import random
import os
import json

#Variables principales
MOVEMENTS = ['rock', 'paper', 'scissors']
WIN_RULES = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
MAX_ATTEMPTS = 5
FILE_NAME = "player_data.json"

print("-----Welcome to Rock, Paper, Scissors Game!-----")

"""Function to save progress"""
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        return {"money": 0,
                "plays": 0}
    
"""Function to save data"""
def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)



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
data = load_data()
money = data["money"]
plays = data["plays"]

print(f"You have played {plays} plays")
print(f"You have: {money} money")

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

if attempts == 5:
    plays +=1

if user_score > computer_score:
    money += 10
    print("Congratulations! You won the game and earned $10.")
    
elif computer_score > user_score:
    print("Computer won the game. Better luck next time!")
else:
    print("The game ended in a tie! You earn $5 for your effort.")
    money += 5

data["plays"] = plays
data["money"] = money
save_data(data)

    

