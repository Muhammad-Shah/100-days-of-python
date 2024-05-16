import random
from xml.dom.pulldom import CHARACTERS

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+', ]

print("\nWelcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password:  "))
nr_numbers = int(input("How many numbers would you like in your password:  "))
nr_symbols = int(input("How many symbols would you like in your password:  "))

# EASY LEVEL
# password = ""

# for letter in range(0, nr_letters):
#     password += random.choice(letters)

# for number in range(0, nr_numbers):
#     password += random.choice(numbers)

# for symbol in range(0, nr_symbols):
#     password += random.choice(symbols)
# print(password)


# HARD LEVEL
password_list = []

for letter in range(0, nr_letters):
    password_list.append(random.choice(letters))

for number in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

for symbol in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

print(password_list)     # In Order
random.shuffle(password_list) # Random
print(password_list)

# Convert to string from list
password = ""
for char in password_list:
    password += char 

print(f"\nYour password is: {password}")