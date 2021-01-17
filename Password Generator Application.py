# importing the tkinter module
from tkinter import *
from PIL import Image, ImageTk

# importing the pyperclip module to use it to copy our generated
# password to clipboard
import pyperclip

# random module will be used in generating the random password
import random

# initializing the tkinter
root = Tk()
root.title("RANDOM PASSWORD GENERATOR")

# Uploading the background image in GUI
render = PhotoImage(file="C:\\Users\\Ankit\\PycharmProject\\Mini Project\\photo.png")
img = Label(root, image=render)
img.place(x=0, y=0)

# setting the width and height of the gui
root.geometry("650x450")    # x is small case here
root.wm_minsize(650, 450)
root.wm_maxsize(650, 450)

# Uploading the Image in GUI
image = Image.open("images.png")
photo = ImageTk.PhotoImage(image)

# declaring a variable of string type and this variable will be
# used to store the password generated
passstr = StringVar()

# declaring a variable of integer type which will be used to
# store the length of the password entered by the user
passlen = IntVar()

# setting the length of the password to zero initially
passlen.set(0)

# function to generate the password
def generate():
    # storing the keys in a list which will be used to generate
    # the password
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
            '*', '(', ')']

    # declaring the empty string
    password = ""

    # loop to generate the random password of the length entered
    # by the user
    for x in range(passlen.get()):
        password = password + random.choice(pass1)

    # setting the password to the entry widget
    passstr.set(password)

# function to copy the password to the clipboard
def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

# Creating a text label widget
Label(root, text="RANDOM PASSWORD GENERATOR", font="Algerian 20 italic", bg= "pink", fg= "#0000FF").pack()

# Creating a text label widget
Label(root, text="Enter the password length", font="Algerian 20 italic", bg="pink", fg= "#0000FF").pack(pady=3)

# Creating a entry widget to take password length entered by the
# user
Entry(root, textvariable=passlen).pack(pady=3)

# button to call the generate function
Button(root, text="Generate Password", bg="pink", command=generate).pack(pady=7)

# entry widget to show the generated password
Entry(root, textvariable=passstr).pack(pady=3)

# button to call the copy to clipboard function
Button(root, text="Copy to clipboard", bg="pink", command=copytoclipboard).pack()
radio_low = Radiobutton(root, text="Low", value=1)
radio_low.pack(padx=5)
radio_middle = Radiobutton(root, text="Medium", value=0)
radio_middle.pack(padx=6)
radio_strong = Radiobutton(root, text="Strong", value=3)
radio_strong.pack(ipadx=50)

label = Label(image=photo)
label.pack()

# mainloop() is an infinite loop used to run the application when
# it's in ready state
root.mainloop()