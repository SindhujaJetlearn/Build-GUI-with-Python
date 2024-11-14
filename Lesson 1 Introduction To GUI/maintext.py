from tkinter import *
import calendar

# Function for showing the calendar of the given year
def showCal():
    # Create a GUI window
    new_gui = Tk()

    # Set the background colour of GUI window
    new_gui.config(background="white")

    # set the name of tkinter GUI window
    new_gui.title("CALENDER")

    # Set the configuration of GUI window
    new_gui.geometry("1000x1000")

    # get method returns current text as string
    fetch_year = int(year_field.get())
    #print("fetch_year",fetch_year)

    # calendar method of calendar module return the calendar of the given year .
    cal_content = calendar.calendar(fetch_year)
    #print("cal_content :",cal_content)

    # Create a Text for showing the content of the calender
    cal_year = Text(new_gui,font="Consolas 10 bold")
    cal_year.insert(END,cal_content)

    # grid method is used for placing the widgets at respective positions in table like structure.
    cal_year.grid(row=1, column=1,padx=5)

    # start the GUI
    new_gui.mainloop()


#Design of Calendar
# Create a GUI window
gui = Tk()

# Set the background colour of GUI window
gui.config(background="white")

# set the name of tkinter GUI window
gui.title("CALENDER")

# Set the configuration of GUI window
gui.geometry("250x140")

# Create a CALENDAR : label with specified font and size
cal = Label(gui, text="CALENDAR", bg="dark gray",
            font=("times", 28, 'bold'))
# grid method is used for placing the widgets at respective positions in table like structure.
cal.grid(row=1, column=1)

# Create a Enter Year : label
year = Label(gui, text="Enter Year", bg="light green")
year.grid(row=2, column=1)

# Create a text entry box for filling or typing the information.
year_field = Entry(gui)
year_field.grid(row=3, column=1)

# Create a Show Calendar Button and attached to showCal function
Show = Button(gui, text="Show Calendar", fg="Black",bg="Red", command=showCal)
Show.grid(row=4, column=1)

# Create a Exit Button and attached to exit function
Exit = Button(gui, text="Exit", fg="Black", bg="Red", command=exit)
Exit.grid(row=6, column=1)


# start the GUI
gui.mainloop()