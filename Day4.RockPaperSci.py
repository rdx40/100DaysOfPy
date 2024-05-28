import random
Choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
compChoice=random.randint(0,2)
if Choice==0:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    if compChoice==0:
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print("Draw")
    elif compChoice==1:
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("You lose")
    else:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("You win")
elif Choice==1:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    if compChoice==0:
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print("You win")
    elif compChoice==1:
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("Draw")
    else:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("You lose")
else:
    if compChoice==0:
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print("You lose")
    elif compChoice==1:
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("You win")
    else:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("Draw")
