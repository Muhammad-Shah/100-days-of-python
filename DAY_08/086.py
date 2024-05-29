# Ceaser Cipher Starting

alpabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encript and 'decode' to decript:> ")
text = input("Type your message:> ").lower()
shift = int(input("Type the shift number:> "))
# Combine the encript() and decrypt() functions into a single function called ceaser()
def ceaser(start_text, shift_amount, direction):
    next_text = ""
    if direction == "decode":
            shift_amount *= -1
    for letter in start_text:
        position = alpabets.index(letter)    
        new_position = position + shift_amount
        new_letter = alpabets[new_position]   
        next_text += new_letter
    print(f"the {direction}d text is:> {next_text}")

ceaser(previous_text=text, shift_amount=shift, direction=direction)
