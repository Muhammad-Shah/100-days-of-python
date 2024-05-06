import random

print("What do you choose type 0 for Rock 1 for Paper or 2 for Scissors.")
user_choice = int(input())

computer_choice = random.randint(0, 2)
print(f"user choice: {user_choice}  & computer chice: {computer_choice}")

if user_choice == computer_choice:
    print("Draw")
elif user_choice >= 3 or user_choice < 0:
    print("Try Again! Inalid number TYPED")
elif user_choice == 1 and computer_choice == 0:
    print("You Win")
elif user_choice == 2 and computer_choice == 1:
    print("You Win")
elif user_choice == 0 and computer_choice == 2:
    print("You Win")
else:
    print("You Lost")