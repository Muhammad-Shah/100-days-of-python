import random
from hang_man_art import stages
from hangman_words import word_list
from turtle import clear

chosen_word = random.choice(word_list)
len_of_chosen_word = len(chosen_word)
lives = 6
# print(f"Chosen Word: {chosen_word}")

display = []
# Create Blanks
for i in range(len_of_chosen_word):
    display += "_"     # display.append("_")
print(display)

end_of_game = False
while not end_of_game:
    guess_letter = input("Guess a Letter: ").lower()

    clear()

    if guess_letter in display:
        print(f"You Already Guessed '{guess_letter}'")

    for position in range(len_of_chosen_word):
        letter = chosen_word[position]
        if letter == guess_letter:
            display[position] = letter
    if guess_letter not in chosen_word:
        lives -= 1
        print(f"Guessed letter '{guess_letter}', is not in the chosen word, you lose a life")
        if lives == 0:
            end_of_game = True
            print("You Lose")
    # Join all the elements in the list and turn into a String
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You Win")
    print(stages[lives])