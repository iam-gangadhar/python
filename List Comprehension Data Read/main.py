

with open("file1.txt", mode='r') as file1:
        First_list = file1.readlines()
        first_list = [int(n.replace('\n',' ') )for n in First_list]
        print(first_list)

with open("file2.txt", mode='r') as file2:
    second_list = file2.readlines()
    second_list = [int(n.replace('\n', ' ')) for n in second_list]
    print(second_list)

result = [n for n in first_list if n in second_list]
print(result)