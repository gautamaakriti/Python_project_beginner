import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("Inavalid start over..")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer choose:")
    print(game_images[computer_choice])

    if user_choice == computer_choice:
        print("Yayyyy!! It's a tie....")
    elif user_choice == 0:
        if computer_choice == 2:
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_choice == 1:
        if computer_choice == 0:
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_choice == 2:
        if computer_choice == 1:
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
