
# TO DO_1  -create an Empty list called display 
# For each letter in the chosen word add a "_" to 'display'
# So if the chosen word was camel ["_", "_", "_", "_", "_"] with 5 "_" with representing each letter to guess word 

# TO DO_2  -loop through each position in the chosen_word
# If the letter at that position matches 'guess_letter' then reveal that letter in the display at that position
# eg: if the user guessed 'm' and the chosen word was 'camel' then display should be ["_", "_", "m", "_", "_"]

# TO DO_3  -print 'display' and you should see the guessed letter at the correct position and every letter replace with "_"
import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"Chosen Word: {chosen_word}")

display = []

for char in chosen_word:
    display += "_"     # display.append("_")
print(display)

guess_letter = input("Guess a Letter: ").lower()

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess_letter:
        display[position] = letter

print(display)
