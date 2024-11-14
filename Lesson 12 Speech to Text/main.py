#pip3 install Pyaudio or pip install Pyaudio
#pip install SpeechRecognition

from tkinter import *
import speech_recognition as sr     # import the library
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *


root= Tk()
root.title("Speech to Text")
root.geometry("800x400")

#heading 
heading1 = Label(root, text = "Voice Notepad",font = "bold, 30 ")
heading1.grid(row=0,column=1,padx=20,pady=20)

Output_text = Text(root, height= 4, width = 40)
Output_text.grid(row=1,column=1,pady = 20,padx=20)

#function     
def Translate():
    r = sr.Recognizer()                 # initialize recognize
    with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
        print("Speak Anything ")
        audio = r.listen(source)        # listen to the source
        try:
            text = r.recognize_google(audio)    # use recognizer to convert our audio into text part.
        except:
            text="Sorry could not recognize your voice"
        Output_text.delete(1.0, END)
        Output_text.insert(END,text)

        
def save():
    fout=asksaveasfile(defaultextension=".txt") 
    if fout:
        print(Output_text.get(1.0,END),file=fout)      
    else:
        messagebox.showinfo("Warning", "Text not saved")

  

# our Translate function using command = Translate 
trans_btn = Button(root, text = 'Click on me!..\nTo start recording',
                   command = Translate,width=20)
trans_btn.grid(row=1,column=0,pady = 20,padx=20)

save_button = Button(root, text='Save the Text',width=20,command=save)
save_button.grid(row = 1, column = 2,pady = 10,columnspan=3)

# start the gui 
root.mainloop() 