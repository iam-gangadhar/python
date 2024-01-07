student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

alphabet_dict = {}
#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
for (key, value) in data.iterrows():
    letter = value['letter']
    word = value['code']
    alphabet_dict[letter] = word

# print(alphabet_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

userinput = input("Enter name to Give Alphabet Abbrivation: ").upper()
user_list = list(userinput)

name = []
for letter in user_list:
    for (key,value) in alphabet_dict.items():
        if key == letter:
            name.append(value)
print(name)

