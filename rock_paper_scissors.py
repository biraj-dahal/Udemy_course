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
---'    ____)____
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
dict_help = {'0': rock, '1': paper, '2' : scissors}
random_selection = random.choice("012")
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.")
print("Your Choice:\n", dict_help[player_choice])
print("Computer's choice: \n", dict_help[random_selection])
if player_choice == random_selection:
    print("It is a tie.")
elif (player_choice == '0' and random_selection == '2') or (player_choice == '1' and random_selection == '0') or (player_choice == '2' and random_selection == '1'):
    print("You win.")
else:
    print("Computer Wins.")
