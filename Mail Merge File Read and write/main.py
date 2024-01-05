#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Reading The names
names = []
with open("./Input/Names/invited_names.txt", mode='r') as name:
    for k in name:
        clean_k = k.replace('\n',"")
        print(clean_k)
        names.append(clean_k)

s_letter = ""
with open("./Input/Letters/starting_letter.txt", mode='r') as letter:
     data = letter.read()
     s_letter += data

print(names)
for l in names:
    new_letter = s_letter.replace("[name]", l)
    with open(f"./Output/{l}.txt", mode='w') as n_letter:
        n_letter.write(new_letter)

