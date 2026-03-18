import tkinter
import math
import tkinter.messagebox
import random

root = tkinter.Tk()
root.minsize(550, 360)
root.title('Guess the number')

number = random.randint(1, 20)

def check_num():
    guess = int()

    tkinter.messagebox.showinfo('High', 'Your guess is too high')

def btn_confirm():
    print('hiruka')

label = tkinter.Label(root, text = 'Welcome to our game!')
label.pack()

label_name = tkinter.Label(root, text = 'What is your name?')
label_name.place(x = 10, y = 105)

text_name = tkinter.Entry(root, width = 20)
text_name.place(x = 10, y = 90)

btnOK = tkinter.Button(root, text = 'OK', command = btn_confirm)
btnOK.place(x = 200, y = 90, height = 30)

btnGuess = tkinter.Button(root, text = 'Guess', command = btn_confirm)
btnGuess.place(x = 200, y = 150, height = 30)

text_Guess = tkinter.Entry(root, width = 20)
text_Guess.place(x = 10, y = 150)

label_Guess = tkinter.Label(root, text = 'Guess a number from 1-20')
label_Guess.place(x = 10, y = 165)

root.mainloop()

