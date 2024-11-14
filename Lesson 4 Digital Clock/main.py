# https://geeksforgeeks.org/how-to-use-strptime-with-milliseconds-in-python/

from tkinter import *
from tkinter.ttk import *

from time import strftime


root = Tk()
root.title('Clock')


lbl = Label(root, font=('calibri', 40, 'bold'),background='orange',foreground='white')
# Placing clock at the centre of the tkinter window
lbl.pack(anchor='center')

def time():
    string=strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

time()

mainloop()