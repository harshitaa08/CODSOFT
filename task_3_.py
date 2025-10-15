# Rock, Paper, Scissors Game
# Internship Task 3 - CODSOFT
# Created by: Harshita Shukla

# This is a simple Python game where the user plays Rock, Paper, Scissors
# against the computer. The game keeps track of scores and allows multiple rounds.

import random

def show_menu():
    print("\n========== ROCK PAPER SCISSORS ==========")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("=========================================")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"

# Score tracking
user_score = 0
computer_score = 0

print("Welcome to Rock, Paper, Scissors Game!")

while True:
    show_menu()
    choice = input("Enter your choice (rock/paper/scissors or 'exit' to quit): ").lower()

    if choice == 'exit':
        print("\nThanks for playing!")
        print(f"Final Score - You: {user_score} | Computer: {computer_score}")
        break

    if choice not in ["rock", "paper", "scissors"]:
        print("Invalid input! Please choose rock, paper, or scissors.")
        continue

    computer_choice = get_computer_choice()
    print(f"\nYou chose: {choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(choice, computer_choice)

    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win this round! 🎉")
        user_score += 1
    else:
        print("Computer wins this round! 🤖")
        computer_score += 1

    print(f"Score - You: {user_score} | Computer: {computer_score}")

    play_again = input("\nDo you want to play another round? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing!")
        print(f"Final Score - You: {user_score} | Computer: {computer_score}")
        print("Goodbye! 👋")
        break
