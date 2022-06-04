from base64 import decode, encode
import string

alphabet = string.ascii_lowercase

def encode(plain_text, shift_amount):
    encrypted_text = ''
    for char in plain_text:
        if char == ' ':
            encrypted_text += ' '
        else:    
            position = alphabet.index(char)
            new_position = position + shift_amount
            while new_position >= 26:
                new_position -= 26
            encrypted_text += alphabet[new_position]
    
    print(f"The encoded text is {encrypted_text}")

def decode(encrypted_text, shift_amount):
    decoded_text = ''
    
    for char in encrypted_text:
        if char == ' ':
            decoded_text += ' '
        else:
            position = alphabet.index(char)
            new_position = position - shift_amount
            
            while new_position < 0:
                new_position += 26
            decoded_text += alphabet[new_position]
    
    print(f"The decoded text is {decoded_text}")
    
    
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encode(text, shift)
    elif direction == "decode":
        decode(text, shift)
    else:
        break