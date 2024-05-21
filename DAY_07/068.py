# TO DO_1  -Randomly choose a word from a word list and assign it a variable called chosen_word 
# TO DO_1  -Ask the user to guess a letter and assign their answer to a variable called guess_letter> Make guess_letter lwer case
# TO DO_3  -Check if the letter the user guessed is one of the letter in the chosen_word 

import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

guess_letter = input("Guess a Letter: ").lower()

for word in chosen_word:
    if guess_letter == word:
        print("Right")
    else:
        print("Wrong")