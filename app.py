
# -----------------  Password Generator ----------------- #
# author: Sayed Mohammad Rezaie -- 10.Nov.2020
# github: @cdied

# description:
# 1. simple password generator
# 2. simple GUI using tkinter
# 3. generating password with the given lenght
# 4. imports tkinter, random and string

# ----------------------  imports  ---------------------- #

from tkinter import *
import random
import string


# ---------------------  Functions  --------------------- #

# defining int for lenght of password
lenght = 0

# Function ran() for genarating random password with ...
# (lenght)character of string with 2 digit int at the end
def ran(lenght):
    character = string.ascii_letters  
    myStr =""
    myStr = "".join(random.choice(character) for i in range(lenght-2))
    num = 0
    num = random.randrange(10, 99)
    return (myStr+str(num))
    
# Function generate() for get the output of function ran() ...
# and display it on screen
def generate(lenght):
    lenght = 0
    lenght = int(spinbox.get())
    password = ""
    password = (ran(lenght))
    if lenght<8:
        password = "Not enough character"
    elif lenght>20:
        password = "Too many character"
    else:
        pass
    Label(root, text=password, background="#1A3D56", foreground="WHITE", font=("Cambria", 16, "bold")).place(relx=0.5, rely=0.8, anchor=CENTER, width=310)


# ------------------------  GUI  ------------------------ #

root = Tk()
root.title("Password Generator")

canvas = Canvas(root, background="#1A3D56", width=500, height=270).pack()

wlable = Label(root, text="Welcome to Password Generator", background="#1A3D56", foreground="WHITE")
wlable.place(relx=0.5, rely=0.1, anchor=CENTER)

elable = Label(root, text="Enter Password lenght 8-20", background="#1A3D56", foreground="WHITE")
elable.place(relx=0.10, rely=0.25, width=150, height=30)

spinbox = Spinbox(root, from_= 0, to = 20, background="#1A3D56", foreground="WHITE")
spinbox.place(relx=0.5, rely=0.25, width=200, height=30)

button = Button(root, text="Generate Password", command=lambda:generate(lenght))
button.place(relx=0.5, rely=0.55, width=200, height=30, anchor=CENTER)


root.mainloop()
