import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# Create deal card function that uses the list below to return a random card
# 11 is Ace

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# Create a function called calculate_sum() that takes a List of cards as inputs and return the score
# Look at the sum() function to help you do this 
def calculate_score(cards):
    """takes a list of cards and return score calculated from the cards"""
    # Inside the calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    # if 11 in cards and 10 in cards and len(cards) == 2: 
    if sum(cards) == 21 and len(cards) == 2:
        return 0 

    # Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

    
# Deal user and computer 2 cards each using deal_card()
user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())  

# Call calculate_score(), If the computer or the user has a blackjack {0} or if the user's score is over 21, then the game ends.
# Hint 11: -The score will need to be rechecked with every new card drawn and the checks in the Hint 9 need to be repeated until the game ends. while() loop
while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"  Your cards: {user_cards}, current score: {user_score} ") 
    print(f"  Computer's first card: {computer_cards[0]} ")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    # If the game is not ended ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game is ended
     
    # Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

    # Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_scoreis over 21, then the computer loses. If none of the above, then the player with the highest score wins.


# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py
 
















