import random

# rock beats scissors
# scissors beats rock
# paper beats rock


def rock_paper_scissors_game():
    choice = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("What is your move? ").lower()
        if user_choice in choice:
            break
        else:
            print("rock, paper, or scissors?")

    rand = random.randint(0, 2)

    print("You choose: " + user_choice)
    print("AI choose: " + choice[rand])

    if user_choice == choice[rand]:
        print("\nYou Tied!")
    else:
        if user_choice == "rock" and choice[rand] == "scissors":
            print("\nYou Win!")
        elif user_choice == "paper" and choice[rand] == "rock":
            print("\nYou Win!")
        elif user_choice == "scissors" and choice[rand] == "paper":
            print("\nYou Win!")
        else:
            print("\nYou Lose!")


print("Rock, Paper, or Scissors?")
rock_paper_scissors_game()
