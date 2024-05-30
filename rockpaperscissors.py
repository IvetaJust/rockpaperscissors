import random
import time

# Asking the user for their choice and validating the input
def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return user_choice

# Randomly selecting the computer's choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

#  Determining the winner of the round
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Visual display of computer's choice
def display_choice(choice):
    choices_art = {
        "rock": """
            ROCK
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """,
        "paper": """
            PAPER
            _______
        ---'   ____)____
                  ______)
                  _______)
                 _______)
        ---.__________)
        """,
        "scissors": """
            SCISSORS
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """
    }
    print(choices_art[choice])

# Counting down from 3 to 1 before showing the computer's choice
def countdown():
    print("Counting down from 3 ...")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    print("SHOOT!")

# Playing a single round of the game
def play_round():
    user_choice = get_user_choice()
    countdown()
    computer_choice = get_computer_choice()
    print("\nYou chose:")
    display_choice(user_choice)
    print("Computer chose:")
    display_choice(computer_choice)
    winner = determine_winner(user_choice, computer_choice)
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win this round!")
    else:
        print("Computer wins this round!")
    return winner

# Playing the game until one player wins two non-tie rounds
def play_game():
    user_score = 0
    computer_score = 0
    non_tie_rounds = 0
    while non_tie_rounds < 3:
        winner = play_round()
        if winner == "user":
            user_score += 1
            non_tie_rounds += 1
        elif winner == "computer":
            computer_score += 1
            non_tie_rounds += 1
        print(f"Score -> You: {user_score} | Computer: {computer_score}\n")
    if user_score > computer_score:
        print("Game ended, you are the winner!")
    elif computer_score > user_score:
        print("Game ended, computer is the winner!")
    else:
        print("Game ended in a tie!")
    input("Press Enter to play again...")

# Running the game in an infinite loop, allowing continuous play
if __name__ == "__main__":
    while True:
        play_game()
