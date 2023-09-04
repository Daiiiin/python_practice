import random


def rock_paper_scissors_game():
    choice = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("What is your move? ").lower()
        if user_choice in choice:
            break
        else:
            print("rock, paper, or scissors?")

    ai_choice = random.choice(choice)

    print("You choose: " + user_choice)
    print("AI choose: " + ai_choice)

    if user_choice == ai_choice:
        print("\nYou Tied!")
    else:
        if user_choice == "rock" and ai_choice == "scissors":
            print("\nYou Win!")
        elif user_choice == "paper" and ai_choice == "rock":
            print("\nYou Win!")
        elif user_choice == "scissors" and ai_choice == "paper":
            print("\nYou Win!")
        else:
            print("\nYou Lose!")


print("Rock, Paper, or Scissors?")
rock_paper_scissors_game()
