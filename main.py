import random
print("\nWelcome to the Rock, Paper, Scissors game:")
if input("Press Enter to continue or type (Help) for the rules ").lower() == "help":
    print("""
            ********* Rules *********
            1) You choose and the computer chooses
            2) Rock smashes Scissors -> Rock wins
            3) Scissors cut Paper -> Scissors win
            4) Paper covers Rock -> Paper wins
            """)

user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

#User choice
if user_choice == "rock":
    print("""You chose:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif user_choice == "paper":
    print("""You chose:
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif user_choice == "scissors":
    print("""You chose:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
else:
    print(f"Your choice ( {user_choice} ) is not in the game!")

#Computer choice
if random.randint(1,3) == 1:
    computer_choice = "rock"
    print("""Computer chose:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif random.randint(1,3) == 2:
    computer_choice = "paper"
    print("""Computer chose:
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
else:
    computer_choice = "scissors"
    print("""Computer chose:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

#Game logic
#Draw
if user_choice == computer_choice:
    print("\nThis is a draw! Try again.\n")
#Win
elif user_choice == "rock" and computer_choice == "scissors":
    print(f"\nYou win!, {user_choice} beats {computer_choice}.\n")
elif user_choice == "paper" and computer_choice == "rock":
    print(f"\nYou win!, {user_choice} beats {computer_choice}.\n")
elif user_choice == "scissors" and computer_choice == "paper":
    print(f"\nYou win!, {user_choice} beats {computer_choice}.\n")
#Lose
elif user_choice == "rock" and computer_choice == "paper":
    print(f"\nYou lose!, {computer_choice} beats {user_choice}.\n")
elif user_choice == "paper" and computer_choice == "scissors":
    print(f"\nYou lose!, {computer_choice} beats {user_choice}.\n")
elif user_choice == "scissors" and computer_choice == "rock":
    print(f"\nYou lose!, {computer_choice} beats {user_choice}.\n")