
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
len_of_chosen_word = len(chosen_word)
# Create a variable called 'lives to keep track of number of lives left
# Set 'lives' to equal 6.
lives = 6
print(f"Chosen Word: {chosen_word}")

display = []
# Create Blanks
for i in range(len_of_chosen_word):
    display += "_"     # display.append("_")
print(display)

end_of_game = False
while not end_of_game:
    guess_letter = input("Guess a Letter: ").lower()
    for position in range(len_of_chosen_word):
        letter = chosen_word[position]
        if letter == guess_letter:
            display[position] = letter 
    # TO DO_2  - If guess_letter is not in the chosen_word the reduce 'lives' by 1
    # If lives goes down to 0 then the game should stop and it prints "you lose"
    if guess_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose")
    if "_" not in display:
        end_of_game = True
        print("You Win")
    # TO DO_3  -Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining
    print(stages[lives])
