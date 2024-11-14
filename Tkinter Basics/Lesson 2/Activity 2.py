# importing tkinter module
from tkinter import *
from tkinter.ttk import *
import time

# creating tkinter window
root = Tk()

# Progress bar widget
progress = Progressbar(root, orient=HORIZONTAL,length=100, mode='determinate')


# Function responsible for the updation of the progress bar value
def bar():  
    progress['value'] = 20
    #flushes all currently-scheduled idle events from Tcl's event queue. 
    #Idle events are used to postpone processing until “there is nothing else to do”, 
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 40
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 50
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 60
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 80
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 100


progress.pack(pady=10)

# This button will initialize
# the progress bar
btn= Button(root, text='Start', command=bar)
btn.pack(pady=10)

# infinite loop
root.mainloop()