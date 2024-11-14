#pip install gTTS
# importing required module
from tkinter import *
#Google Text-to-Speech Library
from gtts import gTTS
import os

# create tkinter window
root = Tk()

root.title("text_to_speech_convertor")
root.geometry("750x500")


frame1 = Frame(root,bg="lightPink",height="150")
frame1.pack(fill=X)

frame2 = Frame(root,bg="lightgreen",height="750")
frame2.pack(fill=X)


label = Label(frame1, text="Text to Speech",font="bold, 30",bg="lightpink")
label.place(x=180, y=70)

entry = Entry(frame2, width=45,bd=4, font=14)
entry.place(x=130, y=52)

def play():
    # Language in which you want to convert
    language = "en"

    #slow=False - have a high speed
    myobj = gTTS(text=entry.get(),lang=language,slow=False)

    # save the audio
    myobj.save("convert.wav")
    #Play the saved audio file
    os.system("convert.wav")



btn = Button(frame2, text="SUBMIT",width="15", pady=10,font="bold, 15",command=play, bg='yellow')
btn.place(x=250, y=130)


# start the gui
root.mainloop()
