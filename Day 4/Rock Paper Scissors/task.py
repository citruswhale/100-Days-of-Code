import random

R = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

P = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

S = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [R, P, S]

user = (input("Choose rock or paper or scissors! "
             "Type 'R' for rock, 'P' for paper and 'S' for scissors: \n"))
comp = random.choice(options)

if(user == 'P'): print("You have chosen paper:\n"+P)
elif (user == 'R'): print("You have chosen rock:\n"+R)
else: print("You have chosen scissors:\n"+S)

if(comp == P): print("Computer has chosen paper:\n"+P)
elif (comp == R): print("Computer has chosen rock:\n"+R)
else: print("Computer has chosen scissors:\n"+S)

if ((user == 'S' and comp == S) or (user == 'P' and comp == P) or (user == 'R' and comp == R)):
    print("It's a tie!!")
elif((user == 'S' and comp == P) or (user == 'P' and comp == R) or (user == 'R' and comp == S)):
    print("You win!!")
else:
    print("Computer wins!!")