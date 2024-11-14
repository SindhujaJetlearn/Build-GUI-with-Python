from tkinter import *
import tkinter.font as font
import random

player_score = 0
computer_score = 0
options = [('rock',0), ('paper',1), ('scissors',2)]

def computer_wins():
    global computer_score, player_score
    computer_score += 1
    winner_label.config(text="Computer Won!!!")
    computer_score_label.config(text='Computer Score : ' + str(computer_score))
    player_score_label.config(text='Player Score : ' + str(player_score))

def player_wins():
    global computer_score, player_score
    player_score += 1
    winner_label.config(text="Player Won!!!")
    computer_score_label.config(text='Computer Score : ' + str(computer_score))
    player_score_label.config(text='Player Score : ' + str(player_score))

def tie():
    global computer_score, player_score
    winner_label.config(text="TIE!!!")
    computer_score_label.config(text='Computer Score : ' + str(computer_score))
    player_score_label.config(text='Player Score : ' + str(player_score))

def player_choice(player_input):
    global player_score, computer_score
    print(player_input)

    computer_input = get_computer_choice()
    print(computer_input)
    player_choice_label.config(text = 'Your Selected : ' + player_input[0])
    computer_choice_label.config(text = 'Computer Selected : ' + computer_input[0])

    if(player_input == computer_input):
        tie()

    #if the player has chosen rock
    if(player_input[1] == 0):
        if(computer_input[1] == 1):
            #this means the computer wins
            computer_wins()
        elif (computer_input[1] == 2):
            #this means the player wins
            player_wins()

    #if the player has paper
    elif(player_input[1] == 1):
        if(computer_input[1] == 0):
            #this means the player wins
            player_wins()
        elif (computer_input[1] == 2):
            #this means the computer wins
            computer_wins()

    #if the player has scissors
    elif(player_input[1] == 2):
        if(computer_input[1] == 0):
            #this means the computer wins
            computer_wins()
        elif (computer_input[1] == 1):
            #this means the player wins
            player_wins()
            

#Function to Randomly Select Computer Choice
def get_computer_choice():
    return random.choice(options)

#Desiging

root = Tk()
root.title("Rock Paper Scissors Game")

app_font = font.Font(size = 12)

#Displaying Game Title
game_title = Label(text = 'Rock Paper Scissors', font = font.Font(size = 20), fg = 'grey')
game_title.pack()

#Label to dispay, who wins each time
winner_label = Label(text = "Let's Start the Game...", fg = 'green', font = font.Font(size = 13), pady = 8)
winner_label.pack()

input_frame = Frame(root)
input_frame.pack()

#Displaying player options
player_options = Label(input_frame, text = "Your Options : ", font = app_font, fg = 'grey')
player_options.grid(row = 0, column = 0, pady = 8)

rock_btn = Button(input_frame, text = 'Rock', width = 15, bd = 0, bg = 'pink', pady = 5, command = lambda: player_choice(options[0]))
rock_btn.grid(row = 1, column = 1, padx = 8, pady = 5)

paper_btn = Button(input_frame, text = 'Paper', width = 15, bd = 0, bg = 'silver', pady = 5, command = lambda: player_choice(options[1]))
paper_btn.grid(row = 1, column = 2, padx = 8, pady = 5)

scissors_btn = Button(input_frame, text = 'Scissors', width = 15, bd = 0, bg = 'light blue', pady = 5, command = lambda: player_choice(options[2]))
scissors_btn.grid(row = 1, column = 3, padx = 8, pady = 5)

#Displaying Score and players choise
score_label = Label(input_frame, text = 'Score : ', font = app_font, fg = 'grey')
score_label.grid(row = 2, column = 0)

player_choice_label = Label(input_frame, text = 'Your Selected : ---', font = app_font)
player_choice_label.grid(row = 3, column = 1, pady = 5)

player_score_label = Label(input_frame, text = 'Your Score : -', font = app_font)
player_score_label.grid(row = 3, column = 2, pady = 5)

computer_choice_label = Label(input_frame, text = 'Computer Selected : ---', font = app_font, fg = 'black')
computer_choice_label.grid(row = 4, column = 1, pady = 5)

computer_score_label = Label(input_frame, text = 'Computer Score : -', font = app_font, fg = 'black')
computer_score_label.grid(row = 4, column = 2, padx = (10,0), pady = 5)

root.geometry('700x300')
#root.configure(background='cadetblue')
root.mainloop()