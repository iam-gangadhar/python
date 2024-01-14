import json
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_numbers + password_symbol
    random.shuffle(password_list)
    password = "".join(password_list)
    print(f"Your password is: {password}")

    entry_Pass.delete(0, END)
    entry_Pass.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear_field():
    entry_web.delete(0, END)
    # entry_Email.delete(0,END)
    entry_Pass.delete(0, END)


def save_password():
    website_name = entry_web.get()
    email_id = entry_Email.get()
    pass_word = entry_Pass.get()
    new_data = {
        website_name: {
            "email": email_id,
            "password": pass_word
        }
    }
    if len(website_name) == 0 or len(pass_word) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have to fill all the details")
    else:
        try:
            with open("mydata.json", "r") as data_file:
                # Reading the Json Data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("mydata.json", mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating the Data if file is already There
            data.update(new_data)
            with open("mydata.json", "w") as data_file:
                #Saving update data
                json.dump(data, data_file, indent=4)
        finally:
            clear_field()

    # user_entry = f"{website_name} | {email_id} | {pass_word} \n"
    # if len(website_name) == 0 or len(pass_word) == 0:
    #     messagebox.showinfo(title="Oops", message="Please don't leave any field")
    # else:
    #     is_ok = messagebox.askokcancel(title=website_name, message=user_entry)
    #     if is_ok:
    #         with open("data.json", mode='w') as file:
    #             file.writelines(user_entry)
    #         clear_field()
def find_password():
    website = entry_web.get()
    with open("mydata.json") as data_file:
        data = json.load(data_file)
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \n Password: {password}")

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="black")

canvas = Canvas(height=200, width=200, bg="black")
logo_mypass = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_mypass)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website: ", fg="white", bg="black", font=("Arial", 10, "bold"))
Email_label = Label(text="Email/Username: ", fg="white", bg="black", font=("Arial", 10, "bold"))
password_label = Label(text="Password: ", fg="white", bg="black", font=("Arial", 10, "bold"))

website_label.grid(row=1, column=0)
Email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

# input boxs
entry_web = Entry(width=21)
entry_Email = Entry(width=21)
entry_Pass = Entry(width=21)

entry_web.grid(row=1, column=1,)
entry_Email.grid(row=2, column=1)
entry_Email.insert(0, "gangadhar@gmail.com")
entry_Pass.grid(row=3, column=1)
entry_Pass.insert(0, "Enter Your Password")

# Buttons
btn_generate = Button(text="Generate Password", command=generate_password)
btn_add = Button(text="Add", width=25, command=save_password)
btn_search = Button(text="Search", width=12, command=find_password)

btn_generate.grid(row=3, column=2)
btn_add.grid(row=4, column=1, )
btn_search.grid(row=1, column=2)

window.mainloop()
