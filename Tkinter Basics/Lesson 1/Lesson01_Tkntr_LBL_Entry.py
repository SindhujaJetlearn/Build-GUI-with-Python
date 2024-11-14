from tkinter import *

root = Tk()
root.title("Login Me")
root.config(background="pink")
root.geometry("450x300")

# the label for user_name
user_name = Label(root,text="Username").place(x=40,y=60)
user_name_entry = Entry(root,width=30,).place(x=110,y=60)

# the label for user_password
user_password = Label(root,text="Password").place(x=40,y=100)
user_password_entry = Entry(root,show='*',width=30).place(x=110,y=100)

submit_button = Button(root,text="Submit").place(x=40,y=130)

root.mainloop()