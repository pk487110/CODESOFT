#!/usr/bin/env python
# coding: utf-8

# In[79]:


# importing the tkinter module
from tkinter import *

# importing the pyperclip module to use it to copy our generated 
# password to clipboard
import pyperclip

# random module will be used in generating the random password
import random

# initializing the tkinter
root = Tk()

# # setting the width and height of the gui
root.title("Password Generator")
root.geometry("400x400")    # x is small case here
root.config(bg="#fbe3e8")

# # declaring a variable of string type and this variable will be 
# # used to store the password generated
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

# # Creating a text label widget
Label(root, text="Password Generator Application",bg="#fbe3e8",font="calibri 20 bold").place(x=20,y=10)

# # Creating a text label widget
Label(root, text="Enter password length :",font="calibri 12 bold",bg="#fbe3e8").place(x=10,y=90)


# # Creating a entry widget to take password length entered by the 
# # user
Entry(root, textvariable=passlen ,width=30).place(x=190,y=94)

# # button to call the generate function
Button(root, text="Generate Password", command=generate,bg="#5adbb5",fg="#f5f7f7",font="calibri 10 bold").place(x=140,y=130)

Label(root, text="Your Password is  - ",font="calibri 12 bold",bg="#fbe3e8").place(x=10,y=190)

Entry(root, textvariable=passstr,width=37).place(x=160,y=194)


Button(root, text="Copy to clipboard", command=copytoclipboard,bg="#4681f4",fg="#f5f7f7",font="calibri 10 bold").place(x=140,y=230)


root.mainloop()


# In[ ]:





# In[ ]:
