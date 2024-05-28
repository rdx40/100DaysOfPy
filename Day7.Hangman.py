import random

word_list=["ardvark","baboon","camel"]

chosenWord=random.choice(word_list)

wordLength=len(chosenWord)

guess = input("Guess a letter: ").lower()

for letter in chosenWord:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
print(chosenWord)