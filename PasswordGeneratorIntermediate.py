# random password generator

# importing libraries
from tkinter import *
import random
import string
import pyperclip

# creating a window
root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("PASSWORD GENERATOR - Karolina Koval May 2023")

#app name
heading = Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack()
Label(root, text ='Karolina Koval', font ='arial 15 bold').pack(side = BOTTOM)

# defining password length
pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).pack()

# defining a function to generate a password
pass_str = StringVar()
def Generator():
    password = ''
    for x in range (0,4):
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(pass_len.get() - 4):
        password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

# displaying an output after clicking a button
Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)

Entry(root, textvariable = pass_str).pack()

# defining a function to copy a password
def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)

root.mainloop()