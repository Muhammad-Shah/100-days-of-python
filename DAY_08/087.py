# Ceaser Cipher Starting
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alpabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def ceaser(start_text, shift_amount, direction):
    next_text = ""
    if direction == "decode":
            shift_amount *= -1
    for letter in start_text:

        if letter in alpabets:
            position = alpabets.index(letter)    
            new_position = position + shift_amount
            new_letter = alpabets[new_position]   
            next_text += new_letter
        # TO DO_3 -What happens if the user input a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded /decoded?
        # e.g start_text = "meet me at 3"
        # end_text = ".... .. .. ."
        else:
            next_text += letter
    print(f"the {direction}d text is:> {next_text}")

# TO DO_1 -Import and print the logo from art.py when the program starts
print(logo)
# TO DO_4 - Can you figure out a way to ask the user if they want to restart the ceasr cipher program
# type yes if you want to go again, otherwise no
# If they type yes then ask them for direction/text/shift again and call the ceaser() function again?
# Try creating a new function that calls itself if they type yes

# Method : 1
# def repeatCipher():
#     direction = input("Type 'encode' to encript and 'decode' to decript:> ")
#     text = input("Type your message:> ").lower()
#     shift = int(input("Type the shift number:> "))

#     #  TO DO_2 -What if the user enter shift that is greater than the number of letters in the alpabets
#     # Try running the program and entering shift number of (45)
#     # Think about how you can use moduls (%)

#     shift = shift % 26

#     ceaser(start_text=text, shift_amount=shift, direction=direction)

#     repeat_choice = input("Do you want to repeat: ")

#     if repeat_choice == "yes":
#         repeatCipher()
#     else:
#         print("Good by!")
#         exit() 

# repeatCipher()

# Method : 2
is_continue = True
while is_continue:
    direction = input("Type 'encode' to encript and 'decode' to decript:> ")
    text = input("Type your message:> ").lower()
    shift = int(input("Type the shift number:> "))

    #  TO DO_2 -What if the user enter shift that is greater than the number of letters in the alpabets
    # Try running the program and entering shift number of (45)
    # Think about how you can use moduls (%)

    shift = shift % 26

    ceaser(start_text=text, shift_amount=shift, direction=direction)

    repeat_choice = input("Type 'yes' if you want to go again. Otherwise 'no'.:> ")

    if repeat_choice == "no":
        is_continue = False
        print("Good by!")
