alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z',]
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    cipher_text = '' 
    for letter in text:
        position = alphabet.index(letter)
        if direction == 'encode':
            new_position = position + shift
            cipher_text += alphabet[new_position]
        elif direction == 'decode':
            new_position = position - shift
            cipher_text += alphabet[new_position]
        else:
            print("Wrong Word Typed ... bye!")
            break
    print(cipher_text)
    
caesar(text,shift,direction=direction)


