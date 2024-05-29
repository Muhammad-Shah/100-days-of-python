# Ceaser Cipher Starting

alpabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encript and 'decode' to decript:> ")
text = input("Type your message:> ").lower()
shift = int(input("Type the shift number:> "))
def encript(plain_text, shift_amount):
    encript_text = ""
    # encript_text = "mjqqt"
    for letter in plain_text:
        position = alpabets.index(letter)
        new_position = position + shift_amount
        new_letter = alpabets[new_position]   
        encript_text += new_letter
    print(f"The encoded text is:> {encript_text}")
# Create a different function called 'decrept' that takes the 'text' and 'shift' as input
def decrypt(encript_text, shift_amount):
    plain_text = ""
    # Inside the decrypt function shift each letter of the text backward in the alphabet by the shift amount and print the decrypted text
    # e.g
    # encrypted_text = "mjqqt"
    # shift = 5
    # plain_text = "hello"
    for letter in encript_text:
        position = alpabets.index(letter)
        new_position = position - shift_amount
        new_letter = alpabets[new_position]
        plain_text += new_letter
    print(f"The decoded text is:> {plain_text}")

if direction == "encode":
    encript(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(encript_text=text, shift_amount=shift)
else:
    print("Wrong Input, Input Either 'encode' or 'decode' ")
