import random
paper ='''
  _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
'''
rock = '''
("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
'''
scissors ='''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
'''
user_choice = input("What do you choose? Type Rock, Paper, Scissors.\n")
possible_action = [rock, paper, scissors]
computer_choice = random.choice(possible_action)
print(f"Computer choose {computer_choice}")
if user_choice == computer_choice:
    print(f"Both players selected {user_choice}. It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
