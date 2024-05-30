from art import logo
alpabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(start_text, shift_amount, direction):
    next_text = ""
    if direction == "decode":
            shift_amount *= -1
    for letter in start_text:

        if letter in alpabets:
            position = alpabets.index(letter)    
            new_position = (position + shift_amount)%26
            new_letter = alpabets[new_position]   
            next_text += new_letter
        else:
            next_text += letter
    print(f"the {direction}d text is:> {next_text}")

print(logo)

is_continue = True
while is_continue:
    direction = input("Type 'encode' to encript and 'decode' to decript:> ")
    text = input("Type your message:> ").lower()
    shift = int(input("Type the shift number:> "))
    # shift = shift % 26  
    ceaser(start_text=text, shift_amount=shift, direction=direction) # Function Call

    repeat_choice = input("Type 'yes' if you want to go again. Otherwise 'no'.:> ")

    if repeat_choice == "no":
        is_continue = False
        print("Good by!")