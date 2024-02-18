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
user_input = int(input("What do you choose? Press 0 for rock, 1 for paper and 2 for scissors?\n"))
computer_pick = random.randint(0, user_input)
list = [rock, paper, scissors]
print(f"You chose: \n{list[user_input]}")
print(f"You chose: \n{list[computer_pick]}")
#rock wins scissors
#paper wins rock
#scissors win paper
#Press 0 for rock, 1 for paper and 2 for scissors
if user_input == 0 and computer_pick == 0:
    print("It's a draw")
elif user_input == 0 and computer_pick == 1:
    print("You lose")
elif user_input == 0 and computer_pick == 2:
    print("You win")
elif user_input == 1 and computer_pick == 0:
    print("You win")
elif user_input == 1 and computer_pick == 1:
    print("It's a draw")
elif user_input == 1 and computer_pick == 2:
    print("You lose")
elif user_input == 2 and computer_pick == 0:
    print("You lose")
elif user_input == 2 and computer_pick == 1:
    print("You win")
elif user_input == 2 and computer_pick == 2:
    print("It's a draw")
