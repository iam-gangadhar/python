

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z',]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")


def encrypt(txt, sft):
    cipher_text = '' 
    for letter in txt:
        position = alphabet.index(letter)
        new_position = position + sft
        cipher_text += alphabet[new_position]

        # for i in alphabet:
        #     if letter == i:
        #         n_letter = alphabet[possition+sft]
        #         cipher_text += n_letter
        #         break
        #     possition += 1
    print(cipher_text)

def decrypt(_text, _shift):
    decrypt_text = ''
    for letter in _text:
        position = alphabet.index(letter)
        new_position = position - _shift
        decrypt_text += alphabet[new_position]
    print(decrypt_text)

if direction == 'encode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text, shift)
elif direction == 'decode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decrypt(text, shift)
else:
    print("Invalid Word Entry.. Try Again")






#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 