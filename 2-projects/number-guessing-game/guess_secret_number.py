import random

MAXIMUM = 100
MINIMUM = 1
MAX_ATTEMPTS = 10

attempts = 0
number_to_guess = random.randint(MINIMUM, MAXIMUM)

print("-----Welcome to the Number Guessing Game!-----")

print(f"I'm thinking of a number between {MINIMUM} and {MAXIMUM}.")
print(f"You have {MAX_ATTEMPTS} attempts to guess the correct number.")

while attempts < MAX_ATTEMPTS:
    try:
        user_choice = int(input(f"Choose a number between {MINIMUM} and {MAXIMUM}: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    

    if user_choice < MINIMUM or user_choice > MAXIMUM:
        print("Invalid choice. Please try again.")
        continue

    attempts += 1

    if user_choice == number_to_guess:
        print(f"Congratulations! You guessed the correct number in {attempts} attempts!")
        break
    elif user_choice < number_to_guess:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
    
        
else:
    print("-----Game Over-----")
    print(f"Sorry, you've used all your attempts. The correct number was {number_to_guess}.")