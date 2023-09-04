import random


def rock_paper_scissors_game():
    choice = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("What is your move? ").lower()
        if user_choice in choice:
            break



print("Rock, Paper, or Scissors?")
rock_paper_scissors_game()
