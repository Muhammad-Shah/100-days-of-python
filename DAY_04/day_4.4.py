# Program to check who will pay the bill randomly
import random

names_string = input("Give me Everybody's names, separated by a comma. ")
# convert string to a list using split -> list is names
names = names_string.split(", ")
# to calculate total item(people) in the list starts from 1
# total_items = len(names)

# Method : 1
# specific person in the list is find randomly from 0-total length 
# person_index = random.randint(0, total_items)
# # subtract 1 because 0 is not included in the len() 
# print(f"{names[person_index-1]} is going to buy the meal today!")



# Method : 2
# person_index = random.randint(0, total_items-1)
# who_will_pay = names[person_index]
# print(f"{who_will_pay} is going to buy the meal today!")



# Method : 3
# This method is very easy by using choice() it will pick any random item from the list
who_will_pay = random.choice(names)
print(f"{who_will_pay} is going to buy the meal today!")

