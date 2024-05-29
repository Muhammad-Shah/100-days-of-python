# Ceaser Cipher Starting
alpabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encript and 'decode' to decript:> ")
text = input("Type your message:> ").lower()
shift = int(input("Type the shift number:> "))
# Creating function called 'encript' that takes "text" and "shift" as input
def encript(plain_text, shift_text):
    encript_text = ""
    # Inside the 'encript' function, 'shift' each letter of the text forward in the alpabets by the shift amount and print the encripted text
    # plain_text = "hello"
    # shift = 5
    # encript_text = "mjqqt"
    for letter in plain_text:
        position = alpabets.index(letter)
        new_position = position + shift_text
        new_letter = alpabets[new_position]   
        encript_text += new_letter
    print(f"The encoded text is:> {encript_text}")
# Call the encript function and pass in the user inputs. You should be able to test the code and encript a message
encript(plain_text=text, shift_text=shift)