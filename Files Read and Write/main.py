# How to read files in python

# first Open the file using Open method
file = open("sampledata.txt")

# reading the data using read method
file_data = file.read()
print(file_data)

# after worke done close the file to free up space.
file.close()
print("file Closed")
print('------------------------------------------')
# Using with keyword to open the file and close the file automatically.
with open("sampledata.txt", mode='a') as file:
    file.write("\n I added this new data ")

with open("sample.txt", mode="w") as file2:
    file2.write("Sample Text in new file2")


# mode = r used for Read the file data
# mode = w used for write the file in to the data. if data existed will be deleted new data added.
# mode = a used to append the data
print("___---------------------------")

filename = r'C:/Users/GK/Desktop/sampledata.txt'
cpath = r'C:/data/mysample.txt'
with open(cpath,mode='w') as dfile:
    dfile.write("Adding some data to this files")
    print(dfile)

print('Added the data END...')