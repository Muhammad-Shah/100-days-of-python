# TO DO_1 -Use a while loop to guess the user again. The loop should only stopped once the user has guessed all
# the letters in the choosen word and 'display' has no more blanks ("_"). The you can tell the user they have won
import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
len_of_chosen_word = len(chosen_word)
print(f"Chosen Word: {chosen_word}")

display = []
# Create Blanks
for char in chosen_word:
    display += "_"     # display.append("_")
print(display)

# Method : 1
# i = 0
# while i < len_of_chosen_word:
#     guess_letter = input("Guess a Letter: ").lower()
#     for position in range(len_of_chosen_word):
#         letter = chosen_word[position]
#         if letter == guess_letter:
#             display[position] = letter
#     print(display) 
#     i = i+1

# Method : 2
end_of_game = False
while not end_of_game:
    guess_letter = input("Guess a Letter: ").lower()
    for position in range(len_of_chosen_word):
        letter = chosen_word[position]
        print(f"current position: {position}\ncurrent letter: {letter}\nguessed letter: {guess_letter}")
        if letter == guess_letter:
            display[position] = letter
    if "_" not in display:
        end_of_game = True
    print(display)