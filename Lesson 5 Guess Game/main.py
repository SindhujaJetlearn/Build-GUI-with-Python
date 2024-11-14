import tkinter
import tkinter.messagebox
import random

root = tkinter.Tk()
root.minsize(350, 260)
root.title('Guess the number game')

number = random.randint(1, 20)

def check_num():
    guess = text_guess.get()
    guess = int(guess)
    if guess > number:
        tkinter.messagebox.showinfo("High", "Your guess is too heigh.")
    if guess < number:
        tkinter.messagebox.showinfo("Low", "Your guess is too low.")
    if guess == number:
        tkinter.messagebox.showinfo("Good", "Good job!")      


def btn_confirm():
    myName = text_name.get()
    #showinfo("Screen_title",text)
    tkinter.messagebox.showinfo("Name", 'Well,' + myName + ',I am thinking of a number between 1 and 20.')


# name
label = tkinter.Label(root, text="Welcome to our game!")
label.pack()

label_name = tkinter.Label(root, text="What's your name?")
label_name.place(x=10, y=60)

text_name = tkinter.Entry(root, width=20)
text_name.place(x=10, y=90)

btnOK = tkinter.Button(root, text="OK", command=btn_confirm)
btnOK.place(x=200, y=90, height=28)

# input
label_guess = tkinter.Label(root, text='Take a guess:')
label_guess.place(x=10, y=150)

text_guess = tkinter.Entry(root, width=10)
text_guess.place(x=90, y=150)

btnCheck = tkinter.Button(root, text='Guess', command=check_num)
btnCheck.place(x=200, y=150, width=45, height=28)

root.mainloop()