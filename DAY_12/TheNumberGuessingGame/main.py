from random import randint
EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(guess, answer, attempts):
    if guess > answer:
        print("Too high")
        return attempts -1
    elif guess < answer:
        print("Too low")
        return attempts -1
    else:
        print(f"You got it! The anser is:  {answer} ")



def set_dificulty():
    level = input("Enter Dificulty level! Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL



def main():
    print("Welcome to the Number Guessing Game.")
    print("I am thinking of a number between 1 and 100")
    answer = randint (1, 100)
    attempts = set_dificulty()
    guess = 0
    while guess != answer:
        print(f"You have {attempts} attempts remaining to guess the number")
        guess = int(input("Make a Guess: "))
        attempts = check_answer(guess, answer, attempts)
        if attempts == 0:
            print("You've run out of guesses, you lose")
            return
        else:
            print("Guess again.")
main()
