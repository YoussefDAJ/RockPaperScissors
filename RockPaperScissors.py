print("Welcome to the Rock, Paper, Scissors game: ")
choice = input("Presse Enter to continue or type (Help) for the rules:").lower()

import random

computer_list = ["rock", "paper", "scissors"]
computer_choice = random.choice(computer_list)

if choice == "help":
    print(
        """****** RULES ******
          \n1) You choose and the computer chooses
          \n2) Rock smashes Scissors --> Rock wins
          \n3) Scissors cut Paper --> Scissors win
          \n4) Paper covers Rock --> Paper wins
          """
    )

choice = input("Enter your choice (Rock, Paper, Scissors): ").lower()

if choice == "paper":
    print(
        """
            \nYou chose: 
          

    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

          
          Paper
          """
    )

    print(f"Computer chose: {computer_choice}")
    if computer_choice == choice:
        print(f"It's tide")
    elif computer_choice == "rock":
        print(f"You win computer choses : {computer_choice}")

    elif computer_choice == "scissors":
        print(f"You lose, computer choses : {computer_choice}")

    else:
        print(f"{choice} is invalide choice")


if choice == "rock":
    print(
        """
            \nYou chose:
         
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

          Rock
          """
    )

    print(f"Computer choses : {computer_choice}")
    if computer_choice == "scissors":
        print(f"You win computer choses : {computer_choice}")
    elif computer_choice == "paper":
        print(f"You lose, computer choses : {computer_choice}")
    elif computer_choice == choice:
        print(f"It's tide")
    else:
        print(f"{choice} is invalide choice")

if choice == "scissors":
    print(
        """
            \nYou chose:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

          Scissors
          """
    )
    print(f"Computer chose: {computer_choice}")
    if computer_choice == "paper":
        print(f"You win computer chose {computer_choice}")
    elif computer_choice == "rock":
        print(f"You lose, computer chose {computer_choice}")
    elif computer_choice == choice:
        print(f"It's tide")
    else:
        print(f"{choice} is invalide choice")
