



try:
    file = open("myfile.txt", mode='w')
    print("file opened")
except FileNotFoundError as error_message:
        print(f"file not found error {error_message}")
else:
    content = file.read()
finally:
    print("This is finally block")