from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"


# TO-DO 2 Implementing the Logic for creating Display Random Word
data = pandas.read_csv("data/words_to_learn.csv")
to_learn = data.to_dict(orient="records")

#print(data['Telugu'][5])
current_card = {}

def random_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(english_word, text=current_card["English"],fill="black")
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(canvas_background, image=photo_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="తెలుగు", fill="white")
    canvas.itemconfig(english_word, text=current_card["Telugu"], fill="white")
    canvas.itemconfig(canvas_background, image=photo_back)
    random_word()

def is_known():
    to_learn.remove(current_card)  # Removing the word from current dictionary
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")
    flip_card()


# User Interface Creation
window = Tk()
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
window.title("Learn English Using FlashCard by Gangadhar")

flip_timer = window.after(3000, func=flip_card)



canvas = Canvas(width=800, height=526)
photo_front = PhotoImage(file="images/card_front.png")
canvas_background = canvas.create_image(400,263, image=photo_front)
card_title = canvas.create_text(400,150,text="English",font=("Arial", 40, "bold"))
english_word = canvas.create_text(400,263, text="?", font=("Arial", 60, "bold"))

canvas.grid(row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

photo_back = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")


# Button Adding Right and Wrong

right_button = Button(image=right, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=0,)

wrong_button = Button(image=wrong, highlightthickness=0, command=random_word)
wrong_button.grid(row=1, column=1)






window.mainloop()