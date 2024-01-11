from tkinter import *

window = Tk()
window.minsize(width=300, height=150)
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)

input_m = Entry()
input_m.grid(column=1, row=0)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_2 = Label(text="Is Equal to ")
label_2.grid(column=0, row=2)

km_label = Label(text="0")
km_label.grid(column=1, row=2)

km = Label(text="KM")
km.grid(column=2, row=2)

def milestokm():
    miles = input_m.get()
    km = int(miles) * 1.609344
    km_label.config(text=f"{round(km,2)}")


calc_button = Button(text="Calculate", command=milestokm)
calc_button.grid(column=1, row=3)







window.mainloop()
